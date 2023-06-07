import requests
import pprint
from db_connector import DBConnector
import rest_app


# Constants _

host = 'sql.freedb.tech'
port = 3306
user = 'freedb_haggai'
password = '7p8Gc!Ycp!MB?%A'
database = 'freedb_users_10'


# initialize the DBConnector class
db = DBConnector(host, port, user, password, database)


error_codes = [500, 400]
# input id and user
while True:
    try:
        user_id = input("Enter user id: ")
        if user_id.isdigit():
            break
        else:
            print("Please enter a valid numeric value.")
    except ValueError:
        print("Please enter a number.")

while True:
    user_name = input("Enter user name: ")
    if any(char.isalpha() for char in user_name):
        break
    else:
        print("Please enter a valid string value.")

api_url = "http://127.0.0.1:5000/data/"+str(user_id)
url = f"http://127.0.0.1:5000/data/" + user_id

# Payload data
data = {
    'user_id': user_id,
    'user_name': user_name
    }

# 1
# POST - test a post of a new user data with the REST API method
res = requests.post(url, json=data)

# Check if the flask server return OK
print("**** Checking if the flask server return OK ****")
user_name = ''
if res.status_code == 200:
    db_user_name = res.json()['user_added']

    msg = f'user: {db_user_name} successfully created  \n\n' \
        f'json output:\n{res.json()}'
    print(msg)
    print()

elif res.status_code in error_codes:
    reason = res.json()['reason']

    msg = f'POST failed, reason: {reason}\n\n' \
          f'json output:\n{res.json()}'
    print(msg)
    print()

else:
    print(f'Post failed with code {res.status_code}')
    print()


# Submit a GET request to make sure status code is 200 and data equals to the
# posted data.
print("**** Users names check ****")
get_res = requests.get(url)
if get_res.status_code == 200:
    db_user_name = get_res.json()['user_name']

    if db_user_name == user_name:
        msg = f'DB user name: {db_user_name} \n\n' \
            f'json output: \n{get_res.json()}'
        print(msg)
        print()

    else:
        msg = f'entered user name: {user_name} \nDB user name: {db_user_name} \n' \
              f'MSG:  entered user name doesnt match to the DB user name'
        print(msg)
        print()

elif get_res.status_code == 500:
    reason = get_res.json()['reason']

    msg = f'GET failed with reason: {reason} \n\n' \
          f'this is the json output:\n{get_res.json()}'
    print(msg)
    print()

else:
    print(f'Get failed with status code{get_res.status_code}')
    print()

print("**** DB users check ****")

db_user_name = db.get_user_name(user_id)


msg = f'entered user name:{user_name}\n'\
    f'DB user name:{db_user_name}\n\n'\

if db_user_name is not None:
    if user_name == db_user_name:
        print(msg + 'names is equal')

    else:
        print(msg + 'names are NOT equal')
else:
    print(f'no such ID:{user_id}')


# 4
# PUT - test a post of an existing user to update his name in the DB

put_res = requests.put(url, json=data)
userName = ''
if put_res.status_code == 200:
    db_user_name = put_res.json()['user_updated']

    msg = f'user updated successfully\n\n' \
          f'this is the json output:\n{put_res.json()}'
    print(msg)

elif put_res.status_code in error_codes:
    reason = put_res.json()['reason']
    msg = f'PUT failed with reason: {reason} \n\n' \
          f'this is the json output:\n{put_res.json()}'
    print(msg)

else:
    print(f'PUT failed with status code {put_res.status_code}')


# DELETE - test if the DELETE request delete the user from the DB by the given ID


del_rest = requests.delete(url)
user_id = 0
msg = ''
if del_rest.status_code == 200:
    user_id = del_rest.json()['user_deleted']
    msg = f'user ID: {user_id} deleted successfully \n\n' \
          f'this is the json output:\n{del_rest.json()}'
    print(msg)

elif del_rest.status_code == 500:
    reason = del_rest.json()['reason']
    msg = f'DELETE failed with reason: {reason} \n\n' \
          f'this is the json output:\n{del_rest.json()}'
    print(msg)
else:
    print(f'DELETE failed with status code {del_rest.status_code}')






