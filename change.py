#script for converting ww3 json to js object for waver site
import sys, time, os, string

#not using json 
#import json
#data = json.load(infile);

workspace = "C:\projects\\waver\\data\\";
asciiData = workspace + "wave_new-ec.js";

#from http://oos.soest.hawaii.edu/erddap/griddap/NWW3_Global_Best.json?Thgt[(2014-08-13):6:(2014-08-15)][(0.0):1:(0.0)][(-67.5):1:(76.5)][(10):1:(350)]
infile = open("C:\projects\waver\data\eastcoast.txt");

inlines = infile.readlines();
infile.close();
newfile = open(asciiData,'w');
newfile.write('var wavepts = [');


for line in inlines:
	valuelist = line.split(',');
	nullchecker= valuelist[4];
	val = "null";
	
	if nullchecker.find('null',0) ==1:
		print ''

	else:
		newfile.write(valuelist[0].strip()+','+valuelist[2].strip()+','+str(float(valuelist[3])-180)+','+valuelist[4].replace("\\n","").strip());
		newfile.write(',');

newfile.write('];');
newfile.close();
sys.exit();
