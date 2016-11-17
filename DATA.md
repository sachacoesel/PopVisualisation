# Dataset description

The data consists of continuous flowcytometric measurements of photosynthetic pico-eukaryotes using the [SeaFlow](http://armbrustlab.ocean.washington.edu/resources/seaflow) cytometer data obtained during the 2013 deepDOM cruise covering a transect from Uruguay to the Amazon.

This package comes with two data files.

1. SeaFlow-clean-Oct2016.csv

- cruise	(code of the specific cruise)
- file	(name of the seaflow file)
- time	(date time (GMT))
- lat		(latitude coordinate)
- lon		(longitude coordinate)
- opp_evt_ratio	(raw data _ event rate)
- flow_rate		(raw data _ flow rate)
- file_duration	(time fo concatenation)
- pop		(populations: beads/picoeuks/prochloro/synecho/unknown)
- n_count	(nr of counts)
- abundance (abundance in 10^6 / L)
- fsc_small	(forward scatter)
- chl_small	(chlorophyll fluorescence)
- 'pe'	()

2. sfl.csv

- cruise	(code of the specific cruise)
- file	(name of the seaflow file)
- time	(date time (GMT))
- lat		(latitude coordinate)
- lon		(longitude coordinate)
- conductivity	
- salinity	
- ocean_tmp	
- par	
- bulk_red	
- stream_pressure	
- flow_rate	
- event_rate

