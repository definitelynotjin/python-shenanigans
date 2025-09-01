import requests
import json

url = f"http://10.14.23.185:90/api_jsonrpc.php"
username = "nocpln"
password = "nocpln123"

try:
    payload1 = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {"user": username, "password": password},
        "id": 1,
    }
    response1 = requests.post(url, json=payload1, timeout=10)
    data1 = response1.json()
    print(data1)
    token = data1["result"]

    payload2 = {
        "jsonrpc": "2.0",
        "method": "hostgroup.get",
        "params": {"output": "extend", "sortfield": "name"},
        "id": 1,
        "auth": token,
    }

    response2 = requests.post(url, json=payload2, timeout=10)
    data2 = response2.json()
    print(data2)

    json_string = json.dumps(data2["result"], indent=4)

    with open("output.json", "w") as json_file:
        json_file.write(json_string)

except requests.exceptions.RequestException as e:
    print(f"error: {e}")
