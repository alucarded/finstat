# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 15:55:24 2018

@author: tefpo
"""
import sys
import urllib.request
import urllib.parse
from io import StringIO

try:
    from data_fetcher import data_reader
except:
    import data_reader        

class URLDataFetcher:
    def __init__(self):
        pass
    
    def fetch_data(self, id, from_datetime = '', to_datetime = '', frequency = ''):
        raise NotImplementedError
        
        
    
class FredDataFetcher(URLDataFetcher):
    
    BASE_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv"
    
    def fetch_data(self, id, from_datetime = '', to_datetime = '', frequency = ''):
        query_dict = { 'id' : id, \
                       'cosd' : from_datetime, \
                       'coed' : to_datetime, \
                       'fq' : frequency }
        params_str = urllib.parse.urlencode(query_dict)
        url = "%s?%s" % (self.BASE_URL, params_str)
        response = urllib.request.urlopen(url)
        csv_str = response.read().decode('utf-8')
        csv_buffer = StringIO(csv_str)
        locale_code = 'en_US'
        if sys.platform == "linux": # for Linux
            locale_code = 'en_US.utf8'
        data_dict = data_reader.read_csv_data(csv_buffer, delim = ',', datetime_format = '%Y-%m-%d', locale_code = locale_code)
        return data_dict

class EurosystemDataFetcher(URLDataFetcher):
    
    BASE_URL = "http://sdw.ecb.europa.eu/export.do"
    
    NODE_DICT = { '143.FM.B.U2.EUR.4F.KR.MLFR.LEV' : '9691107' \
            }
    
    def fetch_data(self, id, from_datetime = '', to_datetime = '', frequency = ''):
                query_dict = { 'node' : self.NODE_DICT[id], \
                               'exportType' : 'csv', \
                               'ajaxTab' : 'true', \
                               'SERIES_KEY' : id }
                params_str = urllib.parse.urlencode(query_dict)
                url = "%s?%s" % (self.BASE_URL, params_str)
                response = urllib.request.urlopen(url)
                csv_str = response.read().decode('utf-8')
                # Response CSV formatting is strage..
                csv_str = "DATE" + csv_str.split("\n",1)[1]
                print(csv_str)
                csv_buffer = StringIO(csv_str)
                locale_code = 'en_US'
                if sys.platform == "linux": # for Linux
                    locale_code = 'en_US.utf8'
                data_dict = data_reader.read_csv_data(csv_buffer, delim = ',', datetime_format = '%Y-%m-%d', row_start = 3, locale_code = locale_code)
                return data_dict
    
if __name__ == "__main__":
    fred_data_fetcher = FredDataFetcher()
    print(fred_data_fetcher.fetch_data(id = 'FEDFUNDS', from_datetime = '2010-07-01', \
                            to_datetime = '2018-06-01', frequency = 'Monthly'))
    euro_data_fetcher = EurosystemDataFetcher()
    print(euro_data_fetcher.fetch_data(id = '143.FM.B.U2.EUR.4F.KR.MLFR.LEV'))
