import requests as rq
import time
import json
from config import *
currency_list = ['EOS', 'TRX', 'VEN', 'BNB', 'ICX', 'OMG', 'DGD', 'BTM', 'PPT', 'AE', 'RHOC', 'MKR', 'ETO', 'ZIL', 'SNT', 'REP', 'ZRX', 'WTC', 'VERI', 'FUN', 'XPA', 'AION', 'LRC', 'QASH', 'IOST', 'KCS', 'NAS', 'BAT', 'GNT', 'BQX', 'STORM', 'R','DRGN', 'FUN', 'KIN', 'KNC', 'ELF', 'SUB', 'NCASH', 'REQ', 'ENG', 'POWR', 'LINK', 'BNT', 'DENT', 'PAY', 'SALT','ADA','GNT','XRP','DGB','XVG','POWR','SC','EMC2','QTUM','NXT','NEO','REP','XLM','BTG','XEM','OMG','STRAT','ETC','XMR','MIOTA','DASH','EOS','STR','LSK','ARDR']
i = 0
o = 0

second_mode = False


def send_notification(title, body):
    data_send = {"type": "note", "title": title, "body": body}
    resp = rq.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

    if second_mode:
        data_send = {"type": "note", "title": title, "body": body}
        resp = rq.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                             headers={'Authorization': 'Bearer ' + access_token_2, 'Content-Type': 'application/json'})
        if resp.status_code != 200:
            raise Exception('Something wrong')
        else:
            print('complete sending')
    else:
        pass

while True:
    for x in currency_list:
        string = "https://api.coinbase.com/v2/exchange-rates?currency=%s"%(x)
        try:
            call = rq.get(string)
            call = json.loads(call.content)
        except Exception as e:
            print(e)
            pass
        if any("errors" in s for s in call):
            if call["errors"][0]["id"] == 'invalid_request':
                pass
                #print(call["errors"][0]["id"])
            else:
                pass
                #print("No error")
        elif not call:
            pass
        else:
            string = "COIN %s ON COINBASE, BUY NOW"%(x)
            send_notification("COIN ON COINBASE",string)
    time.sleep(2)
    o += 1
    if o % 200 == 0:
            string = "Script still looping"
            send_notification("Script active",string)
    if i == 400:
        i = 0
        o = 0

#nohup long-running-command &
