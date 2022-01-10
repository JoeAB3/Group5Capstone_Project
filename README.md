
# Analyzing How the Economic Factors could impact the Performance of Countries in the Summer Olympic Games

In our final project, we are interested in analyze how different economic factors could impact the performance of countries when they participate in the Summer Olympic Games. <mark>We have counted the total events in which each country has finished at the Top 15 at each Olympic Game since 1992. A country with a good performance, in our analysis, is a country that has finished within the first 15 places.</mark>

## Reason we chose this topic:

The team is interested in economics and sports

## Questions we hope to answer with the data:

- Does a countries HDI, annual GDP or total population contribute to a countries performance at the olympics?
- <mark>How are countries distributed depending on their economic factors and performance at the Olympics? Is there some natural clustering?
</mark>

## Description of source of data:

Economic Indicators will be draw from the [**World Bank Data Catalog**](https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators) that has around 1453 indicators compiled from official sources around the world (204 countries are considered). And from [**United Nations**](http://hdr.undp.org/en/indicators/137506#), that is the *Human Development Index(HDI)*, which "measures average achievement in three basic dimensions of human development: long and healthy life, knowledge and decent standard of living. The data sets are in `csv` format and an initially exploration is made in `Python-Pandas Library`. The jupyter notebook is found [here](https://github.com/JoeAB3/Group5Capstone_Project/blob/Leidybranch/pre-processingWBD.ipynb).

<mark> For the Olympic data various data sources were identified for this data.  We identified all the competiting countires in each Summer Olympic games.  Another data source found the placing  for each olympic event.  An additional data set was pulled in to find how many events were participated in.  All these data were used for the primary Olympic data set.</mark>. The cleaning was as well made in `Python` and the code to do it is in [here](https://github.com/JoeAB3/Group5Capstone_Project/tree/Leidybranch/CodeInJupyter/pre-processingOlympicGames.ipynb).

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

In order to answer the second question of our project, we want to apply an unsupervised machine learning algorithm, so we can categorized countries into groups without having any previous information about their membership. 



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
Figure. ERD for OlympicAnalysis Database.

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
Link to Google Slides:
https://docs.google.com/presentation/d/1uGkUmyf4gTuGKR7ov_M5aNJdvH7qaN4pgnWGX73oN0E/edit?usp=sharing

