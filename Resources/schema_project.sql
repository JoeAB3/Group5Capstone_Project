CREATE TABLE Olympics(
  Country character NOT NULL,
  CountryCode character(3) NOT NULL,
  Year integer NOT NULL,
  Perc integer NOT NULL,
  Top15 integer NOT NULL,
  PRIMARY KEY (CountryCode, Year)
);

CREATE TABLE Indicators (
	Year integer NOT NULL,
  CountryCode character(3) NOT NULL,
	CountryName character NOT NULL,
  GDPCapita integer NOT NULL,
  GNICapita integer NOT NULL,
	Physicians integer NOT NULL,
  Population integer NOT NULL,
	SuicideRate integer NOT NULL,
  HDI_Rank integer NOT NULL,
	HDI integer NOT NULL
);
