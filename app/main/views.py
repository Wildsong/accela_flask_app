import sys
import os

from flask import Blueprint, render_template, redirect, flash
from . import main
from app.main.forms import AdditionForm

from flask import current_app
from .tasks import QueryParcels
from celery.result import AsyncResult

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

@main.route('/', methods=['GET','POST'])
def index():
    some_parcels = None
    form = AdditionForm()
    if form.validate_on_submit():
        # We've received input.

        try:
            q = s2i(form.x.data)
            task = QueryParcels.delay(q)
            async_result = AsyncResult(id=task.task_id, app=current_app.celery)
            some_parcels = async_result.get()
            #return z # I could render a totally different page here.

        except Exception as e:
            print("Can't get values", e)
            error = e
            return redirect("/fail")      
        
    return render_template('addition.html', form=form, result=some_parcels) #, table=sdf.to_html(columns=['TAXMAPKEY', 'property_details'], header=True, escape=False, index=False, justify='right'))

@main.route('/results', methods=['GET','POST'])
def results(x,y):
    form = AdditionForm()
    form.x.data = str(x)
    form.y.data = str(y)
    form.result.data = str(x + y)
    return render_template('addition.html', form=form, results=None)


# That's all!
