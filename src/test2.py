import requests
import pandas as pd
import numpy as np
#https://www.finlab.tw/python-%E8%B2%A1%E5%A0%B1%E7%88%AC%E8%9F%B2-1-%E7%B6%9C%E5%90%88%E6%90%8D%E7%9B%8A%E8%A1%A8/

def financial_statement(year, season, type='綜合損益彙總表'):

    if year >= 1000:
        year -= 1911

    if type == '綜合損益彙總表':
        url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb04'
    elif type == '資產負債彙總表':
        url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb05'
    elif type == '營益分析彙總表':
        url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb06'
    else:
        print('type does not match')

    r = requests.post(url, {
        'encodeURIComponent':1,
        'step':1,
        'firstin':1,
        'off':1,
        'TYPEK':'sii',
        'year':str(year),
        'season':str(season),
    })

    r.encoding = 'utf8'
    dfs = pd.read_html(r.text, header=None)

    return pd.concat(dfs[1:], axis=0, sort=False)\
             .set_index(['公司代號'])\
             .apply(lambda s: pd.to_numeric(s, errors='ceorce'))


df = financial_statement(109, 3)
print(df)