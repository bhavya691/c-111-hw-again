import statistics
import random
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv('data.csv')
data = df['Math_score'].tolist()
population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)

def mean_of_interventions(filename):
    df = pd.read_csv(filename)
    data = df['Math_score'].tolist()
    return statistics.mean(data)

mean1 = mean_of_interventions('School1.csv')
mean2 = mean_of_interventions('School2.csv')
mean3 = mean_of_interventions('School3.csv')


def traces(fig, a, label):
    fig.add_trace(go.Scatter(x=[a,a], y=[0,1.3], mode='lines', name=label))

def random_mean_set():
    dataset = []
    for i in range(0,100):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def plot_graph(data, mean, stdev):
    stdev_1_start, stdev_1_end = mean - stdev, mean + stdev
    stdev_2_start, stdev_2_end = mean - 2*stdev, mean + 2*stdev
    stdev_3_start, stdev_3_end = mean - 3*stdev, mean + 3*stdev

    fig = ff.create_distplot([data], ['Score'], show_hist=False)
    traces(fig, mean1, 'mean1') 
    traces(fig, mean2, 'mean2')
    traces(fig, mean3, 'mean3')
    traces(fig, mean, 'mean')
    traces(fig, stdev_1_start, 'stdev_1_start')
    traces(fig, stdev_1_end, 'stdev_1_end')
    traces(fig, stdev_2_start, 'stdev_2_start')
    traces(fig, stdev_2_end, 'stdev_2_end')
    traces(fig, stdev_3_start, 'stdev_3_start')
    traces(fig, stdev_3_end, 'stdev_3_end')
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        random_mean = random_mean_set()
        mean_list.append(random_mean)
    mean = statistics.mean(mean_list)
    stdev = statistics.stdev(mean_list)
    plot_graph(mean_list, mean, stdev)
    print('Mean of raw data: \t', population_mean)
    print('Stdev of raw data: \t', population_stdev)
    print('Mean of Sampling Distribution: \t', mean)
    print('Stdev of Sampling Distrubution: \t', stdev)
    zscore1 = (mean1 - mean) / stdev
    zscore2 = (mean2 - mean) / stdev
    zscore3 = (mean3 - mean) / stdev
    print(zscore1, zscore2, zscore3)

setup()