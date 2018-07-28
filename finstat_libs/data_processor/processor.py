# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 12:35:22 2018

@author: tefpo
"""

import abc
from datetime import datetime
import pytz
import sys
import numbers

class FillStrategy(abc.ABCMeta):
#    NEAREST_NEIGHBOR_INTERPOLATION = 0
#    LINEAR_INTERPOLATION = 1
    
    @abc.abstractmethod
    def fill_algorithm(self):
        pass

class NearestNeighborInterpolation(FillStrategy):
    def fill_algorithm(self):
        pass
    
class LinearInterpolation(FillStrategy):
    def fill_algorithm(self):
        pass

def fill_missing_data(time_series, \
                          time_period, \
                          strategy, \
                          end_date = datetime.now()):
    """Fills gaps in time series.
    
    # Arguments
        time_series: distionary with datetime keys and numeric values.
        time_period: datetime between subsequent data points.
        strategy: interpolation strategy.
    """
    pass

def prepare_complete_series(datetime_dict, time_period, start_date):
    datetime_array = sorted(datetime_dict.keys())
    first_date_idx = sys.maxsize
    for i in range(0, len(datetime_array)):
        if datetime_array[i] >= start_date:
            first_date_idx = i
            break
    if first_date_idx >= len(datetime_array):
        raise ValueError("No datetimes at or after start_date")
    complete_dict = {}
    date_it = start_date
    for i in range(first_date_idx, len(datetime_array)):
        while date_it <= datetime.now(pytz.utc) and (i >= len(datetime_array)-1 or date_it < datetime_array[i+1]):
            complete_dict[date_it] = []
            values_arr = datetime_dict[datetime_array[i]]
            for j in range(0, len(values_arr)):
                assert values_arr[j] is None or isinstance(values_arr[j], numbers.Number)
                try:
                    complete_dict[date_it].append(values_arr[j])
                except Exception as ex:
                    print(ex)
#                    if len(complete_dict) > 1:
#                        complete_dict[date_it] = complete_dict[date_it - time_period]
#                    else:
#                        raise ValueError("First key value is not valid (cannot be evaluated to float)")
            date_it += time_period
    return complete_dict

def merge_data_dictionaries(first_dict, second_dict):
    result_dict = {}
    for key in first_dict:
        if key in second_dict:
            result_dict[key] = first_dict[key] + second_dict[key]
        else:
            print("Key %s not present in both dictionaries", key)
    return result_dict

def scale_values_in_dictionary(data_dict, scale, val_list_idx):
    for key in data_dict.keys():
        data_dict[key][val_list_idx] = data_dict[key][val_list_idx] / scale
    return data_dict