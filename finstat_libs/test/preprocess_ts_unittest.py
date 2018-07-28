# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 17:09:41 2018

@author: tefpo
"""

import unittest
import pytz
from datetime import datetime
from datetime import timedelta
from data_processing import preprocess_time_series as preprocess

class TestPreprocessTS(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_fill_time_series_gaps(self):
        
        simple_series = {datetime(2000, 1, 1, tzinfo = pytz.UTC): 1.0, \
                         datetime(2000, 1, 2, tzinfo = pytz.UTC): 1.1, \
                         datetime(2000, 1, 4, tzinfo = pytz.UTC): 1.2}
        preprocess.fill_time_series_gaps(simple_series, \
                                         timedelta(days=1), \
                                         datetime(2000, 1, 1), \
                                         preprocess.FillStrategy.NEAREST_NEIGHBOR_INTERPOLATION)
        self.assertTrue(False)
 
if __name__ == '__main__':
    unittest.main()