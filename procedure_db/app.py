# Flask Imports
from flask import Flask
from flask import render_template
from flask import request, redirect, send_file

# 3rd Party Imports
import os, json, requests, shutil

# Custom Imports
from database import simdb
from database.db_setup import database_setup
app = Flask(__name__)

@app.route('/')
def dashboard():
    '''
        Landing Page

        Input:
            Expects no inputs

        returns:
            dashboard.html (document)
            search_fields (list)
            search_filters (list)
    '''
    database_setup.init_db()
    if database_setup == True:
        # Insert default data
        from database.db_setup import init_data
        init_data.default_data()

    search_fields = simdb.search_fields()
    search_filters = simdb.search_filters()
    select_options = simdb.select_options()
    search_results = simdb.web_search_results({})

    return render_template(
            "dashboard.html", search_fields = search_fields,
            search_filters = search_filters, select_options = select_options,
            search_results = search_results
    )

@app.route('/web_search_simprocedure', methods=['POST'])
def web_search_simprocedure():
    # return results for web UI
    
    try:
        request_data = request.get_json()
    except:
        return json.dumps({'success': False, 'data': {}}), \
            400, \
            {'ContentType': 'application/json'}
                
    if 'search_fields' not in request_data \
            or len(request_data['search_fields']) == 0:
        return json.dumps({'success': False, 'data': {}}), \
            400, \
            {'ContentType': 'application/json'}

    search_results = simdb.web_search_results(request_data)

    return json.dumps({'success': True, 'data': search_results}), \
        200, \
        {'ContentType': 'application/json'}


@app.route('/api_search_simprocedure', methods=['POST'])
def api_search_simprocedure():
    # request for API applications

    search_results = simdb.api_search_results()

    return json.dumps({'success': True, 'data': search_results}), 200, \
        {'ContentType': 'application/json'}


if __name__ == "__main__":
    IP = '0.0.0.0'
    port = 5000
    app.run(host = IP, port = port, debug = True)
