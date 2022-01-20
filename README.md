# Analyzing How the Economic Factors could impact the Performance of Countries in the Summer Olympic Games

In our final project, we are interested in analyze how different economic factors could impact the performance of countries when they participate in the Summer Olympic Games. We have counted the total events in which each country has finished at the Top 15 at each Olympic Game since 1992. A country with a good performance, in our analysis, is a country that has finished within the first 15 places.

## Reason we chose this topic:

The team is interested in economics and sports

## Questions we hope to answer with the data:

- Does a countries HDI, annual GDP or total population contribute to a countries performance at the olympics?
- How are countries distributed depending on their economic factors and performance at the Olympics? Is there some natural clustering?

## Description of source of data:

Economic Indicators will be draw from the [**World Bank Data Catalog**](https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators) that has around 1453 indicators compiled from official sources around the world (204 countries are considered). And from [**United Nations**](http://hdr.undp.org/en/indicators/137506#), that is the *Human Development Index(HDI)*, which "measures average achievement in three basic dimensions of human development: long and healthy life, knowledge and decent standard of living. The data sets are in `csv` format and an initially exploration is made in `Python-Pandas Library`. The jupyter notebook is found [here](https://github.com/JoeAB3/Group5Capstone_Project/tree/main/CodeInJupyter/).

For the Olympic data various data sources were identified for this data.  We identified all the competiting countires in each Summer Olympic games.  Another data source found the placing  for each olympic event.  An additional data set was pulled in to find how many events were participated in.  All these data were used for the primary Olympic data set. The cleaning was as well made in `Python` and the code to do it is in [here](https://github.com/JoeAB3/Group5Capstone_Project/tree/main/PythonScripts).

## Communication Protocols:

Slack group containing all group members
Team meetings during scheduled class hours on Monday and Wednesday
Additional team meetings twice a week on zoom
Individual GitHub branch for each team member.

## 1. Data Exploration:

Because the HDI has been only reported since 1990, we are considered only the frame of time: 1990-2019. The data was explored so we can keep only the indicators that really could have an impact into the Olympic performance and that does not clutter the information we want to obtain.

### Economic Indicators per Olympic Years:

We want to see how the economic factors have varied along the years for each country. Figure 2 shows scatterplots of the different socio-economic factors for the countries and for a specific Year.

![econo1](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/main/ImagesReadme/GDP.png)

![econo2](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/main/ImagesReadme/Population.png)

![econo3](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/main/ImagesReadme/HDI.png)

Figure 1. Economic Indicators vs. Olympic Year

### Olympic Performance per Country

We also want to check how the countries perform at olympic games along the years. Figure 3 shows two of the plots we have created to see how is the participation of countries at the different olympic years.

![olymps1](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/main/ImagesReadme/bubbleChart.jpg)

![olymps2](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/main/ImagesReadme/Top15_map.png)
Figure 2. Performance (Top15) of each country by year

### Scatter matrix between Indicators:

To determine if there are indicators that are highly correlated between them, we perform a scattermatrix between the economic indicators and in our further analysis only considered indicators that are not correlated. Figure 1 shows the scattermatrix, where it is possible to see how `GDP` and `GNI` as well as `HDI` and `HDI Rank` are higly correlated

![scatter](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/main/ImagesReadme/Correlation.png)

Figure 3. Scattermatrix of all indicators

## 2. Machine Learning:

In order to answer the second question of our project, we want to apply an unsupervised machine learning algorithm, so we can categorized countries into groups without having any previous information about their membership. We have used `k-means` and the `Elbow Curve` Method for estimating a possible number of groups.  An initial exploration of this analysis is in jupyter notebook in [here](https://github.com/JoeAB3/Group5Capstone_Project/blob/Leidy_dbpart/CodeInJupyter/Analysis_KmeansPlots.ipynb)

### Description of preliminary data preprocessing: 

We are going to apply `k-means` in a dataset with 4 indicators: `GDP`, `HDI`, `Population`, `Top15` for each country and each Olympic Game.  Because there are multiple values for the same parameters (since we are considering 7 olympic games), we are going to consider an analyis per Olympic Game. This means, will have a clustering of the countries per each Olympic year.

### Description of preliminary feature engineering:

Because we have several economic factors that could be related, we calculate the correlation between these factors. This was carried out by using the scatter matrix that is shown in Figure 3. After this process we keep the 4 factors/indicators previously listed.

### Explanation of model choice, including limitations and benefits

Because we do not have any priori information about how the countries could be categorized depending on how they perform economically and at the Olympic Games, we want to explore if there is an actual separation or relationship among them.  In this way, we choose the widely known `K-means` algorithm. The benefit of using k-means is that is simple to implement, fast, and guarantees convergence. However, its limitation is that we need to assume prior information about the data, such the number of clusters (`k`). 

### Training and Testing of data

We do not have any training or testing data because our data does not provide any labeled data and furthermore our analyis does not require any training or testing process. However, as part of future improvements for our project we have explained in the **Improvents to the Analysis** section how we can set up a training and testing data.

## 3. Database:

Due to the nature of our data, we use a SQL database to save three tables: `Indicators`, `Olympics`, and `DataAnalysis`. Based on the two first tables, we create the third one with the economic indicators of our interest and the information about the Olympic Games. During the development stage we use `PgAdmin` to create the database and storage the tables. However, for the deployment of our app in `Heroku` we have switched to `Sqlite`, so we do not need to have our database hosted in a web service. We can easily make this transition since we are using `SqlAlchemy` library that uses basically the same methods or functions for manage both kind of databases.

### Database stores static data for use during the project:

The original raw data is access through API calls from our application to the corresponding websites. After a cleaning process in Python, two tables are writen to the database and from them another table is generated to be used in the Machine Learning Analysis. In the [Flask_db_dashboard](https://github.com/JoeAB3/Group5Capstone_Project/tree/main/Flask_db_dashboard) folder there are the scripts that load the tables from internet and perform the initial cleaning for saving the tables into the database. 

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

Each one of the tables are writen into the database (db) using a connection strig to the `SQL` db (during the development stage) and to the `SQLite` db.

1. Connection string to a local db:
```python
db_string = f"postgresql://postgres:{db_password}@127.0.0.1:5432/OlympicAnalysis_FP"
```
2. Connection string to sqlite db:
```python
db_string = 'sqlite:///db.sqlite'
```

## 4. Dashboard

We will have two dashboards to display the findings of our project.  The **Data Exploration** dashboard will display charts showing patterns of the socioeconomic factors as well as the performance at the olympics among countries. These plots will be interactive, as the desire is to have the user be able to filter them by olympic year.  This dashboard will be built in `Tableau`.  The second dashboard will be build using `Flask` and `html` template with some interactive features in `JavaScript`.

### Report from the data exploration:

The `Tableau` dashboard allows the user to choose the year of the Olympic Game that wants to see, and displays the charts for the data exploration that were explained before. 

![scatter](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/main/ImagesReadme/dashboard_1.png)

![scatter](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/main/ImagesReadme/dashboard_2.png)

Figure 6. Tableau Dashboard Overview

### Report from the machine learning task:

A second dashboard will present the findings from our machine learning analysis. The `app.py`, `html` and `css` files are in the same folder in [here](https://github.com/JoeAB3/Group5Capstone_Project/tree/main/Flask_db_dashboard). The `app.py` manages the connection to a our sqlite database as well as the `html` template. 

![dashboard](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/main/ImagesReadme/DashboardOverview.png)
Figure 7. An overview of the dashboard created for showing UML results.

When the dashboard is open for the first time the database needs to be setup by creating the three tables shown in the ERD Diagram (Figure 4). This is performed after the `Loading` button is hit. Once the button indicates the process is finished. The user can use the selector to choose what Olympic year wants to see (Figure 8). After the user has chose the Year, a 3-d scatterplot and a world map are displayed. 

![dashboard1](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/main/ImagesReadme/Dashboard_Interaction.png)

![dashboard2](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/main/ImagesReadme/Dashboard_Interaction2.png)
Figure 8. The dashboard with the interactive elements.

**The dashboard has more than one interactive element:** 

1. The `Loading` button created in `JavaScript` has two icons that allows the user to check the time the database is being set.

2. A `selector` input with a `submit` button. These two elements jointly allow the user to choose what Olympic year wants to see. 

3. The scatterplot as well as the world map allow the user some interaction, as they allow the display of the country information as the data points (in the scatterplot) or the country (in the world map) are hovering in.

![dashboard3](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/Leidy_dbpart/ImagesReadme/ScatterplotDashboard.png)
![dashboard4](https://raw.githubusercontent.com/JoeAB3/Group5Capstone_Project/Leidy_dbpart/ImagesReadme/worldMapDashboard.png)
Figure 9. Clustering of countries shown in different colors in the scatterplot and world map.

## Dashboard Deployed in Heroku

Our dashboard is deployed in [Heroku](https://olympic-analysis-deployment.herokuapp.com/). The folder that contains all scripts and files required for the deployment process are in [olympic_analysis_deployment](https://github.com/JoeAB3/Group5Capstone_Project/tree/main/olympic_analysis_deployment) folder.

## 5. Improvements to the Analysis in the Future:

The most important area to improve in this analysis could be the gathering of more information about other socioeconomic factors. This will allow to have a bigger sample size with the potential for a predictive analysis.  Below there is an analysis that shows how training and testing data could have been used.

### Training and Testing of data with a limited size:
Data was trained and testing by splitting the dataset into groups, with the training group consisting of 80 percent of the dataset while the testing group consisted of only 20 percent of the dataset. A random state of 10 was used to keep the training and testing groups the same over a period of multiple tests. The model was trained using a Linear Regression Model, allowing for a predictive linear regression chart to be created. However, due to the dataset not having enough data points present during the training and testing phases, the best choice was to switch to unsupervised learning in order to achieve optimal data analysis and exploration.

![Train and Test setup](https://user-images.githubusercontent.com/88119309/150042125-17407ac8-92d3-4895-adc4-9432ba68f03c.PNG)
![Linear Regression prediction](https://user-images.githubusercontent.com/88119309/150042166-ce0b390b-1e32-4db7-8abf-06edea53cef9.PNG)

## 6. Presentation
Link to Google Slides of presentation with speaker notes is [here](https://docs.google.com/presentation/d/1uGkUmyf4gTuGKR7ov_M5aNJdvH7qaN4pgnWGX73oN0E/edit?usp=sharing).