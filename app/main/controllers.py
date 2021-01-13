import sys
import os

from flask import Blueprint, render_template, redirect, flash
from webapp.main.forms import AdditionForm

from celery.result import AsyncResult
from tasks import add

main_blueprint = Blueprint(
    'main', 
    __name__,
    template_folder='../templates/main'
)

#from data import read_sdf

def urlfmt(row):
    acct = row['ACCOUNT_ID']
    display = row['ACCOUNT_ID']
    return "<a href=\"https://apps.co.clatsop.or.us/property/property_details/?a=%s\">%s</a>" % (acct,display)

def s2i(s):
    """ Convert a string to an integer even if it has + and , in it. """
    if s == None or s == '':
        return None
    if type(s) == type(0):
        # This is already an integer
        return s
    if s:
        return int(float(s.replace(',', '')))
    return None

@main_blueprint.route('/', methods=['GET','POST'])
def index():
    # this needs to be asynchronous
#    rawdf = read_sdf(Config.TABLE_URL)

 #   sdf = rawdf.drop(labels='SHAPE', axis=1).set_index('OBJECTID')
  #  sdf['property_details'] = sdf.apply(urlfmt, axis=1)

    form = AdditionForm()
    if form.validate_on_submit():
        # We've received input.

        try:
            x = s2i(form.x.data)
            y = s2i(form.y.data)
            print("Here is where you need to queue the request.",x,y)
            task = add.delay(x,y)
            async_result = AsyncResult(id=task.task_id, app=celery)
            add_result = async_result.get()
            return add_result
        except Exception as e:
            print("Can't get values", e)
            error = e
            return redirect("/fail")      
        
    # Prefill the data entry form
#    form.x.data = "1"
 #   form.y.data = "1"

    return render_template('form_add.html', form=form, result=None) #, table=sdf.to_html(columns=['TAXMAPKEY', 'property_details'], header=True, escape=False, index=False, justify='right'))

@main_blueprint.route('/results', methods=['GET','POST'])
def results(x,y):
    form = AdditionForm()
    form.x.data = str(x)
    form.y.data = str(y)
    form.result.data = str(x + y)
    return render_template('form_add.html', form=form, results=2)


# That's all!
