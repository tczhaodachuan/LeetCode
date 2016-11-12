import datetime as dt

import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import numpy as np


class SharpRatioCalculator(object):
    def __init__(self):
        # initialize data source from Yahoo
        self.data_access = da.DataAccess('Yahoo')
        # initialize the interesting keys we would like to use
        self.ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
        self.actual_close = 'close'
        self.d_trade_hours_per_day = dt.timedelta(hours=16)
        self.risk_free_daily = 0.0
        # ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
        # d_data = dict(zip(ls_keys, ldf_data))

    def simulate(self, start_date, end_date, symbols, allocations):
        # convert start day, end day with 16 traiding hours to timestamps
        ldt_timestamps = du.getNYSEdays(start_date, end_date, self.d_trade_hours_per_day)
        # holding days for labels, used to calculate sharp_ratio
        ldt_holding_days = len(ldt_timestamps)
        # get data from data source with bales
        ldf_data = self.data_access.get_data(ldt_timestamps, symbols, self.ls_keys)
        # convert list of objects into dict which put key as ls_keys, value as the object
        d_data = dict(zip(self.ls_keys, ldf_data))

        # get the actual close price from d_data which is a dict
        close_prices = d_data[self.actual_close].values.copy()

        normalized_close_prices = close_prices / close_prices[0, :]

        # convert allocations into a dimension reduce vector
        # allocation_vec = np.array(allocations).reshape(4, 1)
        # adjusted_normalized_close_prices = np.dot(normalized_close_prices, allocation_vec)
        # multiply the allocations after normalized the close prices
        normalized_close_prices = normalized_close_prices * allocations
        # sum each row will give daily returns on this portfolio
        adjusted_normalized_close_prices = np.sum(normalized_close_prices, axis=1)
        # normalized daily returns of the normalized close prices

        # copy values into daily_return variable
        # has to use copy values, cause returnied0 is change the value passed in
        daily_ret = adjusted_normalized_close_prices.copy()
        tsu.returnize0(daily_ret)

        avg_daily_ret = np.mean(daily_ret)
        vol = np.std(daily_ret)
        sharp_ratio = np.sqrt(ldt_holding_days) * (avg_daily_ret - self.risk_free_daily) / vol
        cum_ret = adjusted_normalized_close_prices[len(adjusted_normalized_close_prices) - 1]

        return vol, sharp_ratio, avg_daily_ret, cum_ret

    def simulate2(self, dt_start, dt_end, ls_symbols, ls_allocation):
        # Formatting the date timestamps
        dt_timeofday = dt.timedelta(hours=16)
        ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

        # Open the dataset and read in the closing price
        ls_keys = ['close']
        c_dataobj = da.DataAccess('Yahoo')
        ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
        d_data = dict(zip(ls_keys, ldf_data))

        # Calculate the portfolio value
        temp = d_data['close'].values.copy()
        d_normal = temp / temp[0, :]
        alloc = np.array(ls_allocation).reshape(4, 1)
        portVal = np.dot(d_normal, alloc)
        print portVal

        # Caluclate the daily returns
        dailyVal = portVal.copy()
        tsu.returnize0(dailyVal)

        # Calculate statistics
        daily_ret = np.mean(dailyVal)
        vol = np.std(dailyVal)
        sharpe = np.sqrt(252) * daily_ret / vol
        cum_ret = portVal[portVal.shape[0] - 1][0]
        print portVal.shape[0] - 1

        return vol, daily_ret, sharpe, cum_ret


if __name__ == '__main__':
    sr_calculator = SharpRatioCalculator()
    symbols = ['AAPL', 'GLD', 'GOOG', 'XOM']
    start_date = dt.datetime(2011, 1, 1)
    end_date = dt.datetime(2011, 12, 31)
    allocations = [0.4, 0.4, 0.0, 0.2]
    (vol, sharp_ratio, avg_daily_ret, cum_ret) = sr_calculator.simulate(start_date, end_date, symbols, allocations)
    print 'Start Date: %s' % start_date
    print 'End Date: %s' % end_date
    print 'Symbols: %s' % symbols
    print 'Sharp Ratio : %f' % sharp_ratio
    print 'Volatility(stdev of daily returns) : %f' % vol
    print 'Average Daily Returns : %f' % avg_daily_ret
    print 'Cumulative Returns : %f' % cum_ret
