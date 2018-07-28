# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 12:35:22 2018

@author: tefpo
"""

from datetime import datetime
import pytz

import pandas as pd
import locale

"""
Construct dictionary from CSV file in which first column is datetime
and other columns are values.

Parameters
----------
Returns
-------
Dictionary, where key is datetime and value is an array of values
"""
def read_csv_data(filename_or_buffer, delim = ';', \
                  datetime_format = '%Y-%m-%d', \
                  value_columns_count = 1, \
                  row_start = 1, \
                  locale_code = 'pl_PL'):
    try:
        locale.setlocale(locale.LC_ALL, locale_code)
    except locale.Error as err:
        print("Please install following locale: ", locale_code)
        sys.exit()
    dataset = pd.read_csv(filename_or_buffer, delim)
    datetimes = dataset.iloc[:, 0:1].values
    values_arr = []
    for i in range(0, value_columns_count):
        values_arr.append(dataset.iloc[:, 1:2].values)
        assert len(datetimes) == len(values_arr[i])
    data_dict = {}
    for i in range(row_start, len(datetimes)):
        datetime_object = datetime.strptime(datetimes[i][0], datetime_format)
        if datetime_object.tzinfo is None or datetime_object.tzinfo.utcoffset(datetime_object) is None:
            datetime_object = pytz.utc.localize(datetime_object)
        row_arr = []
        for j in range(0, value_columns_count):
            try:
                if isinstance(values_arr[j][i][0], str):
                    values_arr[j][i][0] = locale.atof(values_arr[j][i][0])
                row_arr.append(values_arr[j][i][0])
            except Exception as ex:
                print("Error, adding None: ", ex)
                row_arr.append(None)
        data_dict[datetime_object] = row_arr
    return data_dict

def main():
    pass

if __name__ == "__main__":
    main()
