from database.queries import queries

def search_fields():
    return []

def search_filters():
    return []

def select_options():
    options = {}
    options['arch'] = ['x86', 'amd', 'x64']
    options['file_type'] = ['elf', 'pe', 'maco-o']
    options['os'] = ['linux', 'windows-10']
    options['intended_for'] = ['strncmp', 'strlen', 'strstr', 'scanf']
    return options 

def web_search_results(request_data, search_type = "ALL"):
    '''
        Returns a list of rows for the web table

    ...

    Parameters
    ----------
    request_data : json
        List of fields from the user web filter options

    ...
    Return Value
    ------------
    list of rows that contain SimProcedure information

    '''
    if search_type == "ALL":
        return queries.select_all()

    print(f"DEBUG: Received {request_data}")
    return []

def api_search_results():
    return {}
