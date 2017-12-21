import requests as rq
import time
import json
from config import access_token
currency_list = ['SALT','ADA','GNT','XRP','DGB','XVG','POWR','SC','EMC2','QTUM','NXT','NEO','REP','XLM','BTG','XEM','OMG','STRAT','ETC','XMR','MIOTA','DASH','EOS','STR','LSK','ARDR']
i = 0
o = 0
def send_notification(title, body):
    data_send = {"type": "note", "title": title, "body": body}
    resp = rq.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

while i == 0:
    for x in currency_list:
        string = "https://api.coinbase.com/v2/exchange-rates?currency=%s"%(x)
        call = rq.get(string)
        call = json.loads(call.content)
        if any("errors" in s for s in call):
            if call["errors"][0]["id"] == 'invalid_request':
                print(call["errors"][0]["id"])
            else:
                print("No error")
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
