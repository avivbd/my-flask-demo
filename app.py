from flask import Flask, render_template, request, redirect
import numpy as np
from bokeh.plotting import figure, output_file, save 
import simplejson as json
import requests 
import pandas as pd

app = Flask(__name__)

app.vars = {}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods = ['GET','POST'])
def index():
    if request.method == 'GET':
          return render_template('index2.html')
    else:
          app.vars['stock'] = request.form['stock_name']
          return redirect('/plot') 

@app.route('/plot',methods = ['GET','POST'])
def plot():          

          # get data from quandl 
          raw_req = requests.get('https://www.quandl.com/api/v1/datasets/WIKI/%s' % (app.vars['stock']))
          pdreq = pd.io.json.json_normalize(raw_req.json()) #get json object and normalize it

          #arrange in dataframe         
          df = pd.DataFrame(pdreq['data'][0], columns=pdreq['column_names'][0]) 
          df['Date'] = pd.to_datetime(df['Date']) #convert date to datetime
          
          #make a figure
          output_file("templates/plot_file.html", title="Stock price", mode="cdn")
          TOOLS="resize,crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
          p = figure(width=800, height=550, x_axis_type="datetime", tools = TOOLS)#
          p.title.text_font_size = "25px"
          p.title.text = "Price of stock: %s " % (app.vars['stock'])
          p.line(df['Date'], df['Close'], line_width=2, color='navy', legend='Closing price')

          #save figure to a html file and render it
          save(p)
          return render_template('plot_file.html') 
         



if __name__ == '__main__':
  app.run(host='104.131.171.187',debug = 'True')





