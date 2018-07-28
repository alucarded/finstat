# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 12:35:22 2018

@author: tefpo
"""

import pandas as pd

def write_csv_data(data_dict, filename, delim = ';'):
    data_frame = pd.DataFrame.from_dict(data_dict, orient = 'index')
    data_frame.to_csv(filename)

def main():
    pass

if __name__ == "__main__":
    main()