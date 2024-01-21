# Guide

1. Create your virtual enviroment in the same directory with this file
2. Activate your virtual environment
3. Run pip install -r requirements.txt
4. Run python3 manage.py makemigrations
5. Run python3 manage.py migrate


### Code to access the AI back end hosted in AWS

Make sure a file called oneMedi.jpeg is present
```
import requests
import base64

ip="34.201.114.120"
image_path='oneMedi.jpeg'
with open(image_path, "rb") as image_file:
    base64_image= base64.b64encode(image_file.read()).decode('utf-8')
 
# Send a POST request to the Flask server
print("Sending request")
response = requests.post(f'http://{ip}:8001/process', json={"image": base64_image,"prompt":"Just give me the text on the image, nothing else. Give me your best guess if you cannot read fully."})
# print(response.json())
message=response.json()["message"]
print(message)
```

Add the message to the description of the medicine
