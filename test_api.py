import requests
import json

def test_api_versions():
    base_url = "http://localhost:8000/api/"
    
    # Test v1 API
    print("Testing API v1...")
    response = requests.get(base_url + "v1/items/")
    print(f"Status code: {response.status_code}")
    if response.status_code == 200:
        print("Response data:")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Error response:", response.text)
    
    print("\n" + "-" * 50 + "\n")
    
    # Test v2 API
    print("Testing API v2...")
    response = requests.get(base_url + "v2/items/")
    print(f"Status code: {response.status_code}")
    if response.status_code == 200:
        print("Response data:")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Error response:", response.text)

if __name__ == "__main__":
    print("This script tests the API versioning implementation.")
    print("Before running this script, make sure the Django server is running with:")
    print("python manage.py runserver")
    print("\nThe script will make requests to both v1 and v2 of the API to verify versioning.")
    print("You should see different fields in the responses from each version.")
    print("\nNote: You need to have created some items in the database for this test to show meaningful results.")