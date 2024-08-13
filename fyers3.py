#my profile details

from fyers_apiv3 import fyersModel
from credentials import client_id
from stocknames import symbols

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE3MDE5Mjc2NzgsImV4cCI6MTcwMTk5NTQxOCwibmJmIjoxNzAxOTI3Njc4LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCbGNWci1RcmwwUVMwUUdRNk4wVi1yek1udmIwWWl0cWxpQ2g4U1VlRjlGQjZSbldHMUlobW1mUWFIeGR4ZHQ2OEh4eUd6Vi10dHFTQXVBR1hGbHRnRVE1OE9KVnNGeTlnNHNBMXlrWC1rT0RNOVF2dz0iLCJkaXNwbGF5X25hbWUiOiJGQUhFRU0gU0FNRUVSIiwib21zIjoiSzEiLCJoc21fa2V5IjoiNmIzMjYzY2Q5OThkNGExNWRiN2Y2ZjBiYTI3NGU3MTEyYjI5YWE5NzBlZWJlMzI0ZGIxOGFjYzAiLCJmeV9pZCI6IlhGMDAwMzEiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.PBYsO84fgAKzrXkU0UnJObFT_g9itFbva9p7yBOBckU"
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

for i in symbols:
    data = {
    "symbol":i,
    "ohlcv_flag":"0"
    }

    response = fyers.depth(data=data)
    ask = response['d'][i]['ask'][0]['price']
    bid = response['d'][i]['bids'][0]['price']
    try:
        print((ask-bid)/ask)
    except ZeroDivisionError:
        print("ask price is zero")