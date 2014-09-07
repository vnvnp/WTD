"""
Data collection module

"""

class Collector():
	"""
	Class Collector:
	This class houses the machinary to collect the excel data. It employs the Element object to represent a dictionary of the single panel row entries in the excel sheet.

	imports:
		numpy
			slice out the excel contents
		eplib
			pull data from the excel sheet /Users/evan/Dropbox/SBoS/SBOS_Prado/windtunnel_data/WTDATA_19june14/SPTAPTFB5.xlsx
		sys
			incorporate the module 'classes' located in a parallel path in the package directory
		classes
			contains classes used in the Data collection module
	"""





	def collectSP(self):
		import numpy
		import eplib
		import sys
		sys.path.append('/Users/evan/Dropbox/SBoS/SBOS_Prado/windtunnel_data/WTDATA_19june14/WTDscript_9_3_2014/classes')
		from classes.classes import ElementSP
		#pull data from the SPTAPTFB Excel sheet
		self.conts=eplib.rdxl_1('/Users/evan/Dropbox/SBoS/SBOS_Prado/windtunnel_data/WTDATA_19june14/SPTAPTFB5.xlsx', 'STP,ATP,FB')

		#turn the sheet into a numpy array
		conts = numpy.array( self.conts )

		#pull a block out of the array
		self.SPconts = conts[2:962,1:10]

		#make the SP element objects from the array
		self.inp=len(self.SPconts); self.SP_ele={}
		for x1 in range(self.inp):
		    self.SP_ele[x1]=ElementSP(
		    	float(self.SPconts[x1][0]), 
		    	float(self.SPconts[x1][1]), 
		    	float(self.SPconts[x1][2]), 
		    	self.SPconts[x1][3], 
		    	self.SPconts[x1][4], 
		    	float(self.SPconts[x1][5]),
		    	float(self.SPconts[x1][6]),
				float(self.SPconts[x1][7]),
				self.SPconts[x1][8])

		return self.SP_ele

	def collectAPT(self):
		import numpy
		import eplib
		import sys
		sys.path.append('/Users/evan/Dropbox/SBoS/SBOS_Prado/windtunnel_data/WTDATA_19june14/WTDscript_9_3_2014/classes')
		from classes.classes import ElementATP
		#pull data from the SPTAPTFB Excel sheet
		self.conts=eplib.rdxl_1('/Users/evan/Dropbox/SBoS/SBOS_Prado/windtunnel_data/WTDATA_19june14/SPTAPTFB5.xlsx', 'STP,ATP,FB')

		#turn the sheet into a numpy array
		conts = numpy.array(self.conts)

		#pull a block out of the array
		self.APTconts = conts[2:482,12:21]


		#make the SP element objects from the array
		self.inp=len(self.APTconts); self.APT_ele={}
		for x1 in range(self.inp):
	
			self.APT_ele[x1]=ElementATP(
		    	float(self.APTconts[x1][0]), 
		    	float(self.APTconts[x1][1]), 
		    	self.APTconts[x1][2], 
		    	float(self.APTconts[x1][3]), 
		    	self.APTconts[x1][4], 
		    	self.APTconts[x1][5],
		    	float(self.APTconts[x1][6]),
				float(self.APTconts[x1][7]),
				float(self.APTconts[x1][8]))

		return self.APT_ele

