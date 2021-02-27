import pandas as pd

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

nb_zones = ['z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7']
total_zones = nb_zones.copy() + ['z8', 'z9', 'z10', 'z11']

#incentive_rates = open('Information/IncentiveRates.csv', 'r').readlines()[0].split(',')
[emission_tax, non_emission_tax] = [0.015, 0.009] # [float(x) for x in incentive_rates]

# penalty_values = [[float(x) for x in y.split(',')] for y in open('Information/PenaltyValues.csv', 'r').readlines()]

penalty_values = pd.read_csv('Information/PenaltyValues.csv', header=None, names=total_zones.copy())
penalty_values['zone'] = total_zones.copy()

plant_production_rates = pd.read_csv('Information/PlantProductionRates.csv', names=['thermal', 'nuclear', 'combustion', 'hydro', 'wind'])
plant_production_rates['zone'] = nb_zones.copy()

trend_2015 = pd.read_csv('PastYearData/NBTrend2015.csv', header=None, names=nb_zones.copy())
trend_2015['months'] = months.copy()

trend_2016 = pd.read_csv('PastYearData/NBTrend2016.csv', header=None, names=nb_zones.copy())
trend_2016['months'] = months.copy()

trend_2017 = pd.read_csv('PastYearData/NBTrend2017.csv', header=None, names=nb_zones.copy())
trend_2017['months'] = months.copy()

trend_2018 = pd.read_csv('PastYearData/NBTrend2018.csv', header=None, names=nb_zones.copy())
trend_2018['months'] = months.copy()

pass