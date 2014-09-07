"""
Main module for execution

imports:
	data_collection
		implementation (functional) of collecting the WTD for proccessing
	classes
		state (spatial) of classes implemented through out the package
	plotting
		plotting functionality of the collected data (functional)
	tables
		tabling functionality of the collected data (functional)

This code starts by creating a collector object (functional). 
Then the collect() method is run to perform the funciton of collecting the data.

"""

import classes.classes
import plotting.plotting as plting
import tables.table
import data_collection.dataprep as data_prep


# excecute data preparation and return two dictionaries of objects respectivly representing the single panel and the area averaged panel results
ALL = data_prep.Dataprep()
# ALL contains both of the SP and APT object dictionaries of elements

# instantiate a plotter instance
pltt1=plting.Pltact(ALL)