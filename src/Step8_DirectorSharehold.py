from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import Utils
import pandas as pd
import random
import time

def GetDirectorSharehold():
    cssSelector = '#divStockList'
    sum_df = pd.DataFrame()

    for rankIndex in range(1, 6):
        url = f'https://goodinfo.tw/tw/StockList.asp?SHEET=董監持股&MARKET_CAT=熱門排行&INDUSTRY_CAT=全體董監持股比例&RANK={str(rankIndex)}'
        print(url)

        try:
            df = Utils.GetDataFrameByCssSelector(url, cssSelector)
            print(df)
            sum_df = pd.concat([sum_df, df], axis=0)
            #df.columns = df.columns.get_level_values(1)
        except:
            time.sleep(random.randint(20, 30))
            df = Utils.GetDataFrameByCssSelector(url, cssSelector)
            print(df)
            #df.columns = df.columns.get_level_values(1)

    sum_df = sum_df[sum_df.ne(sum_df.columns).any(1)]
    sum_df.to_csv('董監持股比例.csv',encoding='utf_8_sig')

GetDirectorSharehold()