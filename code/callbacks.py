from datetime import date


def inject_signature(resource, response):
    """ This callback is executed every time a document (item)
    is fetched from the db and it is about to be returned to the client.
    """
    response['_signature'] = "Talk Python Training"

def add_age(resource, items):
    """ This callback is invoked every time a POST request hits the service,
    *before* the documents are sent to the db.
    """
    for item in items:
        if 'born' in item:
            today = date.today()
            item['age'] = today.year - item['born'].year