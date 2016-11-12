import numpy as np
import pandas as pd


if __name__ == '__main__':
    RKH = pd.read_csv('C:\Users\\tczhaodachuan\Desktop\Papers\RKH.csv', sep=',', header=None)
    header = RKH.values[0][:]
    RKH = pd.DataFrame(RKH.values[1:][:], columns=header)
    #    for i in range(1,len(RKH)):
    #        parsed_date = datetime.datetime.strptime(RKH[0][i], '%m/%d/%Y')
    #        RKH[0][i] = parsed_date
    RTH = pd.read_csv('C:\Users\\tczhaodachuan\Desktop\Papers\RTH.csv', sep=',', header=None)
    header = RTH.values[0][:]
    RTH = pd.DataFrame(RTH.values[1:][:], columns=header)
    OIH = pd.read_csv('C:\Users\\tczhaodachuan\Desktop\Papers\OIH.csv', sep=',', header=None)
    header = OIH.values[0][:]
    OIH = pd.DataFrame(OIH.values[1:][:], columns=header)

    data = pd.merge(RTH, RKH, on='Date', suffixes=('_RTH', '_RKH'))
    data = pd.merge(data, OIH, on='Date')

    data['Adj Close_RTH'] = data['Adj Close_RTH'].astype(np.float)
    data['Adj Close_RKH'] = data['Adj Close_RKH'].astype(np.float)
    data['Adj Close'] = data['Adj Close'].astype(np.float)
    print data['Adj Close_RTH'][0:].values
    print data['Adj Close_RTH'][0:].pct_change().values
    returns = data['Adj Close_RTH'][0:].pct_change().values
    excess_returns = (returns - 0.04 / 252)

    print excess_returns
    print 252 * np.mean(excess_returns[1:])


    # print pd.merge(tday_RKH.to_frame(), tday.to_frame())
