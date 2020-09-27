# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 09:20:59 2020

@author: ASHAAB
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import plotly.graph_objects as go
st.title('Covid 19 Dashboard')
st.sidebar.title('Covid 19 Dashboard using Different Plotly Plots')
st.markdown('This application is a Covid 19 Dashboard made using Streamlit to analyse Covid 19 using different interactive plots')
st.sidebar.markdown('Choose the Plot')

url=('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')
latest_data = pd.read_csv(url)
data = pd.read_csv("C:/Users/ASHAAB/Desktop/full_grouped.csv")
data_INDIA = data[data['Country/Region']=='India']
data_INDIA = data_INDIA[data_INDIA.Confirmed > 0]
worldometer = pd.read_csv("C:/Users/ASHAAB/Desktop/worldometer_data.csv")

st.sidebar.subheader('Choropleth Map')
st.sidebar.markdown('Choropleth Map of World, Asia and Europe')
select = st.sidebar.selectbox('Choose Choropleth Map',['World','Asia','Europe'],key='1')

if not st.sidebar.checkbox("Hide Map",True):
    if select == "World":
       fig = px.choropleth(latest_data,locations='Country',locationmode='country names',color='Confirmed',animation_frame='Date')
       fig.update_layout(title='Choropleth Map of Confirmed Cases - World ',template="plotly_dark")
       st.plotly_chart(fig) 
    elif select == "Asia":
       fig = px.choropleth(latest_data,locations='Country',locationmode='country names',color='Confirmed',animation_frame='Date',scope='asia')
       fig.update_layout(title='Choropleth Map of Confirmed Cases - Asia',template="plotly_dark")
       st.plotly_chart(fig) 
    else:
        fig = px.choropleth(latest_data,locations='Country',locationmode='country names',color='Confirmed',animation_frame='Date',scope='europe')
        fig.update_layout(title='Choropleth Map of Confirmed Cases - Europe',template="plotly_dark")
        st.plotly_chart(fig)
    
st.sidebar.subheader('Line Chart India - Infection Rate, Death Rate and Recovery Rate in Lockdown')
st.sidebar.markdown("Phase 1: 25 March 2020 – 14 April 2020, Phase 2: 15 April 2020 – 3 May 2020, Phase 3: 4 May 2020 – 17 May 2020, Phase 4: 18 May 2020 – 31 May 2020")
select = st.sidebar.selectbox('Choose Line Chart',['Infection Rate','Death Rate','Recovery Rate'],key='2')    
 
India_lockdown_1 = '2020-03-25'
India_lockdown_2 = '2020-04-15'
India_lockdown_3 = '2020-05-04'
India_lockdown_4 = '2020-05-18'


if not st.sidebar.checkbox("Hide Line Chart",True):
    if select == "Infection Rate":
      fig = px.line(data_INDIA,x='Date',y = 'New cases',title='Lockdown Phases - Infection Rate')
      fig.add_shape(dict(type='line',
                   x0=India_lockdown_1,
                   y0=0,
                   x1=India_lockdown_1,
                   y1=data_INDIA['New cases'].max(),
                   line = dict(color='red',dash="dashdot")
                   ))
      fig.add_annotation(dict(
                   x = India_lockdown_1,
                   y = data_INDIA['New cases'].max(),
                   text = 'Phase 1')
                   )
      fig.add_shape(dict(type='line',
                   x0=India_lockdown_2,
                   y0=0,
                   x1=India_lockdown_2,
                   y1=data_INDIA['New cases'].max(),
                   line = dict(color='blue',dash="dashdot")
                   ))
      fig.add_annotation(dict(
                   x = India_lockdown_2,
                   y = data_INDIA['New cases'].max(),
                   text = 'Phase 2')
                   )
      fig.add_shape(dict(type='line',
                   x0=India_lockdown_3,
                   y0=0,
                   x1=India_lockdown_3,
                   y1=data_INDIA['New cases'].max(),
                   line = dict(color='yellow',dash="dashdot")
                   ))
      fig.add_annotation(dict(
                   x = India_lockdown_3,
                   y = data_INDIA['New cases'].max(),
                   text = 'Phase 3')
                   )
      fig.add_shape(dict(type='line',
                   x0=India_lockdown_4,
                   y0=0,
                   x1=India_lockdown_4,
                   y1=data_INDIA['New cases'].max(),
                   line = dict(color='green',dash="dashdot")
                   ))
      fig.add_annotation(dict(
                   x = India_lockdown_4,
                   y = data_INDIA['New cases'].max(),
                   text = 'Phase 4')
                   )
      st.plotly_chart(fig)
      
    elif select == "Death Rate":
       fig = px.line(data_INDIA,x='Date',y = 'New deaths',title='Lockdown Phases - Death Rate')
       fig.add_shape(dict(type='line',
                   x0=India_lockdown_1,
                   y0=0,
                   x1=India_lockdown_1,
                   y1=data_INDIA['New deaths'].max(),
                   line = dict(color='red',dash="dashdot")
                   ))
       fig.add_annotation(dict(
                   x = India_lockdown_1,
                   y = data_INDIA['New deaths'].max(),
                   text = 'Phase 1')
                   )
       fig.add_shape(dict(type='line',
                   x0=India_lockdown_2,
                   y0=0,
                   x1=India_lockdown_2,
                   y1=data_INDIA['New deaths'].max(),
                   line = dict(color='blue',dash="dashdot")
                   ))
       fig.add_annotation(dict(
                   x = India_lockdown_2,
                   y = data_INDIA['New deaths'].max(),
                   text = 'Phase 2')
                   )
       fig.add_shape(dict(type='line',
                   x0=India_lockdown_3,
                   y0=0,
                   x1=India_lockdown_3,
                   y1=data_INDIA['New deaths'].max(),
                   line = dict(color='yellow',dash="dashdot")
                   ))
       fig.add_annotation(dict(
                   x = India_lockdown_3,
                   y = data_INDIA['New deaths'].max(),
                   text = 'Phase 3')
                   )
       fig.add_shape(dict(type='line',
                   x0=India_lockdown_4,
                   y0=0,
                   x1=India_lockdown_4,
                   y1=data_INDIA['New deaths'].max(),
                   line = dict(color='green',dash="dashdot")
                   ))
       fig.add_annotation(dict(
                   x = India_lockdown_4,
                   y = data_INDIA['New deaths'].max(),
                   text = 'Phase 4')
                   )
       st.plotly_chart(fig) 
       
    else:
        fig = px.line(data_INDIA,x='Date',y = 'New recovered',title='Lockdown Phases - Recovery Rate')
        fig.add_shape(dict(type='line',
                   x0=India_lockdown_1,
                   y0=0,
                   x1=India_lockdown_1,
                   y1=data_INDIA['New recovered'].max(),
                   line = dict(color='red',dash="dashdot")
                   ))
        fig.add_annotation(dict(
                   x = India_lockdown_1,
                   y = data_INDIA['New recovered'].max(),
                   text = 'Phase 1')
                   )
        fig.add_shape(dict(type='line',
                   x0=India_lockdown_2,
                   y0=0,
                   x1=India_lockdown_2,
                   y1=data_INDIA['New recovered'].max(),
                   line = dict(color='blue',dash="dashdot")
                   ))
        fig.add_annotation(dict(
                   x = India_lockdown_2,
                   y = data_INDIA['New recovered'].max(),
                   text = 'Phase 2')
                   )
        fig.add_shape(dict(type='line',
                   x0=India_lockdown_3,
                   y0=0,
                   x1=India_lockdown_3,
                   y1=data_INDIA['New recovered'].max(),
                   line = dict(color='yellow',dash="dashdot")
                   ))
        fig.add_annotation(dict(
                   x = India_lockdown_3,
                   y = data_INDIA['New recovered'].max(),
                   text = 'Phase 3')
                   )
        fig.add_shape(dict(type='line',
                   x0=India_lockdown_4,
                   y0=0,
                   x1=India_lockdown_4,
                   y1=data_INDIA['New recovered'].max(),
                   line = dict(color='green',dash="dashdot")
                   ))
        fig.add_annotation(dict(
                   x = India_lockdown_4,
                   y = data_INDIA['New recovered'].max(),
                   text = 'Phase 4')
                   )
        st.plotly_chart(fig)
        
st.sidebar.subheader('Scatter Plot')
st.sidebar.markdown('Scatter Plot of Confirmed v Active Cases and Deaths v Recovered of India ')
select = st.sidebar.selectbox('Choose Scatter Plot',['Confirmed v Active','Deaths v Recovered'],key='3')

if not st.sidebar.checkbox("Hide Scatter Plot",True):
    if select == "Confirmed v Active":
       fig = go.Figure(data=go.Scatter(x=data_INDIA['Confirmed'],y=data_INDIA['Active'],mode='markers',marker=dict(size=10,color=data_INDIA['New cases'],showscale=True),text=data_INDIA['Country/Region']))
       fig.update_layout(title='Scatter Plot for Confirmed v Active Cases',xaxis_title='Confirmed',yaxis_title='Active')
       st.plotly_chart(fig) 
    else:
        fig = go.Figure(data=go.Scatter(x=data_INDIA['Deaths'],y=data_INDIA['Recovered'],mode='markers',marker=dict(size=10,color=data_INDIA['New cases'],showscale=True),text=data_INDIA['Country/Region']))
        fig.update_layout(title='Scatter Plot for Deaths v Recovery',xaxis_title='Deaths',yaxis_title='Recovery')
        st.plotly_chart(fig) 
    
st.sidebar.subheader('Bar Chart')
st.sidebar.markdown('Bar Chart of Total Tests, Deaths/Million, Cases/Million,Tests/Million of 10 Most Affected Countries')
select = st.sidebar.selectbox('Choose Bar Chart',['Total Tests','Deaths/Million','Cases/Million','Tests/Million'],key='4')
 
if not st.sidebar.checkbox("Hide Bar Chart",True):
    if select == "Total Tests":
       fig = px.bar(worldometer.head(10), y='TotalTests',x='Country/Region',color='WHO Region',height=400)
       fig.update_layout(title='Comparison of Total Tests of 10 Most Affected Countries',xaxis_title='Country',yaxis_title='Total Tests',template="plotly_dark")
       st.plotly_chart(fig) 
    elif select =="Deaths/Million":
       fig = px.bar(worldometer.head(10), y='Deaths/1M pop',x='Country/Region',color='WHO Region',height=400)
       fig.update_layout(title='Comparison of Deaths/Million of 10 Most Affected Countries',xaxis_title='Country',yaxis_title='Deaths/Million',template="plotly_dark")  
       st.plotly_chart(fig) 
    elif select =="Cases/Million":
       fig = px.bar(worldometer.head(10), y='Tot Cases/1M pop',x='Country/Region',color='WHO Region',height=400)
       fig.update_layout(title='Comparison of Cases/Million of 10 Most Affected Countries',xaxis_title='Country',yaxis_title='Cases/Million',template="plotly_dark")
       st.plotly_chart(fig)
    else:
       fig = px.bar(worldometer.head(10), y='Tests/1M pop',x='Country/Region',color='WHO Region',height=400)
       fig.update_layout(title='Comparison of Tests/Million of 10 Most Affected Countries',xaxis_title='Country',yaxis_title='Tests/Million',template="plotly_dark")
       st.plotly_chart(fig)
        
st.sidebar.subheader('Bubble Chart and Sunburst Chart')
st.sidebar.markdown('Bubble Chart of Total Cases v Total Deaths and Sunburst Chart for Active Cases')
select = st.sidebar.selectbox('Choose Chart',['Bubble Chart','Sunburst Chart'],key='5')

if not st.sidebar.checkbox("Hide Chart",True):
    if select == "Bubble Chart":
       fig = px.scatter(worldometer.head(50), x="TotalCases", y="TotalDeaths",size='Population',
	               color="Continent",
                 hover_name="Country/Region", log_x=True, size_max=60)
       fig.update_layout(title='Bubble Plot for Total Cases v Total Deaths of 50 Most Affected Countries',xaxis_title='Cases',yaxis_title='Deaths')
       st.plotly_chart(fig)
    else:
        fig = px.sunburst(worldometer.head(50),path=['Continent','Country/Region','WHO Region'],values='Population',
                  color='ActiveCases',
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(worldometer.head(50)['Serious,Critical'], weights=worldometer.head(50)['Population']))
        fig.update_layout(title='Sunburst Chart')
        st.plotly_chart(fig)
        

