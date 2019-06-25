import random
from datetime import datetime, timedelta
import pandas as pd

a = []
for i in range(1,501):
    a.append(random.normalvariate(30, 1.4))


date = [datetime(2017, 7, 1, 10, 0, 0)]
for i in range(1,500):
    day = timedelta(seconds=random.uniform(2, 3))
    date.append(date[i - 1] + day)


gearwheel = pd.DataFrame({'date':date, 'diameter':a})
gearwheel.to_csv('gearwheel.csv', sep='\t', encoding='utf-8', index=False)
