import json
import requests  # see http://python-requests.org


def url_for(endpoint):
    return 'http://localhost:5000/{}/'.format(endpoint)


def delete_all_people():
    r = requests.delete(url_for('people'))
    print("'people' deleted, server response:", r.status_code)


def post_people():
    data = [
        {'firstname': 'John', 'lastname': 'Doe'},
        {'firstname': 'Mike', 'lastname': 'Green'},
    ]

    response = requests.post(
        url_for('people'),
        json.dumps(data), 
        headers={'Content-Type': 'application/json'}
    )
    print("'people' posted, server response:", response.status_code)


def get_people():
    r = requests.get(url_for('people'))
    print('people downloaded, server response:', r.status_code)

    if r.status_code == 200:
        people = r.json()['_items']
        print('{} people:'.format(len(people)))
        for person in people:
            print('{}, {}'.format(person['firstname'], person['_id']))


def main():
    delete_all_people()
    post_people()
    get_people()

if __name__ == '__main__':
    main()