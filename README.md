# Analyzing How the Economic Factors could impact the Performance of Countries in the Summer Olympic Games

In our final project, we are interested in analyze how different economic factors could impact the performance of countries when they participate in the Summer Olympic Games. We have counted the total events in which each country has finished at the Top 15 at each Olympic Game since 1992. A country with a good performance, in our analysis, is a country that has finished within the first 15 places.

## Reason we chose this topic:

The team is interested in economics and sports

## Questions we hope to answer with the data:

- Does a countries HDI, annual GDP or total population contribute to a countries performance at the olympics?
- How are countries distributed depending on their economic factors and performance at the Olympics? Is there some natural clustering?

## Description of source of data:

Economic Indicators will be draw from the [**World Bank Data Catalog**](https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators) that has around 1453 indicators compiled from official sources around the world (204 countries are considered). And from [**United Nations**](http://hdr.undp.org/en/indicators/137506#), that is the *Human Development Index(HDI)*, which "measures average achievement in three basic dimensions of human development: long and healthy life, knowledge and decent standard of living. The data sets are in `csv` format and an initially exploration is made in `Python-Pandas Library`. The jupyter notebook is found [here](https://github.com/JoeAB3/Group5Capstone_Project/tree/Leidy_dbpart/CodeInJupyter/).

For the Olympic data various data sources were identified for this data.  We identified all the competiting countires in each Summer Olympic games.  Another data source found the placing  for each olympic event.  An additional data set was pulled in to find how many events were participated in.  All these data were used for the primary Olympic data set. The cleaning was as well made in `Python` and the code to do it is in [here](https://github.com/JoeAB3/Group5Capstone_Project/tree/Leidy_dbpart/PythonScripts).

## Communication Protocols:

Slack group containing all group members
Team meetings during scheduled class hours on Monday and Wednesday
Additional team meetings twice a week on zoom
Individual GitHub branch for each team member.

## 1. Data Exploration:

Because the HDI has been only reported since 1990, we are considered only the frame of time: 1990-2019. The data was explored so we can keep only the indicators that really could have an impact into the Olympic performance and that does not clutter the information we want to obtain.

### Scatter matrix between Indicators:

To determine if there are indicators that are highly correlated between them, we perform a scattermatrix between the economic indicators and in our further analysis only considered indicators that are not correlated. Figure 1 shows the scattermatrix, where it is possible to see how `GDP` and `GNI` as well as `HDI` and `HDI Rank` are higly correlated

![scatter](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/Leidy_dbpart/ImagesReadme/scatterMatrix.png)
Figure 1. Scattermatrix of all indicators

### Economic Indicators per Olympic Years:

We want to see how the economic factors have varied along the years for each country, so we plot each indicator as a variable of the olympic years per country. We use `hvplot` library to make these plots and although in Pandas, the country can be chosen from a drop-down list bottom, it still is not possible in the python script. Figure 2 shows how the plot looks for a specific country.

![econo](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/Leidy_dbpart/ImagesReadme/Indicators_OYears.png)
Figure 2. Economic Indicators vs. Olympic Year

### Olympic Performance per Country

We also want to check how the countries perform at olympic games along the years. Figure 3 is an example of the histogram that we made to show how is the participation of each country.

![olymps](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/Leidy_dbpart/ImagesReadme/Top15_OYear.png)
Figure 3. Top15 Countries vs. Olympic Year

## 2. Machine Learning:

In order to answer the second question of our project, we want to apply an unsupervised machine learning algorithm, so we can categorized countries into groups without having any previous information about their membership. We have used `k-means` and the `Elbow Curve` Method for estimating a possible number of groups.  An initial exploration of this analysis is in jupyter notebook in [here](https://github.com/JoeAB3/Group5Capstone_Project/blob/Leidy_dbpart/CodeInJupyter/Analysis_KmeansPlots.ipynb)

### Description of preliminary data preprocessing: 

We are going to apply `k-means` in a dataset with 4 indicators: `GDP`, `HDI`, `Population`, `Top15` for each country and each Olympic Game.  Because there are multiple values for the same parameters (since we are considering 7 olympic games), we are going to consider an analyis per Olympic Game. This means, will have a clustering of the countries per each Olympic year.

### Description of preliminary feature engineering:

Because we have several economic factors that could be related, we calculate the correlation between these factors. This was carried out by using the scatter matrix that is shown in Figure 1. After this process we keep the 4 factors/indicators previously listed.

### Explanation of model choice, including limitations and benefits

Because we do not have any priori information about how the countries could be categorized depending on how they perform economically and at the Olympic Games, we want to explore if there is an actual separation or relationship among them.  In this way, we choose the widely known `K-means` algorithm. The benefit of using k-means is that is simple to implement, fast, and guarantees convergence. However, its limitation is that we need to assume prior information about the data, such the number of clusters (`k`). 
 
## 3. Database:

Due to the nature of our data, we use a PostgreSQL database to save three tables: `Indicators`, `Olympics`, and `DataAnalysis`. Based on the two first tables, we create the third one with the economic indicators of our interest and the information about the Olympic Games. The Python sripts for the data exploration and analysis have code that fully integrate the database. The details are explained further.

### Database stores static data for use during the project:

The original raw data is access through API call from our application to the corresponding websites. After a cleaning process, the two tables are writen to `PostgreSQL` and from them another table is generated to be used in the Machine Learning Analysis. In the [PythonScripts] () folder there are the scripts that load the tables from internet and perform the initial cleaning for saving the tables into the database. 

### Database interfaces with the project in some format:

An initial API call is made from our Python script to load the original `csv` files that we are using in this project. Below it is an example:

```Python
#---- Reading World Bank Indicators 
url = 'https://github.com/LeidyDoradoM/mockup_finalProject/blob/myfirstbranch/Resources/WDIData.csv?raw=true'
indicators_df = pd.read_csv(url)
indicators_df
```
### Includes at least two tables: 

Below there is the `ERD` Diagram for our database:

![ERD](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/Leidy_dbpart/ImagesReadme/QuickDBD-export.png)

Figure 4. ERD for OlympicAnalysis Database.

### Includes at least one join using the database language:

The economic indicators and the olympic performance tables are joined using `sql` language from python as it is shown below:

```python
data = pd.read_sql_query("""SELECT
                            ind."Year", ind."CountryCode", ind."GDPCapita", ind."GNICapita", ind."Population", ind."HDI", ind."HDIRank",
                            oly."Top15", oly."Perc", oly."Total"
                            FROM "Indicators" AS ind 
                            INNER JOIN "Olympics" AS oly 
                            ON (ind."CountryCode" = oly."CountryCode" AND ind."Year" = oly."Year");""",
                         engine)
```
### Includes at least one connection string:

Each one of the tables are writen into the database using a connection strig as it is shown in the below piece of code:

```python
db_string = f"postgresql://postgres:{db_password}@127.0.0.1:5432/OlympicAnalysis_FP"
    #Create the database engine
    engine = create_engine(db_string) 
    ## Add olympics_df to a SQL db
    olympic_df.to_sql(name = 'Olympics', con = engine, if_exists = 'replace', index = False) 
    # Add primary keys
    olympic_df.to_sql(con=engine, name='Olympics', if_exists='replace', index=False)   
    with engine.connect() as con:
        con.execute('ALTER TABLE "Olympics" ADD PRIMARY KEY ("CountryCode","Year");')
```

## 4. Presentation
Link to Google Slides of presentation is [here](https://docs.google.com/presentation/d/1uGkUmyf4gTuGKR7ov_M5aNJdvH7qaN4pgnWGX73oN0E/edit?usp=sharing).

## 5. Dashboard

We will have two dashboards to display the findings of our project.  The **Data Exploration** dashboard will display the scatter matrix to illustrate how we chose our indicators. The dashboard will also show the plots for the economic indicators by year. These plots will be interactive, as the desire is to have the user be able to filter them by country. Lastly, the histogram showing a countries performance by olympic game will be used. This will also be filtered by country.  This dashboard will be built in `Tableau`.

### Report from the machine learning task:

A second dashboard built in `Flask` and `html` template will present the findings from our machine learning analysis. The `app.py`, `html` and `css` files are in the *PythonScripts* folder in [here](https://github.com/JoeAB3/Group5Capstone_Project/tree/main/PythonScripts). The `app.py` [script](https://github.com/JoeAB3/Group5Capstone_Project/blob/main/PythonScripts/app.py) manages the connection to a our local Postgres database, and load the **Analysis** table that we use as input for our [Unsupervised Learning model](https://github.com/JoeAB3/Group5Capstone_Project/blob/main/PythonScripts/clusteringData.py). This function will return two plots that show how the countries are distributed along the economic indicators and olympic performance that we are considering in our analysis. The `kmeans` clustering is performed for each Olympic year as we have described previously.  Figure 5 shows a screenshot of how the dashboard looks when the user visits it for the first time.

![dashboard](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/Leidy_dbpart/ImagesReadme/OverviewDashboard.png)
Figure 5. An overview of the dashboard created for showing UML results.

**The dashboard has an interactive element** that is a `selector` input with a `submit` button. These two elements jointly allow the user to choose what Olympic year wants to see. Figure 6 shows how these two elements are displayed in the dashboard page. The `html` [template](https://github.com/JoeAB3/Group5Capstone_Project/tree/Leidy_dbpart/PythonScripts/templates/index.html) and the `css` [file](https://github.com/JoeAB3/Group5Capstone_Project/tree/Leidy_dbpart/PythonScripts/static/assets/css/custom.css) that allows the user this interaction are upload.

![dashboard1](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/Leidy_dbpart/ImagesReadme/Dashboard_Interaction.png)
Figure 6. The dashboard with the interactive element.

After the `submit` button is hit, a 3-d scatterplot and a world map are displayed as it is shown in Figure 7. 

![dashboard2](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/Leidy_dbpart/ImagesReadme/DashboardwResults.png)
Figure 7. The dashboard displaying the results of the *UML*.

The scatterplot as well as the world map allow the user some interaction, as they allow the display of the country information as the data points (in the scatterplot) or the country (in the world map) are hovering in.

![dashboard3](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/Leidy_dbpart/ImagesReadme/ScatterplotDashboard.png)
![dashboard4](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/Leidy_dbpart/ImagesReadme/worldMapDashboard.png)
Figure 8. Clustering of countries shown in different colors in the scatterplot and world map.