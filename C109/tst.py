import pandas as pd
import plotly.figure_factory as ff
import statistics as st
df= pd.read_csv('data.csv')
height = df['Height(Inches)'].tolist()
mean = st.mean(height)
std = st.stdev(height)
tsstd = mean-3*std
testd = mean+3*std
tstd = []
for a in height:
    if a>tsstd and a<testd:
        tstd.append(a)
tp = (len(tstd)/len(height))*100
print(str(tp)+'%')