import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import scipy
import tolist
marks_result.append( ('math score').tolist+('reading score').tolist+('writing score').tolist)

#mean & standard deviation
mean = sum(marks_result) / len(dice_result)
print("Mean : " ,  mean)
stddev = statistics.stdev(marks_result)
print("Standard deviation" , stddev)
median = statistics.median(marks_result)
mode = statistics.mode(marks_result)
print('Median : ' , median)
print('Mode : ' , mode)

#Properties of Normal distribution
'''
1. Mean = Median = Mode
'''



first_stddev_start ,first_stddev_end = mean- stddev , mean + stddev
second_stddev_start ,second_stddev_end = mean- (2*stddev) , mean + (2*stddev)
third_stddev_start ,third_stddev_end = mean- (3*stddev) , mean + (3*stddev)

fig = ff.create_distplot([dice_result] , ["Result"] , show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y= [0,0.17] , mode = 'lines' , name = 'MEAN'))
fig.add_trace(go.Scatter(x = [first_stddev_start, first_stddev_start], y= [0,0.17] , mode = 'lines' , name='STANDARD DEVIATION 1'))
fig.add_trace(go.Scatter(x = [first_stddev_end, first_stddev_end], y= [0,0.17] , mode = 'lines' , name='STANDARD DEVIATION 1'))
fig.add_trace(go.Scatter(x = [second_stddev_start, second_stddev_start], y= [0,0.17] , mode = 'lines' , name='STANDARD DEVIATION 2'))
fig.add_trace(go.Scatter(x = [second_stddev_end, second_stddev_end], y= [0,0.17] , mode = 'lines' , name='STANDARD DEVIATION 2'))
fig.add_trace(go.Scatter(x = [third_stddev_start, third_stddev_start], y= [0,0.17] , mode = 'lines' , name='STANDARD DEVIATION 3'))
fig.add_trace(go.Scatter(x = [third_stddev_end, third_stddev_end], y= [0,0.17] , mode = 'lines' , name='STANDARD DEVIATION 3'))

fig.show()

list_of_data_within_stdev1 = [result for result in dice_result if result > first_stddev_start and result < first_stddev_end]
list_of_data_within_stdev2 = [result for result in dice_result if result > second_stddev_start and result < second_stddev_end]
list_of_data_within_stdev3 = [result for result in dice_result if result > third_stddev_start and result < third_stddev_end]
print("percent data stdv1  : " , len(list_of_data_within_stdev1) * 100/len(marks_result))
print("percent data stdv2  : " , len(list_of_data_within_stdev2) * 100/len(marks_result))
print("percent data stdv3  : " , len(list_of_data_within_stdev3) * 100/len(marks_result))