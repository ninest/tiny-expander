from flask import Flask, Response
import requests

app = Flask(__name__)


@app.route('/<path:url>')
def expand(url):
  session = requests.Session()
  url = url if '://' in url else f'http://{url}'
  resp = session.head(url, allow_redirects=True)
  return Response(resp.url, mimetype='text/plain')


if __name__ == '__main__':
  app.run()
