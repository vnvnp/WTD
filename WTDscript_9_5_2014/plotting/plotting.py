"""
Plotting module

imports:


"""

class Pltact(object):
	"""
	houses the instantiation of the plotting actions class. 
	This maintains the driving mechanisms for the proccess 
	of plotting. it includes the data filter object which 
	is in charge of filtering the accepted ALL data structure
	down to a scoped level which can then be passed to a 
	plotting figure for a specific scope. there then the 
	C&C line data will be overlayed on the plot.
	"""
	def __init__(self,ALL):
		self.ALL = ALL
		self.togethermxmn()


	def togethermxmn(self):

		self.initializepdf('mxmn.pdf')
		#"""
		self.genfig(r'$\alpha=15$, Roof Cap Installed')

		self.C_and_C(c1=0.6, c2=0.3,label2use='C&C')
		x1,y1 = self.APT_plt( mxmni='max', RCi='Installed', alphai='14.0',Zc = 1, color='blue',label2use='Zone 1')
		x2,y2 = self.SPT_plt( mxmni='max', RCi='Roof Cap Installed', alphai=15.0, Zc = 1, color='blue',mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='blue',label2use='Polyfit Zone 1')

		self.C_and_C(c1=-0.9, c2=-0.8, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='min', RCi='Installed', alphai='14.0',Zc = 1, color='blue',mklabel=False)
		x2,y2 = self.SPT_plt( mxmni='min', RCi='Roof Cap Installed', alphai=15.0, Zc = 1, color='blue',mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='blue',mklabel=False)

		self.C_and_C(c1=0.6, c2=0.3, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='max', RCi='Installed', alphai='14.0',Zc = 2, color='red',label2use='Zone 2')
		x2,y2 = self.SPT_plt( mxmni='max', RCi='Roof Cap Installed', alphai=15.0, Zc = 2, color='red',mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='red',label2use='Polyfit Zone 2')

		self.C_and_C(c1=-1.7, c2=-1.2, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='min', RCi='Installed', alphai='14.0',Zc = 2, color='red',mklabel=False)
		x2,y2 = self.SPT_plt( mxmni='min', RCi='Roof Cap Installed', alphai=15.0, Zc = 2, color='red',mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='red',mklabel=False)

		self.C_and_C(c1=-2.6, c2=-2.0, mklabel=False) #zone ,3
		self.SPT_plt( mxmni='max', RCi='Roof Cap Installed', alphai=15.0, Zc = 3, color='green',label2use='Zone 3')
		self.SPT_plt( mxmni='min', RCi='Roof Cap Installed', alphai=15.0, Zc = 3, color='green',mklabel=False)

		self.mklegend()
		self.savefig()
		

		self.genfig(r'$\alpha=30$, Roof Cap Installed')
		self.C_and_C(c1=0.9, c2=0.8, label2use='C&C')
		x1,y1 = self.APT_plt(  mxmni='max', RCi='Installed', alphai='30.0',Zc = 1, color='blue', label2use='Zone 1')
		x2,y2 = self.SPT_plt( mxmni='max', RCi='Roof Cap Installed', alphai=30.0, Zc = 1, color='blue', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='blue', label2use='Polyfit Zone 1')

		self.C_and_C(c1=-1.0, c2=-0.8, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='min', RCi='Installed', alphai='30.0',Zc = 1, color='blue', mklabel=False)
		x2,y2 = self.SPT_plt( mxmni='min', RCi='Roof Cap Installed', alphai=30.0, Zc = 1, color='blue', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='blue', mklabel=False)

		self.C_and_C(c1=0.9, c2=0.8, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='max', RCi='Installed', alphai='30.0',Zc = 2, color='red', label2use='Zone 2')
		x2,y2 = self.SPT_plt( mxmni='max', RCi='Roof Cap Installed', alphai=30.0, Zc = 2, color='red', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='red', label2use='Polyfit Zone 2')

		self.C_and_C(c1=-1.2, c2=-1.0, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='min', RCi='Installed', alphai='30.0',Zc = 2, color='red', mklabel=False)
		x2,y2 = self.SPT_plt( mxmni='min', RCi='Roof Cap Installed', alphai=30.0, Zc = 2, color='red', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='red', mklabel=False)

		self.C_and_C(c1=-1.2, c2=-1.0, mklabel=False)
		self.SPT_plt( mxmni='max', RCi='Roof Cap Installed', alphai=30.0, Zc = 3, color='green', label2use='Zone 3')
		self.SPT_plt( mxmni='min', RCi='Roof Cap Installed', alphai=30.0, Zc = 3, color='green', mklabel=False)
		self.mklegend()
		self.savefig()
		

		self.genfig(r'$\alpha=45$, Roof Cap Installed')
		self.C_and_C(c1=0.9, c2=0.8, label2use='C&C')
		x1,y1 = self.APT_plt(  mxmni='max', RCi='Installed', alphai='45.0',Zc = 1, color='blue', label2use='Zone 1')
		x2,y2 = self.SPT_plt( mxmni='max', RCi='Roof Cap Installed', alphai=45.0, Zc = 1, color='blue', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='blue', label2use='Polyfit Zone 1')

		self.C_and_C(c1=-1.0, c2=-0.8, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='min', RCi='Installed', alphai='45.0',Zc = 1, color='blue', mklabel=False)
		x2,y2 = self.SPT_plt( mxmni='min', RCi='Roof Cap Installed', alphai=45.0, Zc = 1, color='blue', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='blue', mklabel=False)

		self.C_and_C(c1=0.9, c2=0.8, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='max', RCi='Installed', alphai='45.0',Zc = 2, color='red', label2use='Zone 2')
		x2,y2 = self.SPT_plt( mxmni='max', RCi='Roof Cap Installed', alphai=45.0, Zc = 2, color='red', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='red', label2use='Polyfit Zone 2')

		self.C_and_C(c1=-1.2, c2=-1.0, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='min', RCi='Installed', alphai='45.0',Zc = 2, color='red', mklabel=False)
		x2,y2 = self.SPT_plt( mxmni='min', RCi='Roof Cap Installed', alphai=45.0, Zc = 2, color='red', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='red', mklabel=False)

		self.C_and_C(c1=-1.2, c2=-1.0, mklabel=False)
		self.SPT_plt( mxmni='max', RCi='Roof Cap Installed', alphai=45.0, Zc = 3, color='green', label2use='Zone 3')
		self.SPT_plt( mxmni='min', RCi='Roof Cap Installed', alphai=45.0, Zc = 3, color='green', mklabel=False)
		self.mklegend()
		self.savefig()
		self.closepdf()
		#"""

		self.initializepdf('mxmnRCNI.pdf')
		self.genfig(r'$\alpha=15$, Roof Cap Not Installed')

		self.C_and_C(c1=0.6, c2=0.3, label2use='C&C')
		x1,y1 = self.APT_plt(  mxmni='max', RCi='Not Installed', alphai='14.0',Zc = 1, color='blue', label2use='Zone 1')
		x2,y2 = self.SPT_plt( mxmni='max', RCi='Roof Cap Not Installed', alphai=15.0, Zc = 1, color='blue', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='blue', label2use='Polyfit Zone 1')

		self.C_and_C(c1=-0.9, c2=-0.8, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='min', RCi='Not Installed', alphai='14.0',Zc = 1, color='blue', mklabel=False)
		x2,y2 = self.SPT_plt( mxmni='min', RCi='Roof Cap Not Installed', alphai=15.0, Zc = 1, color='blue', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='blue', mklabel=False)

		self.C_and_C(c1=0.6, c2=0.3, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='max', RCi='Not Installed', alphai='14.0',Zc = 2, color='red', label2use='Zone 2')
		x2,y2 = self.SPT_plt( mxmni='max', RCi='Roof Cap Not Installed', alphai=15.0, Zc = 2, color='red', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='red', label2use='Polyfit Zone 2')

		self.C_and_C(c1=-1.7, c2=-1.2, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='min', RCi='Not Installed', alphai='14.0',Zc = 2, color='red', mklabel=False)
		x2,y2 = self.SPT_plt( mxmni='min', RCi='Roof Cap Not Installed', alphai=15.0, Zc = 2, color='red', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='red', mklabel=False)

		
		self.SPT_plt( mxmni='max', RCi='Roof Cap Not Installed', alphai=15.0, Zc = 3, color='green', label2use='Zone 3')
		self.SPT_plt( mxmni='min', RCi='Roof Cap Not Installed', alphai=15.0, Zc = 3, color='green', mklabel=False)
		self.mklegend()
		self.savefig()
		

		self.genfig(r'$\alpha=30$, Roof Cap Not Installed')
		self.C_and_C(c1=0.9, c2=0.8, label2use='C&C')
		x1,y1 = self.APT_plt(  mxmni='max', RCi='Not Installed', alphai='30.0',Zc = 1, color='blue', label2use='Zone 1')
		x2,y2 = self.SPT_plt( mxmni='max', RCi='Roof Cap Not Installed', alphai=30.0, Zc = 1, color='blue', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='blue',label2use='Polyfit Zone 1')

		self.C_and_C(c1=-1.0, c2=-0.8, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='min', RCi='Not Installed', alphai='30.0',Zc = 1, color='blue', mklabel=False)
		x2,y2 = self.SPT_plt( mxmni='min', RCi='Roof Cap Not Installed', alphai=30.0, Zc = 1, color='blue', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='blue', mklabel=False)

		self.C_and_C(c1=0.9, c2=0.8, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='max', RCi='Not Installed', alphai='30.0',Zc = 2, color='red', label2use='Zone 2')
		x2,y2 = self.SPT_plt( mxmni='max', RCi='Roof Cap Not Installed', alphai=30.0, Zc = 2, color='red', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='red', label2use='Polyfit Zone 2')

		self.C_and_C(c1=-1.2, c2=-1.0, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='min', RCi='Not Installed', alphai='30.0',Zc = 2, color='red', mklabel=False)
		x2,y2 = self.SPT_plt( mxmni='min', RCi='Roof Cap Not Installed', alphai=30.0, Zc = 2, color='red', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='red', mklabel=False)

		
		self.SPT_plt( mxmni='max', RCi='Roof Cap Not Installed', alphai=30.0, Zc = 3, color='green', label2use='Zone 3')
		self.SPT_plt( mxmni='min', RCi='Roof Cap Not Installed', alphai=30.0, Zc = 3, color='green', mklabel=False)
		self.mklegend()
		self.savefig()
		

		self.genfig(r'$\alpha=45$, Roof Cap Not Installed')
		self.C_and_C(c1=0.9, c2=0.8, label2use='C&C')
		x1,y1 = self.APT_plt(  mxmni='max', RCi='Not Installed', alphai='45.0',Zc = 1, color='blue', label2use='Zone 1')
		x2,y2 = self.SPT_plt( mxmni='max', RCi='Roof Cap Not Installed', alphai=45.0, Zc = 1, color='blue', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='blue', label2use='Polyfit Zone 1')

		self.C_and_C(c1=-1.0, c2=-0.8, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='min', RCi='Not Installed', alphai='45.0',Zc = 1, color='blue', mklabel=False)
		x2,y2 = self.SPT_plt( mxmni='min', RCi='Roof Cap Not Installed', alphai=45.0, Zc = 1, color='blue', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='blue', mklabel=False)

		self.C_and_C(c1=0.9, c2=0.8, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='max', RCi='Not Installed', alphai='45.0',Zc = 2, color='red', label2use='Zone 2')
		x2,y2 = self.SPT_plt( mxmni='max', RCi='Roof Cap Not Installed', alphai=45.0, Zc = 2, color='red', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='red', label2use='Polyfit Zone 2')

		self.C_and_C(c1=-1.2, c2=-1.0, mklabel=False)
		x1,y1 = self.APT_plt(  mxmni='min', RCi='Not Installed', alphai='45.0',Zc = 2, color='red', mklabel=False)
		x2,y2 = self.SPT_plt( mxmni='min', RCi='Roof Cap Not Installed', alphai=45.0, Zc = 2, color='red', mklabel=False)
		self.fit( x1 + x2, y1 + y2, color='red', mklabel=False)

		self.SPT_plt( mxmni='max', RCi='Roof Cap Not Installed', alphai=45.0, Zc = 3, color='green', label2use='Zone 3')
		self.SPT_plt( mxmni='min', RCi='Roof Cap Not Installed', alphai=45.0, Zc = 3, color='green', mklabel=False)
		self.mklegend()
		self.savefig()
		self.closepdf()
		

		

		







	def sepratemxmn(self):
		self.initializepdf('mx.pdf')
		self.genfig()
		self.APT_plt( c1=0.6, c2=0.3, mxmni='max', RCi='Installed', alphai='14.0',Zc = 1)
		self.APT_plt( c1=0.6, c2=0.3, mxmni='max', RCi='Installed', alphai='14.0',Zc = 2)
		self.savefig()

		self.genfig()
		self.APT_plt( c1=0.9, c2=0.8, mxmni='max', RCi='Installed', alphai='30.0',Zc = 1)
		self.APT_plt( c1=0.9, c2=0.8, mxmni='max', RCi='Installed', alphai='30.0',Zc = 2)
		self.savefig()

		self.genfig()
		self.APT_plt( c1=0.9, c2=0.8, mxmni='max', RCi='Installed', alphai='45.0',Zc = 1)
		self.APT_plt( c1=0.9, c2=0.8, mxmni='max', RCi='Installed', alphai='45.0',Zc = 2)
		self.savefig()
		self.closepdf()


		self.initializepdf('mn.pdf')
		self.genfig()
		self.APT_plt( c1=-0.9, c2=-0.8, mxmni='min', RCi='Installed', alphai='14.0',Zc = 1)
		self.APT_plt( c1=-1.7, c2=-1.2, mxmni='min', RCi='Installed', alphai='14.0',Zc = 2)
		self.savefig()

		self.genfig()
		self.APT_plt( c1=-1.0, c2=-0.8, mxmni='min', RCi='Installed', alphai='30.0',Zc = 1)
		self.APT_plt( c1=-1.2, c2=-1.0, mxmni='min', RCi='Installed', alphai='30.0',Zc = 2)
		self.savefig()

		self.genfig()
		self.APT_plt( c1=-1.0, c2=-0.8, mxmni='min', RCi='Installed', alphai='45.0',Zc = 1)
		self.APT_plt( c1=-1.2, c2=-1.0, mxmni='min', RCi='Installed', alphai='45.0',Zc = 2)
		self.savefig()
		self.closepdf()

		self.initializepdf('mxRCNI.pdf')
		self.genfig()
		self.APT_plt( c1=0.6, c2=0.3, mxmni='max', RCi='Not Installed', alphai='14.0',Zc = 1)
		self.APT_plt( c1=0.6, c2=0.3, mxmni='max', RCi='Not Installed', alphai='14.0',Zc = 2)
		self.savefig()

		self.genfig()
		self.APT_plt( c1=0.9, c2=0.8, mxmni='max', RCi='Not Installed', alphai='30.0',Zc = 1)
		self.APT_plt( c1=0.9, c2=0.8, mxmni='max', RCi='Not Installed', alphai='30.0',Zc = 2)
		self.savefig()

		self.genfig()
		self.APT_plt( c1=0.9, c2=0.8, mxmni='max', RCi='Not Installed', alphai='45.0',Zc = 1)
		self.APT_plt( c1=0.9, c2=0.8, mxmni='max', RCi='Not Installed', alphai='45.0',Zc = 2)
		self.savefig()
		self.closepdf()


		self.initializepdf('mnRCNI.pdf')
		self.genfig()
		self.APT_plt( c1=-0.9, c2=-0.8, mxmni='min', RCi='Not Installed', alphai='14.0',Zc = 1)
		self.APT_plt( c1=-1.7, c2=-1.2, mxmni='min', RCi='Not Installed', alphai='14.0',Zc = 2)
		self.savefig()

		self.genfig()
		self.APT_plt( c1=-1.0, c2=-0.8, mxmni='min', RCi='Not Installed', alphai='30.0',Zc = 1)
		self.APT_plt( c1=-1.2, c2=-1.0, mxmni='min', RCi='Not Installed', alphai='30.0',Zc = 2)
		self.savefig()

		self.genfig()
		self.APT_plt( c1=-1.0, c2=-0.8, mxmni='min', RCi='Not Installed', alphai='45.0',Zc = 1)
		self.APT_plt( c1=-1.2, c2=-1.0, mxmni='min', RCi='Not Installed', alphai='45.0',Zc = 2)
		self.savefig()
		self.closepdf()	



	def initializepdf(self, pdfname = 'pdf1.pdf'):
		import classes.classes
		
		#make practice pdf
		self.pdf1=classes.classes.Plotter(self.ALL)
		self.pdf1.makepdf(pdfname)


	def genfig(self,title):
		# generate figure
		self.pdf1.genfig(title)

	def savefig(self):
		# save the figure
		self.pdf1.svfig()	

	def closepdf(self):
		self.pdf1.clpdf()

	def C_and_C(self, c1=0.9, c2=0.8,mklabel=True,label2use='line'):
		# add C and C line to the figure
		self.pdf1.pltCandC(c1,c2,'black',mklabel,label2use)

	def APT_plt(self, mxmni='max', RCi='Installed', alphai='14.0', Zc = 1,color = 'b',mklabel=True,label2use='line'):




		# filter the data
		filterobj=Datafilter_APT(self.ALL, mxmni, RCi, alphai)

		# perform zone filter
		filterobj.zfilter(Zc)

		x,y=filterobj.getzfxy()
		#plot the filtered data
		self.pdf1.WTD(x,y,color,mklabel,label2use)

		return x,y
		
		

	def SPT_plt(self, mxmni='max', RCi='Roof Cap Installed', alphai=15.0, Zc = 1, color = 'b',mklabel=True,label2use='line'):
		filterobj=Datafilter_SPT(self.ALL, mxmni, RCi, alphai)
		# perform zone filter
		filterobj.zfilter(Zc)

		x,y=filterobj.getzfxy()
		#plot the filtered data
		self.pdf1.WTD(x,y,color,mklabel,label2use)

		return x,y

	def fit(self,x,y,color = 'b',mklabel=True,label2use='line'):
		# plot fit line
		self.pdf1.WTDfit(x,y,color,mklabel,label2use)

	def mklegend(self,*args):
		self.pdf1.mklegend(*args)



class Datafilter_SPT(object):
	"""
	within the Plotting action class, 
	this is responsible for filtering 
	the data from the ALL data structure 
	and returning an object of reduced size.
	"""

	def __init__(self,ALL,mxmni='max',RCi='Roof Cap Installed',alphai=15.0):
		self.x = []
		self.y = []
		self.f_ele = {}
		i = 0
		for x1 in range(len(ALL.SP_ele_mod1)):
			o=ALL.SP_ele_mod1[x1]
			if o.mxmn==mxmni: 
				if o.RC==RCi: 
					if o.alpha==alphai: 
						self.f_ele[i] = o
						i = i+1
	def zfilter(self,Zc):
		if Zc==1:
			i=0
			self.zf_ele = {}
			for x1 in range(len(self.f_ele)):
				v1 = self.f_ele[x1].w1n
				v2 = self.f_ele[x1].w2n
				v3 = self.f_ele[x1].w3n
				maxval = max(v1,v2,v3)
				if maxval==v1:
					self.zf_ele[i] = self.f_ele[x1]
					i = i + 1
		if Zc==2:
			i=0
			self.zf_ele = {}
			for x1 in range(len(self.f_ele)):
				v1 = self.f_ele[x1].w1n
				v2 = self.f_ele[x1].w2n
				v3 = self.f_ele[x1].w3n
				maxval = max(v1,v2,v3)
				if maxval==v2:
					self.zf_ele[i] = self.f_ele[x1]
					i = i + 1
		if Zc==3:
			i=0
			self.zf_ele = {}
			for x1 in range(len(self.f_ele)):
				v1 = self.f_ele[x1].w1n
				v2 = self.f_ele[x1].w2n
				v3 = self.f_ele[x1].w3n
				maxval = max(v1,v2,v3)
				if maxval==v3:
					self.zf_ele[i] = self.f_ele[x1]
					i = i + 1


	def getxy(self):
		x = []
		y = []
		for x1 in range(len(self.f_ele)):
			y.append(self.f_ele[x1].GCp)
			x.append(self.f_ele[x1].AT)

		return x,y

	def getzfxy(self):
		x = []
		y = []
		for x1 in range(len(self.zf_ele)):
			y.append(self.zf_ele[x1].GCp)
			x.append(self.zf_ele[x1].AT)

		return x,y

class Datafilter_APT(object):
	"""
	within the Plotting action class, 
	this is responsible for filtering 
	the data from the ALL data structure 
	and returning an object of reduced size.
	"""

	def __init__(self,ALL,mxmni='max',RCi='Installed',alphai='14.0'):
		self.x = []
		self.y = []
		self.f_ele = {}
		i = 0
		for x1 in range(len(ALL.APT_ele_mod2)):
			o=ALL.APT_ele_mod2[x1]
			if o.mxmn==mxmni: 
				if o.RC==RCi: 
					if o.alpha==alphai: 
						self.f_ele[i] = o
						i = i+1
	def zfilter(self,Zc):
		if Zc==1:
			i=0
			self.zf_ele = {}
			for x1 in range(len(self.f_ele)):
				v1 = self.f_ele[x1].w1n
				v2 = self.f_ele[x1].w2n
				v3 = self.f_ele[x1].w3n
				maxval = max(v1,v2,v3)
				if maxval==v1:
					self.zf_ele[i] = self.f_ele[x1]
					i = i + 1
		if Zc==2:
			i=0
			self.zf_ele = {}
			for x1 in range(len(self.f_ele)):
				v1 = self.f_ele[x1].w1n
				v2 = self.f_ele[x1].w2n
				v3 = self.f_ele[x1].w3n
				maxval = max(v1,v2,v3)
				if maxval==v2:
					self.zf_ele[i] = self.f_ele[x1]
					i = i + 1
		if Zc==3:
			i=0
			self.zf_ele = {}
			for x1 in range(len(self.f_ele)):
				v1 = self.f_ele[x1].w1n
				v2 = self.f_ele[x1].w2n
				v3 = self.f_ele[x1].w3n
				maxval = max(v1,v2,v3)
				if maxval==v3:
					self.zf_ele[i] = self.f_ele[x1]
					i = i + 1


	def getxy(self):
		x = []
		y = []
		for x1 in range(len(self.f_ele)):
			y.append(self.f_ele[x1].GCp)
			x.append(self.f_ele[x1].AT)

		return x,y

	def getzfxy(self):
		x = []
		y = []
		for x1 in range(len(self.zf_ele)):
			y.append(self.zf_ele[x1].GCp)
			x.append(self.zf_ele[x1].AT)

		return x,y





		