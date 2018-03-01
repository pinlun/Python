# bokeh serve --show barchart
# library
from os.path import dirname, join

import pandas as pd
import numpy as np

from bokeh.palettes import viridis
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.models.widgets import PreText, Select
from bokeh.layouts import row, column
from bokeh.io import curdoc

# function
# 將是字串的欄位轉為為數值
def depercent(x):
    a = x.replace('%','')
    a = int(float(a))*0.01
    return a

# 將資料進行計算轉換為視覺化的資料
def groupmean(data, col):
    item = np.unique(data.loc[:, col])
    colors = viridis(len(item))
    a = []
    for i in item:
        tmp = data[data[col] == i]
        a.append(np.mean(tmp["Yield"]))
    dd = ColumnDataSource(data=pd.DataFrame({col:item, "Yield":a, "colors":colors}))
    dd.data[col] = dd.data[col].astype(str)
    dd.data['Yield'] = dd.data['Yield'].astype('float64')
    return dd

# 畫圖
def make_plot(source, col):
    #tools = 'pan,wheel_zoom,xbox_select,reset'
    hover = HoverTool(tooltips=[
        (col, "@"+col),
        ("Yield", "@Yield")
        ])
    plot = figure(plot_width=800, tools=[hover])
    plot.title.text = 'Average of Yield for '+col
    plot.vbar(x='index', top='Yield', source=source, width=0.9, bottom=0, legend=col, color='colors')
    plot.y_range.start = 0
    return plot

# 顯示敘述統計
def update_stats(data):
    #stats.text = str(data.describe())
    stats.text = str(data)

# 當選項改變則做更新
def update(attrname, old, new):
    col = dim.value
    src = groupmean(data, col)
    update_stats(src.to_df())
    plot.title.text = 'Average of Yield for '+col
    source.data.update(src.data)
    newfig = make_plot(src, col)
    layout.children[0] = newfig
   
# widges
# 選項欄位設定
default_sel = ['Department', 'Productline', 'ProductType']
dim = Select(value='Department', title='Dim', options=default_sel)
stats = PreText(text='', width=500)

# input
# 讀取資料並執行畫圖
datadir = join(dirname(__file__), 'department.csv')
data = pd.read_csv(datadir)
data['Yield'] =  [depercent(i) for i in data.loc[:, 'Yield']]
col = 'Department'
source = groupmean(data, col)
plot = make_plot(source, col)

# initialize
# 初始化連帶的選項
dim.on_change('value', update)

# set up layout
# 畫布設定
widgets = column(dim, stats)
layout = row(plot, widgets)

curdoc().add_root(layout)
curdoc().title = "SPC"
