#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import time



start_time = time.time()
all_tables=['tz_2013.csv', 'tz_2014.csv', 'tz_2015.csv', 'tz_2016.csv', 'tz_2017.csv', 'tz_2018.csv', 'tz_2019.csv', 'tz_2020.csv', 'tz_2021.csv' ]
for i in all_tables:
    vehicles = pd.read_csv(i, sep=";", low_memory=False  )

    ShortVehicles = vehicles.iloc[:, [4, 7, 8, 9, 10, 14, 15, 18]]  # Use columns what we need
    ShortVehicles.to_csv('AllData.csv', mode='a')
# interested collumns ~> 'D_REG', 'BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR', 'KIND', 'BODY', 'PURPOSE', 'FUEL', 'CAPACITY', 'OWN_WEIGHT', 'TOTAL_WEIGHT', 'N_REG_NEW'

print("--- %s seconds ---" % (time.time() - start_time))
