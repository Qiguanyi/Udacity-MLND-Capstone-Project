# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import database_api as dbi
import CustomizedFunctions as CFun
import datetime
import calendar

def List_to_SQL(list):
    '''
    change elements in list into SQL expression
    '''
    item = ['\'{}\''.format(x) for x in list]
    item = '(' + ', '.join(item) + ')'
    return item

def getMonthFirstDayAndLastDay(year=None, month=None):
    """
    :param year: 年份，默认是本年，可传int或str类型
    :param month: 月份，默认是本月，可传int或str类型
    :return: firstDay: 当月的第一天，datetime.date类型
              lastDay: 当月的最后一天，datetime.date类型
    """
    if year:
        year = int(year)
    else:
        year = datetime.date.today().year

    if month:
        month = int(month)
    else:
        month = datetime.date.today().month

    # 获取当月第一天的星期和当月的总天数
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)

    # 获取当月的第一天
    firstDay = datetime.date(year=year, month=month, day=1)
    lastDay = datetime.date(year=year, month=month, day=monthRange)

    return [firstDay, lastDay]

def filter_extreme_MAD(series,n): #MAD: 中位数去极值 
    
    median = series.quantile(0.5)
    new_median = ((series - median).abs()).quantile(0.50)
    
    max_range = median + n*new_median
    min_range = median - n*new_median
    
    return np.clip(series,min_range,max_range)


def ZscoreNormalization(x):
    """Z-score normaliaztion"""
    x = (x - np.mean(x)) / np.std(x)
    return x

def xlsx_to_csv_pd(file_name_xls, sheetname):
    data_xls = pd.read_excel(file_name_xls, sheetname = sheetname, index_col=0)
    data_xls.to_csv(file_name_xls, encoding='utf-8')



# -- define a class including all parameter
path = 'C:/Users/ThinkPadUser/Desktop/Udacity_ML Engineer/Capstone Project/'
Base_indicator_section = pd.read_csv(path+'data/Base_indicator_section.csv', index_col=0)
Base_indicator_section['TRADE_DT'] = [str(x) for x in Base_indicator_section['TRADE_DT']]
data_day = list(set(list(Base_indicator_section['TRADE_DT'])))
data_day.sort()

class Para:
    method = 'SVM'
    month_in_sample = data_day[:72] # return 72 months
    month_test = data_day[72:] # return 80 months
    percent_select = [0.3, 0.3] # 30% positive samples, 30% negetive samples
    percent_cv = 0.1 # 10% cross validation samples
    path_data = 'C:/Users/ThinkPadUser/Desktop/Udacity_ML Engineer/Capstone Project/data'
    path_results = 'C:/Users/ThinkPadUser/Desktop/Udacity_ML Engineer/Capstone Project/results'
    seed = 42 # random seed
    svm_kernel = 'rbf' # svm parameter
    svm_c = 1 # svm parameter
    
para = Para()

# -- function: label data
def label_data(data):
    # initialize
    data['return_bin'] = np.nan
    # sort by excess return
    data = data.sort_values(by = 'S_DQ_PCTCHANGE', ascending = False)
    # decide how much stocks will be selected
    n_stock_select = np.multiply(CFun.para.percent_select, data.shape[0])
    n_stock_select = np.around(n_stock_select).astype(int)
    # assign 1 or 0
    data.iloc[:n_stock_select[0], -1] = 1
    data.iloc[-n_stock_select[1]:, -1] = 0
    # remove other stocks
    data = data.dropna(axis = 0)
    
    return data
