import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
df =  pd.read_csv('height-weight.csv')
data_height = df['Height(Inches)'].tolist()
data_weight = df['Weight(Pounds)'].tolist()
mean_height = statistics.mean(data_height)
mean_weight = statistics.mean(data_weight)
mode_height = statistics.mode(data_height)
mode_weight = statistics.mode(data_weight)
median_height = statistics.median(data_height)
median_weight = statistics.median(data_weight)
stDev_height = statistics.stdev(data_height)
stDev_weight = statistics.stdev(data_weight)
print('mean of height is {}'.format(mean_height))
first_stdev_start = mean_height - stDev_height
first_stdev_end = mean_height + stDev_height
height_listOfData1 = [result for result in data_height if result > first_stdev_start and result < first_stdev_end]
print('{}% of data height'.format(len(height_listOfData1)*100/len(data_height)))
second_stdev_start = mean_height - (2*stDev_height)
second_stdev_end = mean_height +(2*stDev_height)
height_listOfData2 = [result for result in data_height if result > second_stdev_start and result < second_stdev_end]
print('{}% of data height'.format(len(height_listOfData2)*100/len(data_height)))
third_stdev_start = mean_height - (3*stDev_height)
third_stdev_end = mean_height +(3*stDev_height)
height_listOfData3 = [result for result in data_height if result > third_stdev_start and result < third_stdev_end]
print('{}% of data height'.format(len(height_listOfData3)*100/len(data_height)))
print('mean of weight is {}'.format(mean_weight))
first_stdev_start_weight = mean_weight - stDev_weight
first_stdev_end_weight = mean_weight + stDev_weight
weight_listOfData1 = [result for result in data_weight if result > first_stdev_start_weight and result < first_stdev_end_weight]
print('{}% of data weight'.format(len(weight_listOfData1)*100/len(data_weight)))
second_stdev_start_weight = mean_weight - (2*stDev_weight)
second_stdev_end_weight = mean_weight +(2*stDev_weight)
weight_listOfData2 = [result for result in data_weight if result > second_stdev_start_weight and result < second_stdev_end_weight]
print('{}% of data weight'.format(len(weight_listOfData2)*100/len(data_weight)))
third_stdev_start_weight = mean_weight - (3*stDev_weight)
third_stdev_end_weight = mean_weight +(3*stDev_weight)
weight_listOfData3 = [result for result in data_weight if result > third_stdev_start_weight and result < third_stdev_end_weight]
print('{}% of data weight'.format(len(weight_listOfData3)*100/len(data_weight)))
