import pytest
import requests
import json
from jsonschema import validate

@pytest.mark.api
def test_login_page():
    res = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities")
    json_data = res.json()

    with open(r"C:\Users\mashood.khan_hrsoft\PycharmProjects\automation\data\activities_response.json","r") as f:
        exp =json.loads(f.read())

    for a,e in zip(json_data,exp):
        a.pop("dueDate",None)
        e.pop("dueDate",None)

    print("actual json ",json_data)
    print("actual json ", json_data)
    assert json_data == exp
    assert res.status_code == 200

@pytest.mark.api
def test_post_login():
    headers = {"Content-Type": "application/json"}
    with open(r"C:\Users\mashood.khan_hrsoft\PycharmProjects\automation\data\activities_response.json","r") as f:
        body = json.loads(f.read())
   #res =  requests.post("https://fakerestapi.azurewebsites.net/api/v1/Authors",headers=headers,json=body)