import json, requests

def test_login_page():
    res = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities")
    json_data = res.json()

    file_path = "data/activities_response.json"
    with open(file_path, "r") as f:
        expected = json.load(f)

    for actual, exp in zip(json_data, expected):
        actual.pop("dueDate", None)
        exp.pop("dueDate", None)

    print("actual json", json_data)
    assert json_data == expected
    assert res.status_code == 200

# @pytest.mark.api
# def test_post_login():
#     headers = {"Content-Type": "application/json"}
#     with open(r"C:\Users\mashood.khan_hrsoft\PycharmProjects\automation\data\activities_response.json","r") as f:
#         body = json.loads(f.read())
#    #res =  requests.post("https://fakerestapi.azurewebsites.net/api/v1/Authors",headers=headers,json=body)