"""
Class module which contains all ambiguous classes

imports:


Class Element:
specifically this class is intended to stroe the raw organized pull 
from the excel sheets and is the object for each row in the excel spreadsheet.

Class Dprep:
	this class handles all data preparation with specific functions

"""
class Plotter(object):
	"""The plotter object instantiates a plotting 
	instance where by the user can manage all figures 
	which they wish to plot. It loads the ALL data 
	object which houses contents of all of the data 
	from the WTD"""
	def __init__(self, ALL):
		self.ALL = ALL

	def makepdf(self,name):
		"""
		this creates a pdf file with the name passed to the make fig function. 
		Then, it creates a figure on the pdf file. plot properties are specified 
		by the pltpr function. C and C line plot is generated and plotted. then 
		the figure and pdf files are saved and closed. The pdf files are treated 
		as object which are generated and then operated on. 
		"""
		# prepare imports
		import matplotlib.pyplot as plt
		from matplotlib.backends.backend_pdf import PdfPages
		self.pdf_pages = PdfPages(name)
		# set up plot properties
		self.plt = plt

		# save and close the figure
	
	def genfig(self,title):
		self.fig = self.plt.figure(figsize=(6.875, 6), dpi=100)
		self.plt.title(title)
		self.plt.grid()

	def svfig(self):

		self.pdf_pages.savefig(self.fig)

	def clpdf(self):

		self.pdf_pages.close()

	def pltCandC(self,c1,c2,color,mklabel,label2use):
		# initialize C & C lines
		x,y = self.CandC(c1, c2)
		# plotting action
		self.plt.grid()
		self.plt.xlabel('At')
		self.plt.ylabel('Cp')
		self.plt.xscale('log')
		if mklabel == True:
			self.plt.plot(x,y,color=color,label = label2use)
		else:
			self.plt.plot(x,y,color=color)


 	def CandC(self,c1,c2):
		x,y = self.AISC_CC(c1,c2)
		return x,y

	def mklegend(self,*args):
		
		self.plt.grid()
		self.plt.xlabel('At')
		self.plt.ylabel('Cp')
		self.plt.xscale('log')
		self.plt.legend(*args,loc=0,prop={'size':6})


	def lgf(self,x1,x2,y1,y2,x):
		import math
		b = y2 - (math.log10(x2)/(math.log10(x2)-math.log10(x1)))*(y2-y1)
		y = ((y2-y1)/(math.log10(x2)-math.log10(x1)))*math.log10(x) + b
		return y

	def AISC_CC(self,c1,c2):
		import math
		x1 = range(1,11)
		y1 = [c1]*len(x1)

		x2 = range(11,101)
		y2 = [self.lgf(10., 100., c1, c2, e) for e in x2]

		x3 = range(101,301)
		y3 = [c2]*len(x3)

		x = x1 + x2 + x3
		y = y1 + y2 + y3

		return x,y

	def WTD(self,x,y,color,mklabel,label2use):
		self.plt.grid()
		self.plt.xlabel('At')
		self.plt.ylabel('Cp')
		self.plt.xscale('log')
		if mklabel == True:
			self.plt.plot(x,y,'x', color=color, markersize=2., label = label2use)
		else:
			self.plt.plot(x,y,'x', color=color, markersize=2.)

	def WTDfit(self,x,y,color,mklabel,label2use):
		import numpy as np
		# fit with np.polyfit
		m1, m2, b = np.polyfit(x, y, 2)
		x1=np.linspace(10,270,1000)
		y = [m1*e**2 + m2*e + b for e in x1]

		xy=sorted(zip(x1,y))
		x = []
		y = []
		for x1,y1 in xy:
			x.append(x1)
			y.append(y1)
		self.plt.grid()
		self.plt.xlabel('At')
		self.plt.ylabel('Cp')
		self.plt.xscale('log')

		if mklabel == True:
			self.plt.plot(x,y,'-',color=color,label = label2use)
		else:
			self.plt.plot(x,y,'-',color=color)


class ElementSP(object):

	
	"""This class maintains the definition 
	of an element object. Within it,
	there are properties which define 
	its context in the scope of the wind tunnel 
	data proccessing procedure."""
	
	def __init__(self, WD, PN, GCp, mxmn, zone, AT, alpha, On, RC):
		self.WD = WD
		self.PN = PN
		self.GCp = GCp
		self.mxmn = mxmn
		self.zone = zone
		self.AT = AT
		self.alpha = alpha 
		self.On = On
		self.RC = RC



class ElementATP(object):

	
	"""This class maintains the definition 
	of an element object. Within it,
	there are properties which define 
	its context in the scope of the wind tunnel 
	data proccessing procedure."""
	
	def __init__(self, ATG, WD, mxmn, run, RC, alpha, On, AT, GCp):
		self.ATG = ATG
		self.WD = WD
		self.mxmn = mxmn 
		self.run = run
		self.RC = RC
		self.alpha = alpha
		self.On = On
		self.AT = AT
		self.GCp = GCp


class Panel(object):
	'''
	represents a distint panel object 
	whose properties depend on the wind 
	directionality, location, and the offset 
	from the roof ridge
	'''


	def __init__(self,location,WD,On):
		self.WD = WD
		self.On = On
		self.location = location
		A = 18.33
		if WD ==0:
# zone 1
			if location==2:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==3:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==4:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==5:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.

			if location==7:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==8:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==9:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.

			if location==10:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.

			if location==12:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==13:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==14:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==15:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.

#zone 2
			if On==6:
				if location ==1:
					self.w1 = 0.5*5.5/A
					self.w2 = 2.5*5.5/A
					self.w3 = 0.
				if location ==6:
					self.w1 = 0.5*5.5/A
					self.w2 = 2.5*5.5/A
					self.w3 = 0.
				if location ==11:
					self.w1 = 0.5*5.5/A
					self.w2 = 2.5*5.5/A
					self.w3 = 0.
				if location ==16:
					self.w1 = 0.
					self.w2 = 0.5*5.5/A
					self.w3 = 2.5*5.5/A

			if On==21:
				if location ==1:
					self.w1 = 1.75*5.5/A
					self.w2 = 1.25*5.5/A
					self.w3 = 0.
				if location ==6:
					self.w1 = 1.75*5.5/A
					self.w2 = 1.25*5.5/A
					self.w3 = 0.
				if location ==11:
					self.w1 = 1.75*5.5/A
					self.w2 = 1.25*5.5/A
					self.w3 = 0.
				if location ==16:
					self.w1 = 0.
					self.w2 = 1.75*5.5/A
					self.w3 = 1.25*5.5/A

			if On==36:
				if location ==1:
					self.w1 = 1.
					self.w2 = 0.
					self.w3 = 0.
				if location ==6:
					self.w1 = 1.
					self.w2 = 0.
					self.w3 = 0.
				if location ==11:
					self.w1 = 1.
					self.w2 = 0.
					self.w3 = 0.
				if location ==16:
					self.w1 = 0.
					self.w2 = 1.
					self.w3 = 0.
			
			if location == 17:
				self.w1 = 0.
				self.w2 = 1.
				self.w3 = 0.
			if location == 18:
				self.w1 = 0.
				self.w2 = 1.
				self.w3 = 0.
			if location == 19:
				self.w1 = 0.
				self.w2 = 1.
				self.w3 = 0.
			if location == 20:
				self.w1 = 0.
				self.w2 = 1.
				self.w3 = 0.


		if WD ==1:
# zone 1
			if location==17:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==18:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==19:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==20:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.

			if location==7:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==8:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==9:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.

			if location==10:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.

			if location==12:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==13:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==14:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.
			if location==15:
				self.w1 = 1.
				self.w2 = 0.
				self.w3 = 0.

#zone 2
			if On==6:
				if location ==16:
					self.w1 = 0.5*5.5/A
					self.w2 = 2.5*5.5/A
					self.w3 = 0.
				if location ==6:
					self.w1 = 0.5*5.5/A
					self.w2 = 2.5*5.5/A
					self.w3 = 0.
				if location ==11:
					self.w1 = 0.5*5.5/A
					self.w2 = 2.5*5.5/A
					self.w3 = 0.
				if location ==1:
					self.w1 = 0.
					self.w2 = 0.5*5.5/A
					self.w3 = 2.5*5.5/A

			if On==21:
				if location ==16:
					self.w1 = 1.75*5.5/A
					self.w2 = 1.25*5.5/A
					self.w3 = 0.
				if location ==6:
					self.w1 = 1.75*5.5/A
					self.w2 = 1.25*5.5/A
					self.w3 = 0.
				if location ==11:
					self.w1 = 1.75*5.5/A
					self.w2 = 1.25*5.5/A
					self.w3 = 0.
				if location ==1:
					self.w1 = 0.
					self.w2 = 1.75*5.5/A
					self.w3 = 1.25*5.5/A

			if On==36:
				if location ==16:
					self.w1 = 1.
					self.w2 = 0.
					self.w3 = 0.
				if location ==6:
					self.w1 = 1.
					self.w2 = 0.
					self.w3 = 0.
				if location ==11:
					self.w1 = 1.
					self.w2 = 0.
					self.w3 = 0.
				if location ==1:
					self.w1 = 0.
					self.w2 = 1.
					self.w3 = 0.
			
			if location == 2:
				self.w1 = 0.
				self.w2 = 1.
				self.w3 = 0.
			if location == 3:
				self.w1 = 0.
				self.w2 = 1.
				self.w3 = 0.
			if location == 4:
				self.w1 = 0.
				self.w2 = 1.
				self.w3 = 0.
			if location == 5:
				self.w1 = 0.
				self.w2 = 1.
				self.w3 = 0.

class Generate_Array(object):
	"""
	This takes the panel object and makes 
	an array that is representative of a 
	certain config with a specific WD and
	 a specific On. each panel has a w1, 
	 w2 and w3 which can be used to build
	  the ATG w1, w2, w3
	"""

	def __init__(self,WDn,On):
		self.array = {}

		locn = range(1,21)
		for x1 in locn:
			self.array[x1] = Panel(x1, WDn, On)


class ATGdict(object):
	"""
	provides a dictionary of the gemoetric 
	areas and thier associated panel numbers
	"""

	def __init__(self):
		self.ATGd = {}
		self.ATGd[1] = [1,2,3,4,5]
		self.ATGd[2] = [6,7,8,9,10]
		self.ATGd[3] = [11,12,13,14,15]
		self.ATGd[4] = [16,17,18,19,20]
		self.ATGd[5] = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
		self.ATGd[6] = [11,12,13,14,15,16,17,18,19,20]
		self.ATGd[7] = [13,14,15,18,19,20]
		self.ATGd[8] = [11,12,13,16,17,18]
		self.ATGd[9] = [1,2,3,4,16,17,18,19]
		self.ATGd[10] = [6,7,8,9,11,12,13,14]


class Findweights(object):
	"""
	This builds the arrays for each different 
	WD and On when initialized. Then, it 
	calculates the weights of each ATG and 
	outputs that.
	"""

	def __init__(self,ele):
		# has w1,w2,w3 values for each individual panel for each of the WD and O6 possibilities
		self.ele = ele
		self.Array_0_6 =Generate_Array(0,6)
		self.Array_0_21=Generate_Array(0,21)
		self.Array_0_36=Generate_Array(0,36)
		self.Array_1_6 =Generate_Array(1,6)
		self.Array_1_21=Generate_Array(1,21)
		self.Array_1_36=Generate_Array(1,36)

		# contains my ATG panel numberings for ATGn 1 to 10
		self.myATG=ATGdict()

	def calcweights(self):
		"""
		This produces the w1n, w2n, and w3n. 
		WHich are the weights associated with each ATGn
		"""
		for x1 in range(len(self.ele)):
			o = self.ele[x1]
			w1n, w2n, w3n=self.matcher(o.ATGn, o.WD, o.On)
			o.w1n = w1n
			o.w2n = w2n
			o.w3n = w3n

		return self.ele

	def matcher(self, ATGn, WD, On):
		"""
		This is housed inside of the calcweights 
		and is the actual decision mechanism handeling 
		the weighting of each panel object.
		"""

		if WD==0.:
			if On == 6.:
				w1c = []
				w2c = []
				w3c = []
				w1 = 0.
				w2 = 0.
				w3 = 0.
				for ATGi in self.myATG.ATGd[ATGn]:
					for panel_num in range(1,21):
						if ATGi==panel_num:
							w1 = self.Array_0_6.array[panel_num].w1
							w2 = self.Array_0_6.array[panel_num].w2
							w3 = self.Array_0_6.array[panel_num].w3

							w1c.append(w1)
							w2c.append(w2)
							w3c.append(w3)
				w1k = sum(w1c)
				w2k = sum(w2c)
				w3k = sum(w3c)

				ws = w1k + w2k + w3k
				w1n = w1k/ws
				w2n = w2k/ws
				w3n = w3k/ws


			if On == 21.:
				w1c = []
				w2c = []
				w3c = []
				w1 = 0.
				w2 = 0.
				w3 = 0.
				for ATGi in self.myATG.ATGd[ATGn]:
					for panel_num in range(1,21):
						if ATGi==panel_num:
							w1 = self.Array_0_21.array[panel_num].w1
							w2 = self.Array_0_21.array[panel_num].w2
							w3 = self.Array_0_21.array[panel_num].w3

							w1c.append(w1)
							w2c.append(w2)
							w3c.append(w3)
				w1k = sum(w1c)
				w2k = sum(w2c)
				w3k = sum(w3c)

				ws = w1k + w2k + w3k
				w1n = w1k/ws
				w2n = w2k/ws
				w3n = w3k/ws


			if On == 36.:
				w1c = []
				w2c = []
				w3c = []
				w1 = 0.
				w2 = 0.
				w3 = 0.
				for ATGi in self.myATG.ATGd[ATGn]:
					for panel_num in range(1,21):
						if ATGi==panel_num:
							w1 = self.Array_0_36.array[panel_num].w1
							w2 = self.Array_0_36.array[panel_num].w2
							w3 = self.Array_0_36.array[panel_num].w3

							w1c.append(w1)
							w2c.append(w2)
							w3c.append(w3)
				w1k = sum(w1c)
				w2k = sum(w2c)
				w3k = sum(w3c)

				ws = w1k + w2k + w3k
				w1n = w1k/ws
				w2n = w2k/ws
				w3n = w3k/ws



		if WD==1.:
			if On == 6.:
				w1c = []
				w2c = []
				w3c = []
				w1 = 0.
				w2 = 0.
				w3 = 0.
				for ATGi in self.myATG.ATGd[ATGn]:
					for panel_num in range(1,21):
						if ATGi==panel_num:
							w1 = self.Array_1_6.array[panel_num].w1
							w2 = self.Array_1_6.array[panel_num].w2
							w3 = self.Array_1_6.array[panel_num].w3

							w1c.append(w1)
							w2c.append(w2)
							w3c.append(w3)
				w1k = sum(w1c)
				w2k = sum(w2c)
				w3k = sum(w3c)

				ws = w1k + w2k + w3k
				w1n = w1k/ws
				w2n = w2k/ws
				w3n = w3k/ws


			if On == 21.:
				w1c = []
				w2c = []
				w3c = []
				w1 = 0.
				w2 = 0.
				w3 = 0.
				for ATGi in self.myATG.ATGd[ATGn]:
					for panel_num in range(1,21):
						if ATGi==panel_num:
							w1 = self.Array_1_21.array[panel_num].w1
							w2 = self.Array_1_21.array[panel_num].w2
							w3 = self.Array_1_21.array[panel_num].w3

							w1c.append(w1)
							w2c.append(w2)
							w3c.append(w3)
				w1k = sum(w1c)
				w2k = sum(w2c)
				w3k = sum(w3c)

				ws = w1k + w2k + w3k
				w1n = w1k/ws
				w2n = w2k/ws
				w3n = w3k/ws


			if On == 36.:
				w1c = []
				w2c = []
				w3c = []
				w1 = 0.
				w2 = 0.
				w3 = 0.
				for ATGi in self.myATG.ATGd[ATGn]:
					for panel_num in range(1,21):
						if ATGi==panel_num:
							w1 = self.Array_1_36.array[panel_num].w1
							w2 = self.Array_1_36.array[panel_num].w2
							w3 = self.Array_1_36.array[panel_num].w3

							w1c.append(w1)
							w2c.append(w2)
							w3c.append(w3)
				w1k = sum(w1c)
				w2k = sum(w2c)
				w3k = sum(w3c)

				ws = w1k + w2k + w3k
				w1n = w1k/ws
				w2n = w2k/ws
				w3n = w3k/ws

		return w1n, w2n, w3n




class Dprep(object):
	'''
	prep_APT
		add ATGn and float everything that should be 
		floated except for the alpha
	'''
	def prep_APT1(self, obj_ele_dict):
	
		for x1 in range(len(obj_ele_dict)):
			o=obj_ele_dict[x1]

			if o.AT == 90:
				if o.ATG == 1:
					o.ATGn = 1
				if o.ATG == 2:
					o.ATGn = 2
				if o.ATG == 3:
					o.ATGn = 3
				if o.ATG == 4:
					o.ATGn = 4
			if o.AT == 108:
				if o.ATG == 1:
					o.ATGn = 5
				if o.ATG == 2:
					o.ATGn = 6
			if o.AT == 144:
				if o.ATG == 1:
					o.ATGn = 7
				if o.ATG == 2:
					o.ATGn = 8
			if o.AT == 180:
				o.ATGn = 9
			if o.AT == 270:
				o.ATGn = 10


		return obj_ele_dict

	def prep_SPT1(self, obj_ele_dict):
		# use the weight finder class to obtain the array panel configs
		weightfinder=Findweights(obj_ele_dict)

		for x1 in range(len(obj_ele_dict)):
			o=obj_ele_dict[x1]
			if o.WD==0.0:
				if o.On==6.0:
					array=weightfinder.Array_0_6
					PN = o.PN
					o.w1n = array.array[PN].w1
					o.w2n = array.array[PN].w2
					o.w3n = array.array[PN].w3
				if o.On==21.0:
					array=weightfinder.Array_0_21
					PN = o.PN
					o.w1n = array.array[PN].w1
					o.w2n = array.array[PN].w2
					o.w3n = array.array[PN].w3
				if o.On==36.0:
					array=weightfinder.Array_0_36
					PN = o.PN
					o.w1n = array.array[PN].w1
					o.w2n = array.array[PN].w2
					o.w3n = array.array[PN].w3

			if o.WD==1.0:
				if o.On==6.0:
					array=weightfinder.Array_1_6 
					PN = o.PN
					o.w1n = array.array[PN].w1
					o.w2n = array.array[PN].w2
					o.w3n = array.array[PN].w3
				if o.On==21.0:
					array=weightfinder.Array_1_21
					PN = o.PN
					o.w1n = array.array[PN].w1
					o.w2n = array.array[PN].w2
					o.w3n = array.array[PN].w3
				if o.On==36.0:
					array=weightfinder.Array_1_36
					PN = o.PN
					o.w1n = array.array[PN].w1
					o.w2n = array.array[PN].w2
					o.w3n = array.array[PN].w3

		return obj_ele_dict


