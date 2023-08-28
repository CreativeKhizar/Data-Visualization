import pandas as pd

data={
    "Date" : ["14/03/2004","15/03/2004","16/03/2004","17/03/2004","18/03/2004"],
    "Time" : ["01:00:00","02:00:00","03:00:00","04:00:00","05:00:00"],
    "CO(GT)" : [2.8,2.5,3.0,2.2,2.7]
}

df=pd.DataFrame(data)
start_date="14/03/2004"
end_date="16/03/2004"
min_co_level=2.5

df['Date']=pd.to_datetime(df['Date'],format="%d/%m/%Y")

filtered_df=df[(df['Date']>=start_date) & (df['Date']<=end_date)&(df['CO(GT)']>=min_co_level)]

print(filtered_df)


import pandas as pd
import plotly.express as px

data={
    "Region" : ["Region_A","Region_B","Region_C"],
    "CO(GT)" : [2.4,3.2,1.5],
    "NO(GT)" : [25,30,22],
    "PTO8.S5(03)" : [300,350,180]
}
df=pd.DataFrame(data)
fig=px.treemap(df,path=["Region"],values="CO(GT)",title="CO(GT) Level by Region")
fig.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Date" : ["2023-01-01","2023-01-02","2023-01-03","2023-01-04","2023-01-05"],
    "CO(GT)" : [2.8,3.2,2.5,2.7,3.0]
}

df=pd.DataFrame(data)
df['Date']=pd.to_datetime(df['Date'])
plt.figure(figsize=(10,6))
sns.set_theme(style="darkgrid")
sns.lineplot(x="Date",y="CO(GT)",data=df,marker="o")
plt.title("CO(GT) Trend Over Time")
plt.xlabel("Date")
plt.ylabel("CO(GT) Level")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import pandas as pd

data = {
    "Date" : ["2023-01-01","2023-01-02","2023-01-03","2023-01-04","2023-01-05"],
    "CO(GT)" : [2.8,3.2,2.5,2.7,3.0],
    "NO2(GT)" : [25,30,22,28,32],
    "PTO8.S5(O3)" : [300,350,280,320,360]
}

df=pd.DataFrame(data)

co_mean=df['CO(GT)'].mean()
no2_mean=df['NO2(GT)'].mean()
o3_mean=df['PTO8.S5(O3)'].mean()
report="Air Quality Report\n"
report+="----------------------------------\n"
report+=f"Average CO(GT) Level : {co_mean : .2f}\n"
report+=f"Average NO2(GT) Level : {no2_mean : .2f}\n"
report+=f"Average O3 Level : {o3_mean : .2f}\n"
print(report)
