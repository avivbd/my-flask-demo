from flask import Flask, render_template, request, redirect
import requests 

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

#a comment

raw_req = requests.get('https://www.quandl.com/api/v1/datasets/WIKI/aapl')


@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')
