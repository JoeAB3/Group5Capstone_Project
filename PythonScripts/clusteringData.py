# Import modules 
import pandas as pd
import numpy as np
import psycopg2
from sklearn.cluster import KMeans  
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import plotly.express as px

def Kmean_Olympics(analysis_table,year):
    df_data = analysis_table.dropna()
    # Clustering by years
    df = df_data[df_data.Year == year]
    X = df.drop(['Year','CountryCode','GNICapita','HDIRank'], axis=1)
    X = X.dropna()
    X_scaled = MinMaxScaler().fit_transform(X)
    model = KMeans(n_clusters=3, random_state=0)
    # Fitting model
    model.fit(X_scaled)
    # Get the predictions
    predictions = model.predict(X_scaled)
    df['cluster'] = model.labels_
    fig = px.scatter_3d(df, x="GDPCapita", y="HDI",z="Top15", color="cluster",symbol="cluster",
                        hover_name="CountryCode", width=800)
    fig.update_layout(legend=dict(x=0,y=1))
    print(f"fig type: {type(fig)}")
    #fig.write_html('clustering1992.html')
    return fig
