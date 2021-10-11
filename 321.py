import plotly.figure_factory as ff
import statistics
import random 
import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv("asds.csv")
data=df["temp"].tolist()
populationMean=statistics.mean(data)
fig=ff.create_distplot([data],["temp"],show_hist=False)
# fig.show()
standarndeviation=statistics.stdev(data)
print("standarndeviation=",standarndeviation)
print("populationMean=",populationMean)

dataSets=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataSets.append(value)

Mean=statistics.mean(dataSets)
standarndeviation=statistics.stdev(dataSets)

print("Mean=",Mean)
print("standarndeviation=",standarndeviation)

def random_setOfMean(counter):
    dataSets=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataSets.append(value)
    
    Mean=statistics.mean(dataSets)
    return Mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

def setup():
    Meanlist=[]
    for i in range(0,1000):
        setOfMean=random_setOfMean(100)
        Meanlist.append(setOfMean)
    
    show_fig(Meanlist)



setup()