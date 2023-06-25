import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


def valve_behaviour(id,start,end,client):
    df = client.time_series.data.retrieve(id=id,start=start,end=end).to_pandas()
    df.columns = ['Prcent_opening']
    df['opening_cm'] = (df['Prcent_opening']/100)
    df['position_change'] = df['opening_cm'].diff()
    df = df[1:]
    df['abs_position_change'] = np.abs(df['position_change'].values)
    df['traveled_in_total'] = df['abs_position_change'].cumsum()
    df.index = (df.index.view(np.int64)-df.index.view(np.int64)[0])/(1e9*60*60)
    #df['traveled_in_total'].plot()
    return df['traveled_in_total']

def valve_diagnostic(id,client):
    dtn = datetime.now()
    start = datetime(dtn.year,dtn.month,dtn.day)

    plt.figure(figsize=(10,10))
    for i in range(10,31):
        values = valve_behaviour(id,start-timedelta(days=i+1),start-timedelta(days=i),client)
        color = 'red'
        if(start-timedelta(days=i+1)>=datetime(2023,6,4)):
            color = 'blue'
        this_label = str((start-timedelta(days=i+1)).month)+'/'+str((start-timedelta(days=i+1)).day)
        plt.plot(values,color=color,label=this_label)
    plt.legend()
    plt.show()