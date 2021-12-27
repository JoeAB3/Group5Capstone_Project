CREATE TABLE Olympics(
  CountryCode character(3) NOT NULL,
  Year integer NOT NULL,
  Season character NOT NULL,
  MedalsCount integer NOT NULL
  PRIMARY KEY (CountryCode, Year)
);

CREATE TABLE Indicators (
  CountryCode character(3) NOT NULL,
  GDP integer NOT NULL,
  GNI integer NOT NULL,
  PopSize integer NOT NULL,
  Year character NOT NULL,
  HDI integer NOT NULL,
  HDI_Rank integer NOT NULL
  PRIMARY KEY (CountryCode, Year)
);
