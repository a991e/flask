from flask import Flask
import requests
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/f/<path:url>')
def forward(url):
   if url.find('http:') != -1:
      url = url[0:6] + '/' + url[6:]
   elif url.find('https:') != -1:
      url = url[0:7] + '/' + url[7:]
   parsed_url = urlparse(url)
   referer = parsed_url.scheme + "://" + parsed_url.netloc
   headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Referer":referer,
   }
   try:
      response = requests.get(url,headers=headers)
   except Exception as e:
      return e
   return (response.content, response.status_code, response.headers.items())

if __name__ == '__main__':
   app.run(debug=True, port=os.getenv("PORT", default=5000))
