import requests

url = "http://localhost:5000/api"

req = requests.post(url, json={
    "fixed-acidity": 1.0, 
    "volatile-acidity": 1.0,
    "citric-acid": 1.0,
    "residual-sugar": 1.0,
    "chlorides": 1.0,
    "free-sulfur-dioxide": 1.0,
    "total-sulfur-dioxide": 1.0,
    "density": 1.0,
    "ph": 1.0,
    "sulphates": 1.0,
    "alcohol": 1.0,
})

print(req.json())