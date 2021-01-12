import sys
import os

from flask import Blueprint, render_template, redirect, flash

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

@main_blueprint.route('/', methods=['GET'])
def index():
    # this needs to be asynchronous
#    rawdf = read_sdf(Config.TABLE_URL)

 #   sdf = rawdf.drop(labels='SHAPE', axis=1).set_index('OBJECTID')
  #  sdf['property_details'] = sdf.apply(urlfmt, axis=1)

    return render_template('main.html') #, table=sdf.to_html(columns=['TAXMAPKEY', 'property_details'], header=True, escape=False, index=False, justify='right'))

# That's all!
