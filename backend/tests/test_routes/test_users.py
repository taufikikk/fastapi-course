import json

def test_create_user(client):
    data = {"username":"testusername","email":"iniil@test.com","password":"325534"}
    response = client.post("/users/",json.dumps(data))
    assert response.status_code == 200 
    assert response.json()["email"] == "iniil@test.com"
    assert response.json()["is_active"] == True
    