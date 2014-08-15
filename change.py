#script for converting ww3 json to js object for waver site
import sys, time, os, string

#not using json 
#import json
#data = json.load(infile);

workspace = "C:\projects\\waver\\data\\";
asciiData = workspace + "wave_northamerica_sm.js";

#from http://oos.soest.hawaii.edu/erddap/griddap/NWW3_Global_Best.json?Thgt[(2014-08-13):6:(2014-08-15)][(0.0):1:(0.0)][(-67.5):1:(76.5)][(10):1:(350)]
infile = open("C:\\projects\\waver\\data\\northamerica2.txt");

inlines = infile.readlines();
infile.close();
newfile = open(asciiData,'w');
newfile.write('var wavepts0 = [');

#take first index
timestep = 1;
datapoints = 0;
currentDate = inlines[0].split(',')[0].strip();

for line in inlines:
	valuelist = line.split(',');
	#make sure the json header is chopped off
	nullchecker= valuelist[4];
	valnul = "null";
	
	if nullchecker.find(valnul,0) ==1:
		print 'nodata'

	else:
		#seperate dates into different objects
		if valuelist[0].strip() == currentDate:
			newfile.write(valuelist[0].strip()+','+valuelist[2].strip()+','+str(float(valuelist[3])-360)+','+valuelist[4].replace("\\n","").strip());
			newfile.write(',');
			datapoints = datapoints+1;
		else:
			datapoints = 0;
			currentDate = valuelist[0].strip();
			newfile.seek(-1, os.SEEK_END);
			newfile.truncate();
			newfile.write('];');
			newfile.write('\n var wavepts'+str(timestep)+' = [');
			timestep=timestep+1;
			newfile.write(valuelist[0].strip()+','+valuelist[2].strip()+','+str(float(valuelist[3])-360)+','+valuelist[4].replace("\\n","").strip());
			newfile.write(',');

print timestep;
print datapoints;
#truncate the last comma
newfile.seek(-1, os.SEEK_END);
newfile.truncate();
newfile.write('];');
newfile.close();
sys.exit();
