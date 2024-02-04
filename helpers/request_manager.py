import requests

def send(): 
    url = "placeholder"
    response = requests.get(url)

    if response.status_code == 200:
        print("Success")
        return response.json()

    else:
        print("Error")

