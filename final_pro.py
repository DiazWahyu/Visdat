# -*- coding: utf-8 -*-
"""final_pro.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xZoPzX2qeLww3dw5OHRxLL-i4D9xsG-o
"""

# import modules
import numpy as np
import pandas as pd
from bokeh.io import output_file, save, curdoc
from bokeh.plotting import figure, show
from bokeh.layouts import column, row
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import CDSView, ColumnDataSource, GroupFilter, Div, HoverTool

df = pd.read_csv("covid_19_indonesia_time_series_all.csv")
df.head()

# read data
Location = ['Jawa Barat','DKI Jakarta','Jawa Timur', 'Bali', 'Jawa Tengah']

df = pd.read_csv("covid_19_indonesia_time_series_all.csv", parse_dates=['Date'])
data = df[df.Location.isin(Location)] 
data.head()

# output to file
output_file('covid19.html',
             title = 'Visualisasi Data Statistik COVID-19')

# Create and configure the figure
con_fig = figure(x_axis_type='datetime',
                  plot_height=400, plot_width=1000,
                  title='Click Legend to HIDE Data',
                  x_axis_label='Date', y_axis_label='Total Cases')

dea_fig = figure(x_axis_type='datetime',
                  plot_height=400, plot_width=1000,
                  title='Click Legend to HIDE Data',
                  x_axis_label='Date', y_axis_label='Total Deaths')

rec_fig = figure(x_axis_type='datetime',
                  plot_height=400, plot_width=1000,
                  title='Click Legend to HIDE Data',
                  x_axis_label='Date', y_axis_label='Total Recovered')

# create a ColumnDataSource
covid_cds = ColumnDataSource(data)

# create views for 5 Country
ind_view = CDSView(source=covid_cds,
                  filters=[GroupFilter(column_name='Location', group='Jawa Barat')])

vie_view = CDSView(source=covid_cds,
                  filters=[GroupFilter(column_name='Location', group='DKI Jakarta')])

tha_view = CDSView(source=covid_cds,
                  filters=[GroupFilter(column_name='Location', group='Jawa Timur')])

phi_view = CDSView(source=covid_cds,
                  filters=[GroupFilter(column_name='Location', group='Bali')])

mal_view = CDSView(source=covid_cds,
                  filters=[GroupFilter(column_name='Location', group='Jawa Tengah')])

# format the tooltip
con_tooltips = [
            ('Location', '@Location'),
            ('Total Cases', '@Total Cases')
            ]

dea_tooltips = [
            ('Location', '@Location'),
            ('Total Deaths', '@New Total Deaths')
            ]

rec_tooltips = [
            ('Location', '@Location'),
            ('Total Recovered', '@New Total Recovered')
            ]

# format hover glyph
con_hover_glyph = con_fig.circle(x='Date', y='Total Cases', source=covid_cds,
                                 size=7, alpha=0,
                                 hover_fill_color='white', hover_alpha=0.5)

dea_hover_glyph = dea_fig.circle(x='Date', y='Total Deaths', source=covid_cds,
                                 size=7, alpha=0,
                                 hover_fill_color='white', hover_alpha=0.5)

rec_hover_glyph = rec_fig.circle(x='Date', y='Total Recovered', source=covid_cds,
                                 size=7, alpha=0,
                                 hover_fill_color='white', hover_alpha=0.5)

# add the HoverTool to the figure
con_fig.add_tools(HoverTool(tooltips=con_tooltips, renderers=[con_hover_glyph]))
dea_fig.add_tools(HoverTool(tooltips=dea_tooltips, renderers=[dea_hover_glyph]))
rec_fig.add_tools(HoverTool(tooltips=rec_tooltips, renderers=[rec_hover_glyph]))

# consolidate the common keyword arguments in dicts
common_circle = {
    'source': covid_cds,
    'size': 5,
    'alpha': 1,
    'muted_alpha': 0
}
common_Jawa_Barat = {
    'view': ind_view,
    'color': '#FC6E51',
    'legend_label': 'Jawa Barat'
}
common_Jakarta = {
    'view': vie_view,
    'color': '#370665',
    'legend_label': 'DKI Jakarta'
}
common_Jawa_Timur = {
    'view': tha_view,
    'color': '#35589A',
    'legend_label': 'Jawa Timur'
}
common_Bali = {
    'view': phi_view,
    'color': '#F14A16',
    'legend_label': 'Bali'
}
common_Jawa_Tengah = {
    'view': mal_view,
    'color': '#FC9918',
    'legend_label': 'Jawa Tengah'
}

# create the figures and draw the data
con_fig.circle(x='Date', y='Total Cases', **common_circle, **common_Jakarta)
con_fig.circle(x='Date', y='Total Cases', **common_circle, **common_Jawa_Barat)
con_fig.circle(x='Date', y='Total Cases', **common_circle, **common_Bali)
con_fig.circle(x='Date', y='Total Cases', **common_circle, **common_Jawa_Tengah)
con_fig.circle(x='Date', y='Total Cases', **common_circle, **common_Jawa_Timur)

dea_fig.circle(x='Date', y='Total Deaths', **common_circle, **common_Jakarta)
dea_fig.circle(x='Date', y='Total Deaths', **common_circle, **common_Jawa_Barat)
dea_fig.circle(x='Date', y='Total Deaths', **common_circle, **common_Bali)
dea_fig.circle(x='Date', y='Total Deaths', **common_circle, **common_Jawa_Tengah)
dea_fig.circle(x='Date', y='Total Deaths', **common_circle, **common_Jawa_Timur)

rec_fig.circle(x='Date', y='Total Recovered', **common_circle, **common_Jakarta)
rec_fig.circle(x='Date', y='Total Recovered', **common_circle, **common_Jawa_Barat)
rec_fig.circle(x='Date', y='Total Recovered', **common_circle, **common_Bali)
rec_fig.circle(x='Date', y='Total Recovered', **common_circle, **common_Jawa_Tengah)
rec_fig.circle(x='Date', y='Total Recovered', **common_circle, **common_Jawa_Timur
               )

# add interactivity to the legend
con_fig.legend.click_policy = 'mute'
dea_fig.legend.click_policy = 'mute'
rec_fig.legend.click_policy = 'mute'

# add a tittle for the entire visualization using Div
html = """<h3>Visualisasi Data Statistik COVID-19</h3>
Kelompok: Zhafier <br>
Kelas: IF-42-GAB04 <br>"""
sup_title = Div(text=html)

# Create three panels
con_panel = Panel(child=con_fig, title='Total Cases')
dea_panel = Panel(child=dea_fig, title='Total Deaths')
rec_panel = Panel(child=rec_fig, title='Total Recovered')

# Assign the panels to Tabs
tabs = Tabs(tabs=[con_panel, dea_panel, rec_panel])

# Visualize
layout = row(column(sup_title, tabs))
curdoc().add_root(layout)

# save to file
save(layout)