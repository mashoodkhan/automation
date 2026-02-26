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

