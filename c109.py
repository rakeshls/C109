import random
import statistics
import plotly.figure_factory as ff
dice_result = []
for result in range(0,1000):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    dice_result.append(d1+d2)
mean = sum(dice_result)/len(dice_result)
mode = statistics.mode(dice_result)
median = statistics.median(dice_result)
stDev = statistics.stdev(dice_result)
print(mean)
print(median)
print(mode)
print(stDev)
#print('{}% of data',fromate(len(list_of_data)))
fig = ff.create_distplot([dice_result],['results'],show_hist = False)
fig.show()