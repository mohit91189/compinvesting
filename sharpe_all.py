import glob
import os
import csv
from stocks import *

csv_fields = ['stock_code','avg_annual', 'avg_daily','daily_std_dev','sharpe_ratio']
pwd = os.path.dirname(os.path.abspath(__file__))
files = glob.iglob(os.path.join(pwd,"data","all", '*.csv'))
with open(os.path.join(pwd,'output.csv'), 'w') as csvfile:
    writer = csv.DictWriter(csvfile, csv_fields, delimiter=',')
    for f in files:
        stock = f.split('/')[-1].replace('.csv','')
        stock_file = loadCSV(f)
        ss = stockStats(stock_file, stock)
        if ss['avg_annual'] > 0 and ss['sharpe_ratio'] > 1:
            print ss
            writer.writerow(ss)