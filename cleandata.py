import pandas as pd
filename = "Well2A3mths.csv"
cchs = pd.read_csv("Data/"+filename, low_memory=False)
subset_1 = cchs.drop(["Id","TimeStamp", "Downhole Gauge Fluid Level above Downhole Sensor (estimated)", 
	"Downhole Gauge Fluid Level from Surface (estimated)",
	"Downhole Gauge Pressure Average Yesterday",
	"Downhole Gauge Sensor Depth from Rotary Table",
	"Downhole Gauge Temperature","Downhole Gauge Temperature Averge Yesterday",
	"WEC PCP Efficiency Alarm", "WEC PCP Theoretical Pump Displacement", "WEC Pump Trip", 
	"WEC Slow pump to min speed command", "PIIntTSTicks", "PIIntShapeID", 
	filename[4] + filename[5], "Wellhead State", "VSD Mode", "Wellhead Flow Configuration",
	"Downhole Gauge Type", "Tubing Size Type", "Wellhead Type"], axis = 1);
subset_1['act cap'] = 120.1
subset_1['max cap'] = 9000
subset_1['depth'] = 582.0
subset_1.to_csv('Cleaned Data/clean_' + filename)
