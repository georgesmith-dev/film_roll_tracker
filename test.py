# file to test routes are working
import requests


def valid_post_new_roll(base_url):
    "valid post new roll request"
    new_roll = {
        "stock": "portra",
        "exposures": 36,
        "iso": 400,
        "developed": False,
        "camera_used": "leica m2",
    }
    try:
        new_roll_response = requests.post(f"{base_url}/rolls", json=new_roll)
        print(new_roll_response.status_code)
        print(new_roll_response.json())
    except requests.RequestException as e:
        print(f"An unexpected error has occured: {e}")


def invalid_post_new_roll(base_url):
    "ivalid post new roll request"
    new_roll = {
        "stock": "portra",
        "exposures": "36",
        "iso": 1600,
        "developed": False,
        "camera_used": "leica m2",
    }
    try:
        new_roll_response = requests.post(f"{base_url}/rolls", json=new_roll)
        print(new_roll_response.status_code)
        print(new_roll_response.json())
    except requests.RequestException as e:
        print(f"An unexpected error has occured: {e}")


def get_all_rolls(base_url):
    try:
        all_rolls_response = requests.get(f"{base_url}/rolls/all")
        print(all_rolls_response.status_code)
        print(all_rolls_response.json())
    except requests.RequestException as e:
        print(f"An unexpected error has occured: {e}")


if __name__ == "__main__":
    valid_post_new_roll("http://127.0.0.1:8000/")
    invalid_post_new_roll("http://127.0.0.1:8000/")
    get_all_rolls("http://127.0.0.1:8000/")
