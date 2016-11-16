import datetime as dt

import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np


class SharpRatioCalculator(object):
    def __init__(self, plot=False):
        # initialize data source from Yahoo
        self.data_access = da.DataAccess('Yahoo')
        # initialize the interesting keys we would like to use
        self.ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
        self.actual_close = 'close'
        self.d_trade_hours_per_day = dt.timedelta(hours=16)
        self.risk_free_daily = 0.0
        self.plot = plot
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

        temp_normalized_close_prices = close_prices / close_prices[0, :]

        # convert allocations into a dimension reduce vector
        # allocation_vec = np.array(allocations).reshape(4, 1)
        # adjusted_normalized_close_prices = np.dot(normalized_close_prices, allocation_vec)
        # multiply the allocations after normalized the close prices
        normalized_close_prices = temp_normalized_close_prices * allocations
        # sum each row will give daily returns on this portfolio
        adjusted_normalized_close_prices = np.sum(normalized_close_prices, axis=1)

        # draw pic
        s_data = self.data_access.get_data(ldt_timestamps, ['$SPX'], self.ls_keys)
        spx_data = dict(zip(self.ls_keys, s_data))
        spx_close_price = spx_data[self.actual_close].values.copy()
        spx_normalized_close_price = spx_close_price / spx_close_price[0]
        if self.plot:
            plt.clf()
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
            plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
            plt.plot(ldt_timestamps, temp_normalized_close_prices)
            plt.plot(ldt_timestamps, adjusted_normalized_close_prices)
            plt.plot(ldt_timestamps, spx_normalized_close_price)
            plt.legend(symbols + ['Portfolio', 'SPX'])
            plt.ylabel('Adjusted Normalized Daily Returns')
            plt.xlabel('Date')
            plt.gcf().autofmt_xdate()
            plt.savefig('adjustedclose.pdf', format='pdf')
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

    def optimize(self, start_date, end_date, symbols):

        max_sharp_ratio = 0
        max_allocations = [0, 0, 0, 1.0]
        for x in np.arange(0, 1, 0.1):
            for y in np.arange(0, 1 - x + 0.1, 0.1):
                for z in np.arange(0, 1 - x - y + 0.1, 0.1):
                    allocations = [x, y, z, 1 - x - y - z]
                    statistic = self.simulate(start_date, end_date, symbols, allocations)

                    if statistic[1] >= max_sharp_ratio:
                        max_sharp_ratio = statistic[1]
                        max_allocations = allocations

        return (max_allocations, max_sharp_ratio)

    def gradient_ascent(self, start_date, end_date, symbols):
        best_allocations = np.zeros(len(symbols))
        sharpe_ratios = []
        for i in range(len(symbols)):
            init_allocations = np.zeros(len(symbols))
            init_allocations[i] = 1
            response = self.simulate(start_date, end_date, symbols, init_allocations)

            if response[1] > 0:
                sharpe_ratios.append(response[1])
            else:
                sharpe_ratios.append(0.0)
        total = sum(sharpe_ratios)
        print sharpe_ratios, total
        for i in range(len(symbols)):
            allocate = sharpe_ratios[i] / total
            best_allocations[i] = allocate

        return best_allocations

if __name__ == '__main__':
    sr_calculator = SharpRatioCalculator()
    symbols = ['C', 'GS', 'IBM', 'HNZ']
    start_date = dt.datetime(2010, 1, 1)
    end_date = dt.datetime(2010, 12, 31)
    allocations = [0.2, 0.0, 0.8, 0.0]
    (vol, sharp_ratio, avg_daily_ret, cum_ret) = sr_calculator.simulate(start_date, end_date, symbols, allocations)


    # print sr_calculator.optimize(start_date, end_date, symbols)
    best_allocations = sr_calculator.gradient_ascent(start_date, end_date, symbols)
    print best_allocations

    (vol, sharp_ratio, avg_daily_ret, cum_ret) = sr_calculator.simulate(start_date, end_date, symbols, best_allocations)
    print 'Start Date: %s' % start_date
    print 'End Date: %s' % end_date
    print 'Symbols: %s' % symbols
    print 'Sharp Ratio : %f' % sharp_ratio
    print 'Volatility(stdev of daily returns) : %f' % vol
    print 'Average Daily Returns : %f' % avg_daily_ret
    print 'Cumulative Returns : %f' % cum_ret
