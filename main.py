import os
from dotenv import load_dotenv
from fastapi import FastAPI, responses
import requests

app = FastAPI()
load_dotenv()

CLIENT_SECRET = os.environ["CLIENT_SECRET"] #load the client secret
CLIENT_ID = os.environ["CLIENT_ID"] #load the client_id

REDIRECT_URI = "http://localhost:8000/callback"
auth_url = f"https://auth.truelayer-sandbox.com/?response_type=code&client_id={CLIENT_ID}&scope=info%20accounts%20balance%20transactions%20offline_access&redirect_uri={REDIRECT_URI}&providers=uk-cs-mock"
@app.get("/", response_class=responses.HTMLResponse) #serve a button that sends user to the fetch the code
def home():
    return f""" <html>
    <a href= {auth_url}> <button>"Click To Connect"</button></a>
    </html>"""


@app.get("/callback")
def callback(code: str):
    token = requests.post(url = "https://auth.truelayer-sandbox.com/connect/token", data =
                          {
                              "grant_type":"authorization_code",
                              "client_id":CLIENT_ID,
                              "client_secret":CLIENT_SECRET,
                              "redirect_uri":REDIRECT_URI,
                              "code":code
                          }
                          )
    print(f"SECRET FUCKING TOKEN{token.json()}")
    return token.json()




