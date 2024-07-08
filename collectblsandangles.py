import math
geomfile = open("dyn.xyz").readlines()
gCatzero = geomfile[2]
gCatzero_list = gCatzero.split()
gOatzero = geomfile[3]
gOatzero_list = gOatzero.split()

#defining unit vector along CO at time=0fs

#vector components along x,y,z at t=0fs
ux = float(gCatzero_list[1]) - float(gOatzero_list[1])
uy = float(gCatzero_list[2]) - float(gOatzero_list[2])
uz = float(gCatzero_list[3]) - float(gOatzero_list[3])

#magnitude of vector at t=0fs along CO
u = ((ux**2.0) + (uy**2.0) + (uz**2.0))**(0.5)

#x,y,z of unitvector
ix = ux/u
iy = uy/u
iz = uz/u


alist = [] #list conatining lines
blist = []  #list consisting numbers of lines
linea = 0  #to count number of lines

with open("dyn.xyz",'r') as filea:
	for line in filea:
		alist.append(line)
		blist.append(linea)
		linea += 1
j = 2
k = 3
m = 1
n = 4
o = 5
thetalist = []
timelist = []
cdd_diff = []
COlist = []
CD1list = []
CD2list = []
cdddifflist = []
thetaocd1list = []
thetaocd2list = []
deltathetalist = []
thetacd1wrtinitcolist = []
thetacd2wrtinitcolist = []
# The list of the difference in between angles of initial OC-D1 and initial OC-D2
anglediff_list = []
dihedralocd_list = []
dihedralout_list = []

for l in range(1,len(blist)+1):
	if j <= len(blist) and k <= len(blist):
		#CO bond length, the below 3 will also be used for plane
		vx = float(alist[j].split()[1]) - float(alist[k].split()[1])
		vy = float(alist[j].split()[2]) - float(alist[k].split()[2])
		vz = float(alist[j].split()[3]) - float(alist[k].split()[3])
		v = ((vx**2.0) + (vy**2.0) + (vz**2.0))**(0.5)
		#unit vectors along CO
		iix = vx/v
		iiy = vy/v
		iiz = vz/v
		COlist.append(v)
		#CD1 bond length, the below 3 will also be used for plane
		cd1x = (float(alist[j].split()[1]) - float(alist[n].split()[1]))
                cd1y = (float(alist[j].split()[2]) - float(alist[n].split()[2]))
                cd1z = (float(alist[j].split()[3]) - float(alist[n].split()[3]))
		cd1 = ((cd1x**2.0) + (cd1y**2.0) + (cd1z**2.0))**(0.5)
		cd1ix = cd1x/cd1
		cd1iy = cd1y/cd1
		cd1iz  = cd1z/cd1
		CD1list.append(cd1)
		#OD1 for ODD plane normal
                od1x = (float(alist[k].split()[1]) - float(alist[n].split()[1]))
                od1y = (float(alist[k].split()[2]) - float(alist[n].split()[2]))
                od1z = (float(alist[k].split()[3]) - float(alist[n].split()[3]))
                od1 = ((od1x**2.0) + (od1y**2.0) + (od1z**2.0))**(0.5)
		#CD2 bond length, the below 3 will also be used for plane
		cd2x = (float(alist[j].split()[1]) - float(alist[o].split()[1]))
                cd2y = (float(alist[j].split()[2]) - float(alist[o].split()[2]))
                cd2z = (float(alist[j].split()[3]) - float(alist[o].split()[3]))
		cd2 = ((cd2x**2.0) + (cd2y**2.0) + (cd2z**2.0))**(0.5)
                cd2ix = cd2x/cd2
                cd2iy = cd2y/cd2
                cd2iz  = cd2z/cd2
		CD2list.append(cd2)
		#OD2 for ODD plane normal
                od2x = (float(alist[k].split()[1]) - float(alist[o].split()[1]))
                od2y = (float(alist[k].split()[2]) - float(alist[o].split()[2]))
                od2z = (float(alist[k].split()[3]) - float(alist[o].split()[3]))
                od2 = ((od2x**2.0) + (od2y**2.0) + (od2z**2.0))**(0.5) 
		#CD1 - CD2
		cd1d2 = abs(cd2 - cd1)
		cdddifflist.append(cd1d2)
		#ANgle O-C-D1
		thetaocd1 = (math.acos(((iix*cd1ix)+(iiy*cd1iy)+(iiz*cd1iz))/(1.0*1.0)))*(180.0/3.141593)
		thetaocd1list.append(thetaocd1)
		#ANgle O-C-D1 wrt initial CO vector
		thetacd1wrtinitco = (math.acos(((ix*cd1ix)+(iy*cd1iy)+(iz*cd1iz))/(1.0*1.0)))*(180.0/3.141593)
		thetacd1wrtinitcolist.append(thetacd1wrtinitco)
		#Angle O-C-D2
		thetaocd2 = (math.acos(((iix*cd2ix)+(iiy*cd2iy)+(iiz*cd2iz))/(1.0*1.0)))*(180.0/3.141593)
		thetaocd2list.append(thetaocd2)
		#ANgle O-C-D2 wrt initial CO vector
                thetacd2wrtinitco = (math.acos(((ix*cd2ix)+(iy*cd2iy)+(iz*cd2iz))/(1.0*1.0)))*(180.0/3.141593)
                thetacd2wrtinitcolist.append(thetacd2wrtinitco)
		# OCD1 - OCD2
		deltatheta = abs(thetaocd2 - thetaocd1)
		deltathetalist.append(deltatheta)
		#Angle differnce wrt initial CO vector
		angle_diff = abs(thetacd2wrtinitco - thetacd1wrtinitco)
		anglediff_list.append(angle_diff)
		#normal vector of OCD1
		plncod1x = (vy*cd1z)-(vz*cd1y)
		plncod1y = (vz*cd1x)-(vx*cd1z)
		plncod1z = (vx*cd1y)-(vy*cd1x)
		plncod1 = ((plncod1x**2.0)+(plncod1y**2.0)+(plncod1z**2.0))**0.5
		#normal vector of OCD2
                plncod2x = (vy*cd2z)-(vz*cd2y)
                plncod2y = (vz*cd2x)-(vx*cd2z)
                plncod2z = (vx*cd2y)-(vy*cd2x)
		plncod2 = ((plncod2x**2.0)+(plncod2y**2.0)+(plncod2z**2.0))**0.5
		#normal vector of CDD
                plncddx = (cd1y*cd2z)-(cd1z*cd2y)
                plncddy = (cd1z*cd2x)-(cd1x*cd2z)
                plncddz = (cd1x*cd2y)-(cd1y*cd2x)
                plncdd = ((plncddx**2.0)+(plncddy**2.0)+(plncddz**2.0))**0.5
		#normal vector of ODD
                plnoddx = (od1y*od2z)-(od1z*od2y)
                plnoddy = (od1z*od2x)-(od1x*od2z)
                plnoddz = (od1x*od2y)-(od1y*od2x)
                plnodd = ((plnoddx**2.0)+(plnoddy**2.0)+(plnoddz**2.0))**0.5
		# angle between normals of planes
		dihedralocd = (math.acos(((plncod1x*plncod2x)+(plncod1y*plncod2y)+(plncod1z*plncod2z))/(plncod1*plncod2)))*(180.0/3.141593)
		dihedralocd_list.append(180.0-dihedralocd)
		dihedralcdd_odd = (math.acos(((plncddx*plnoddx)+(plncddy*plnoddy)+(plncddz*plnoddz))/(plncdd*plnodd)))*(180.0/3.141593)
                dihedralout_list.append(dihedralcdd_odd)
		#Timelist
		time = alist[m].split()[2]
                timelist.append(time)
		#Angle of CO wrt CO vector at t=0fs
		if ux == vx and uy == vy and uz == vz :
			theta = 0.0
                        thetalist.append(theta)
		else:
			theta = (math.acos(((ix*iix)+(iy*iiy)+(iz*iiz))/(1.0*1.0)))*(180.0/3.141593)
			thetalist.append(theta)
		m = m + 6
		k = k + 6
		j = j + 6
		n = n + 6
		o = o + 6
		l += 1

#print(thetacd1wrtinitcolist)

#for p in range(0,len(timelist)):
#	if float(timelist[p]) < 30.0 :
#		cd1x = (float(alist[2].split()[1]) - float(alist[n].split()[1]))	
#		cd1y = (float(alist[2].split()[2]) - float(alist[n].split()[2]))
#		cd1z = (float(alist[2].split()[3]) - float(alist[n].split()[3]))
#		cd1 = ((cd1x**2.0) + (cd1y**2.0) + (cd1z**2.0))**0.5
#		# unit vectors along CD1
#		cd1ix = cd1x/cd1
#		cd1iy = cd1y/cd1
#		cd1iz = cd1z/cd1
		# angle of CD1 with initial axis along C=O
#                thetacd1 = (math.acos(((ux*cd1ix)+(uy*cd1iy)+(uz*cd1iz))/(u*cd1)))*(180.0/3.141593)
#                thetacd1list.append(thetacd1)
#		cd2x = (float(alist[2].split()[1]) - float(alist[o].split()[1]))
 #               cd2y = (float(alist[2].split()[2]) - float(alist[o].split()[2]))
#               cd2z = (float(alist[2].split()[3]) - float(alist[o].split()[3]))
 #               cd2 = ((cd2x**2.0) + (cd2y**2.0) + (cd2z**2.0))**0.5
		# unit vectors along CD2
 #               cd2ix = cd2x/cd2
 #               cd2iy = cd2y/cd2
 #               cd2iz = cd2z/cd2
		# angle of CD2 with initial axis along C=O 
#		thetacd2 = (math.acos(((ux*cd2ix)+(uy*cd2iy)+(uz*cd2iz))/(u*cd2)))*(180.0/3.141593)
#		thetacd2list.append(thetacd2)
#		angle_diff = abs(thetacd1 - thetacd2)
#		cdd = abs(cd1 - cd2)
#		time = alist[m].split()[2]
 #               timelist.append(time)
#		p += 1
#		n = n + 6
#		o = o + 6
#		r = r + 6
#		cdd_diff.append(cdd)
#		anglediff_list.append(angle_diff)		
#		time = alist[m].split()[2]
#                timelist.append(time)


with  open("intcoors.txt",'w') as fileb:
	for n in range(0,len(timelist)):	
		fileb.write("{0}  {1:5f}  {2:5f}  {3:5f}  {4:5f}  {5:5f}  {6:5f}\n".format(timelist[n],COlist[n],CD1list[n],CD2list[n],thetaocd1list[n],thetaocd2list[n],dihedralocd_list[n]))
		n += 1

add = 0.0
add1 = 0.0
add2 = 0.0
add3 = 0.0
add4 = 0.0
#print(anglediff_list)

with open("anglecorrelation.txt",'w') as filee:
        for q in range(0,len(timelist)):
                if float(timelist[q]) < 11.0:
                        add = add + cdddifflist[q]
                        add1 = add1 + anglediff_list[q]
                        add2 = add2 + deltathetalist[q]
                        add3 = add3 + dihedralocd_list[q]
			add4 = add4 + dihedralout_list[q]
                	mean_cdd = add/(q+1)
                	mean_angdiffwrtinitco = add1/(q+1)
                	mean_angdiff = add2/(q+1)
                	mean_dihedralocd = add3/(q+1)
			mean_dihedralout = add4/(q+1)
                	filee.write("{0}  {1:5f}  {2:5f}  {3:5f}  {4:5f}  {5:5f}  {6:5f} \n".format(timelist[q],thetalist[q],mean_cdd,mean_angdiff,mean_angdiffwrtinitco,mean_dihedralocd,mean_dihedralout))
                	q += 1

#listc = []
#liste = []
#linenumb = 0

#Perpendicular velocities of C and O at 0.5 fs
#with open("veloc05.txt",'r') as filef:
#        for line in filef:
#		listc.append(line)
#		liste.append(linenumb)
#		linenumb += 1
#CO vecor 0.5 fs
#vvx = float(alist[8].split()[1]) - float(alist[9].split()[1])
#vvy = float(alist[8].split()[2]) - float(alist[9].split()[2]) 
#vvz = float(alist[8].split()[3]) - float(alist[9].split()[3]) 
#vv = ((vvx**2.0) + (vvy**2.0) + (vvz**2.0))**(0.5)
#unit vectors along CO at 0.5 fs
#vix = vvx/vv
#viy = vvy/vv
#viz = vvz/vv

#velocity vector of C at 0.5 fs
#vcx = float(listc[1].split()[0])
#vcy = float(listc[1].split()[1])
#vcz = float(listc[1].split()[2])
#vc = ((vcx**2.0) + (vcy**2.0) + (vcz**2.0))**(0.5)
#unit vectors of veloc of C at 0.5 fs
#vcix = vcx/vc
#vciy = vcy/vc
#vciz = vcz/vc

#velocity vector of O at 0.5 fs
#vox = float(listc[2].split()[0])
#voy = float(listc[2].split()[1])
#voz = float(listc[2].split()[2])
#vo = ((vox**2.0) + (voy**2.0) + (voz**2.0))**(0.5)
#unit vectors of veloc of O at 0.5 fs
#voix = vox/vo
#voiy = voy/vo
#voiz = voz/vo

#angleperpC = (math.asin(((vcix*vix)+(vciy*viy)+(vciz*viz))/(1.0*1.0)))*(180.0/3.141593)
#angleperpO = (math.asin(((voix*vix)+(voiy*viy)+(voiz*viz))/(1.0*1.0)))*(180.0/3.141593)

#vcperp = vc*math.sin(angleperpC)
#voperp = vo*math.sin(angleperpO)


#with open("perpveloc.txt",'w') as fileg:
#	fileg.write("0.5  {0:5f}\n".format(voperp-vcperp))
	
