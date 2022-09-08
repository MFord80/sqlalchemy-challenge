# sqlalchemy-challenge

This repository contains:   
    * Jupiter notebook of climate analysis.  
    * A resource folder containing data as both CSVs and in SQLite format.  
    * A python application that create an API containing jsonified representation of some aspects of the analysed data.  

### API routes

The following routes are available in the API:
/api/v1.0/precipitation
/api/v1.0/stations
/api/v1.0/tobs
/api/v1.0/yyyy-mm-dd [start]
/api/v1.0/yyyy-mm-dd/yyyy-mm-dd [start/end]

The routes provide the following data:

*precipitation*
Precipitation data for the most recent 12 months

*stations*
A list of the stations in the dataset

*tobs*
Temperatures observed for the most recent 12 months at the station that made the highest number of recordings (USC00519281)

*yyyy-mm-dd [start]*
User generated data returning the maximum, minimum and average temperature for the period from and including the date provided to the most recent recorded date.

*yyyy-mm-dd [start/end]*
User generated data returning the maximum, minimum and average temperature for the period from and including the first date provided [start] to the second date provided [end].

Note: Data was recorded for dates between 2010-01-01 and 2017-08-23 inclusive. Dates entered outside of this range will not return a result.
