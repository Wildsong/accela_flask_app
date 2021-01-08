import sys
import os

from flask import render_template, redirect, flash
from app import app
#from app.forms import CasesForm
from config import Config

from data import read_sdf

VERSION = 'accela app 0.1'

def urlfmt(row):
    acct = row['ACCOUNT_ID']
    display = row['ACCOUNT_ID']
    return "<a href=\"https://apps.co.clatsop.or.us/property/property_details/?a=%s\">%s</a>" % (acct,display)

@app.route('/', methods=['GET'])
def home_page():
    # this needs to be asynchronous
    rawdf = read_sdf(Config.TABLE_URL)

    sdf = rawdf.drop(labels='SHAPE', axis=1).set_index('OBJECTID')
    sdf['property_details'] = sdf.apply(urlfmt, axis=1)

    return render_template('home.html', table=sdf.to_html(columns=['TAXMAPKEY', 'property_details'], header=True, escape=False, index=False, justify='right'))

# That's all!
