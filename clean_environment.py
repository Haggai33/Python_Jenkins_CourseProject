import requests

try:
    requests.get('http://127.0.0.1:5000/stop_server')

except requests.exceptions.RequestException as e:
    print(f'Rest server is NOT responding')

    try:
        requests.get('http://127.0.0.1:5001/stop_server')

    except requests.exceptions.RequestException as e:
        print(f'Web_app is NOT responding')

