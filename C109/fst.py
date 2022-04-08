import pandas as pd
import plotly.figure_factory as ff
import statistics as st
df = pd.read_csv('data.csv')
height = df['Height(Inches)'].tolist()
mean = st.mean(height)
std = st.stdev(height)
fsstd = mean - std
festd = mean + std
fstd = []
for a in height:
    if a>fsstd and a<festd:
        fstd.append(a)
fp = (len(fstd)/len(height))*100
print(fp)
graph = ff.create_distplot([fstd],['height'],show_hist=False)
graph.show()