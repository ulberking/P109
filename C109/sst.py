import pandas as pd
import plotly.figure_factory as ff
import statistics as st
df = pd.read_csv('data.csv')
height = df['Height(Inches)'].tolist()
mean = st.mean(height)
std = st.stdev(height)
ssstd = mean-(2*std)
sestd = mean+(2*std)
sstd = []
for a in height:
    if a> ssstd and a< sestd:
        sstd.append(a)
sp = (len(sstd)/len(height))*100
print(str(sp)+'%')