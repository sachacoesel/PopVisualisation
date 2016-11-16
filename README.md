#PopVis
The tool we will develop will help users to explore phytoplankton population abundances over a transect in an interactive way. 


###Organization of the project
The project has the following structure:
PopVis

###Data input
For example, two datasets have been provided. It requires users to use data where time and geographical information are present. 
 
1. continuous flowcytometer data cruise 2013 : cell abundance, time/date, lat/lon
2. continuous measurements salinity, Temp, irradiance, chl fluorescence, time/date, lat/lon

###Users:
-scientist

What questions need to be answered:
1. providing interactive visualisation tools for data exploration
2. effect of environmental parameters on cell abundance per population
3. diel variation - periodicity

1. two datasets: 1- biological (cell count) 2- environmental (temp salinty, etc), 3- geographical
2. data merging tool
3. grouping tool
4. plotting tool -graphical
5. plotting tool - geographical 

ipython notebook

Issues-
- do we need statistics?
- double check if time and lat/lon between two datafiles are compatible.
- diel analysis: moving through different area's, populations will change as well.