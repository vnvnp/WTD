"""
Class dataprep operates on the collected data for further extraction and synthesis
"""

class Dataprep():
	"""
	this class first collects the data at initialization (SPT and APT) and then performs preparations on the data
	"""
	def __init__(self):
		import data_collection.DC as DC
		import classes.classes as DP
		# generate the collector object
		DCC=DC.Collector()
		# run the collection method and obtain the element objects for SPT and APT
		SP_ele=DCC.collectSP()
		APT_ele=DCC.collectAPT()

		# create the data prep object
		DPr=DP.Dprep()
		# prepare the APT data
		APT_ele_mod1=DPr.prep_APT1(APT_ele)

		weighfinder=DP.Findweights(APT_ele_mod1)
		APT_ele_mod2=weighfinder.calcweights()

		# prepare the SPT data. this adds the weights to it
		SP_ele_mod1=DPr.prep_SPT1(SP_ele)

		# setting object dictionaries to be defined in the classes variables
		self.SP_ele_mod1 = SP_ele_mod1
		self.APT_ele_mod2 = APT_ele_mod2

		#for x1 in range(480):
		#	print vars(APT_ele_mod2[x1])



		for x1 in range(960):
			print vars(SP_ele_mod1[x1])