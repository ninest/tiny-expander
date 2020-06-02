from flask import Flask, Response
import requests

app = Flask(__name__)


@app.route('/api/<path:url>')
def expand(url):
  session = requests.Session()

  # add http if not there
  url = url if '://' in url else f'http://{url}'

  # follow any redirects
  resp = session.head(url, allow_redirects=True)

  return Response(resp.url, mimetype='text/plain')


@app.route('/ping')
def ping():
  return Response('PONG', mimetype='text/plain')


if __name__ == '__main__':
  app.run()
