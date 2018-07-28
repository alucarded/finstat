# -*- coding: utf-8 -*-
from data_fetcher.data_fetcher import FredDataFetcher
from data_fetcher.data_fetcher import EurosystemDataFetcher
#from data_fetcher import data_reader
from data_processor import processor
from visualization import plot

from datetime import datetime
from datetime import timedelta
import logging
import pytz

NZD_OFFICIAL_CASH_RATES_PATH = "C:\\Users\\tefpo\\Desktop\\forex_analysis\\data\\nzd\\nzd_OCR.csv"
ECB_INTEREST_RATES_PATH = "C:\\Users\\tefpo\\Desktop\\forex_analysis\\data\\eur\\ecb_marginal_lending_interest_rates.csv"

#EURUSD_EXCHANGE_RATES_PATH = "C:\\Users\\tefpo\\Desktop\\forex_analysis\\data\\eur\\EURUSD.csv"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def generate_chart():
    fred_fetcher = FredDataFetcher()
    eurosystem_fetcher = EurosystemDataFetcher()

    interest_rates = eurosystem_fetcher.fetch_data('143.FM.B.U2.EUR.4F.KR.MLFR.LEV')
    #interest_rates = data_reader.read_csv_data(ECB_INTEREST_RATES_PATH, locale_code = 'pl_PL.utf8')
    us_rates = fred_fetcher.fetch_data(id = 'FEDFUNDS', from_datetime = '2000-01-01', \
                            to_datetime = '2018-07-01', frequency = 'Daily')
    #exchange_rate = data_reader.read_csv_data(EURUSD_EXCHANGE_RATES_PATH, datetime_format = '%d.%m.%Y %H:%M:%S.000 GMT%z', locale_code = 'en_US.utf8')
    exchange_rate = fred_fetcher.fetch_data(id = 'DEXUSEU', from_datetime = '2000-01-01', \
                            to_datetime = '2018-07-01', frequency = 'Daily')

    interest_rates = processor.prepare_complete_series(interest_rates, timedelta(days=1), datetime(2000, 1, 1, tzinfo = pytz.UTC))
    us_rates = processor.prepare_complete_series(us_rates, timedelta(days=1), datetime(2000, 1, 1, tzinfo = pytz.UTC))

    # Get difference
    interest_rates_diff = {}
    for key in interest_rates.keys():
        interest_rates_diff[key] = [interest_rates[key][0] - us_rates[key][0]]
    interest_rates_diff = processor.scale_values_in_dictionary(interest_rates_diff, 2.0, 0)

    exchange_rate = processor.prepare_complete_series(exchange_rate, timedelta(days=1), datetime(2000, 1, 1, tzinfo = pytz.UTC))

    plot_dict = processor.merge_data_dictionaries(interest_rates_diff, exchange_rate)

    plotter = plot.PyPlot()
    div_data = plotter.plot(plot_dict, ['EURUSD interest rates difference', 'EURUSD exchange rate'], 2)
    logger.info("Plot data: {}".format(div_data))
    print(div_data)
    return div_data

if __name__ == "__main__":
    generate_chart()