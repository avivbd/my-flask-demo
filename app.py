from flask import Flask, render_template, request, redirect
import numpy as np
from bokeh.plotting import figure, output_file, save 


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
          return redirect('/plot') 

@app.route('/plot',methods = ['GET','POST'])
def plot():          
          #app.vars['stock'] = request.form['stock_name'] 
          # prepare some data
          N = 4000
          x = np.random.random(size=N) * 100
          y = np.random.random(size=N) * 100
          radii = np.random.random(size=N) * 1.5
          colors = [
          "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
          ]
          # output to static HTML file (with CDN resources)
          output_file("templates/plot_file.html", title="color_scatter.py example", mode="cdn")
          TOOLS="resize,crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
          # create a new plot with the tools above, and explicit ranges
          p = figure(tools=TOOLS, x_range=(0,100), y_range=(0,100))
          # add a circle renderer with vectorized colors and sizes
          p.circle(x,y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)
          # show the results
          save(p)
          return render_template('plot_file.html') 
         



if __name__ == '__main__':
  app.run(host='104.131.171.187',debug = 'True')




















