import re
from typing import Counter, Pattern
from iqoptionapi.stable_api import IQ_Option
from iqoptionapi.ws.objects.candles import Candle
from candlestick import candlestick
import concurrent.futures
import pandas as pd
import asyncio, random
from threading import Thread
from threading import current_thread
import numpy as np
import time
from datetime import datetime
import logging
import json
import sys

def con(verbose = False, iq = None, checkConnection = False):
    print("start")
    if verbose:
        logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')

    if iq == None:
      print("Trying to connect to IqOption")
      iq=IQ_Option('boopathiviky@gmail.com','ex$4,X.,tzDU5b?') # YOU HAVE TO ADD YOUR USERNAME AND PASSWORD
      iq.connect()

    if iq != None:
      while True:
        if iq.check_connect() == False:
          print('Error when trying to connect')
          print(iq)
          print("Retrying")
          iq.connect()
        else:
          if not checkConnection:
            print('Successfully Connected!')
          break
        time.sleep(3)

    iq.change_balance("PRACTICE") #or real
    return iq
async def movingaverage(iq,pair):
  con(iq = iq, checkConnection = True)
  while True:
    data=iq.get_candles(pair, 60, 300, time.time())
    candle = pd.DataFrame.from_dict(data)
    candle.rename(columns={"max": "high", "min": "low"}, inplace=True)
    candle['EMA_16'] = candle['close'].ewm(span = 16, adjust = False).mean()
    candle['EMA_6'] = candle['close'].ewm(span = 6, adjust = False).mean()
    candle['MA_20'] = candle['close'].rolling(window = 20).mean()
    candle['MA_50'] = candle['close'].rolling(window = 50).mean()
    data=candle
    data1=data[["EMA_16","EMA_6"]].round(8)
    data2=data[["MA_20","MA_50"]].round(8)
    # data3=data[["MA_20","EMA_6"]].round(8)
    # data4=data[["MA_50","EMA_16"]].round(8)
    emadiff=data1.T.diff().astype(float)
    madiff=data2.T.diff().astype(float)
    # xmadiff=data3.T.diff().astype(float)
    # yadiff=data4.T.diff().astype(float)
    emadiff=emadiff*1000000
    madiff=madiff*1000000
    emadiff=emadiff.round()
    madiff=madiff.round()
    # xmadiff=xmadiff*1000000
    # yadiff=yadiff*1000000
    # xmadiff=xmadiff.round()
    # yadiff=yadiff.round()
    dd=emadiff.T
    ddd=madiff.T
    # x=xmadiff.T
    # y=yadiff.T
    data["EMADIFF"]=dd["EMA_6"]
    data["MADIFF"]=ddd["MA_50"]
    # xx=x["EMA_6"]
    # yy=y["EMA_16"]
    # data["XSMA"]=xx
    # data["XBMA"]=yy
    candle["EMADIFF"]=data["EMADIFF"].abs()
    candle["MADIFF"]=data["MADIFF"].abs()
    # candle["XSMA"]=data["XSMA"].abs()
    # candle["XBMA"]=data["XBMA"].abs()
    global trend
    global miner
    trend="N"
    miner="N"
    trend_anaylzer=""
    Money=1
    expirations_mode=1
    if candle["MA_20"].iloc[-1]>candle["MA_50"].iloc[-1]:
      trend="up"
      if candle ["EMA_6"].iloc[-1]>candle ["EMA_16"].iloc[-1]:
        miner="up"
      if candle ["EMA_6"].iloc[-1]<candle ["EMA_16"].iloc[-1]:
        miner="down"
      if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]>candle["EMADIFF"].iloc[-3]):
        trend_anaylzer="continuation"
      if (candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]>candle["EMADIFF"].iloc[-3]):
        trend_anaylzer = "higher point"
      if (candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]<candle["EMADIFF"].iloc[-3]):
        trend_anaylzer = "retracement"
      if (candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]<candle["EMADIFF"].iloc[-3]):
        trend_anaylzer = "entry"
    elif candle["MA_20"].iloc[-1]<candle["MA_50"].iloc[-1]:
      trend = "down"
      if candle ["EMA_6"].iloc[-1]>candle ["EMA_16"].iloc[-1]:
        miner="up"
      if candle ["EMA_6"].iloc[-1]<candle ["EMA_16"].iloc[-1]:
        miner="down"
      if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]>candle["EMADIFF"].iloc[-3]):
        trend_anaylzer="continuation"
      if (candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]>candle["EMADIFF"].iloc[-3]):
        trend_anaylzer = "higher point"
      if (candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]<candle["EMADIFF"].iloc[-3]):
        trend_anaylzer = "retracement"
      if (candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]<candle["EMADIFF"].iloc[-3]):
        trend_anaylzer = "entry"
    # await asyncio.sleep(5)
    return trend_anaylzer,trend,miner
  
    

async def fibanoci(iq,pair):
  sec = time()
  ema16,ema20,ema6,ema50,result=await movingaverage(iq,pair)
  print(json.dumps(result,indent=1))
  while True:
    print("fib1")
    ema16,ema20,ema6,ema50,result=await movingaverage(iq,pair)
    await asyncio.sleep(1)
    print("EMA_16:",ema16,"EMA_6:",ema6,"|","MA_20:",ema20," /","MA_50:",ema50,end="\r")
    
async def patterns(iq,pair):
  candle=""
  data = iq.get_candles(pair, 60, 3, time.time())
  print("\n enter into trade for "+str(pair),"search for candlesticks")
  df = pd.DataFrame.from_dict(data)
  df.rename(columns={"max": "high", "min": "low"}, inplace=True)
  # print(str(df)+' For '+str(pair))
  current_close = df["close"][2]
  res = candlestick.bullish_engulfing(df, target="bullish_engulfing")
  df = res
  res = candlestick.bearish_engulfing(df, target="bearish_engulfing")
  res = candlestick.hammer(res, target="hammer")
  res = candlestick.inverted_hammer(res, target="inverted_hammer")
  res = candlestick.shooting_star(res, target="shooting_star")
  res = candlestick.hanging_man(res, target="hanging_man")
  res = candlestick.doji(res, target="doji")
  res = candlestick.dragonfly_doji(res, target="dragonfly_doji")
  res = candlestick.bearish_harami(res,target="bearish_harami")
  res = candlestick.star(res,target="star")
  res = candlestick.morning_star_doji(res,target="morning_star_doji")
  res = candlestick.piercing_pattern(res,target="piercing_pattern")
  ca1 = res.to_dict("records")
  count=1
  pos=0
  for data in ca1:
    # print(count)
    
    if data["bearish_engulfing"] == True:
      candle="bearish_engulfing"
      pos=count
    if data["bearish_engulfing"] == True:
      candle="bearish_engulfing"
      pos=count
    if data["hammer"] == True:
      candle="hammer"
      pos=count
    if data["inverted_hammer"] == True:
      candle="inverted_hammer"
      pos=count
    if data["shooting_star"] == True:
      candle="shooting_star"
      pos=count
    if data["hanging_man"] == True:
      candle="hanging_man"
      pos=count
    if data["doji"] == True:
      candle="doji"
      pos=count
    if data["dragonfly_doji"] == True:
      candle="dragonfly_doji"
      pos=count
    if data["bearish_harami"] == True:
      candle="bearish_harami"
      pos=count
    if data["star"] == True:
      candle="star"
      pos=count
    if data["morning_star_doji"] == True:
      candle="morning_star_doji"
      pos=count
    count = count+1
  
  return candle,pos
    # await asyncio.sleep(1)

async def sartagy(iq,Actives):
  con(iq = iq, checkConnection = True)
  print("For=",Actives)
  pair=Actives
  Actives=pd.read_csv("candlesdata/"+"l_"+str(Actives)+".csv")
  Actives.columns=["index","values"]
  Actives = Actives["values"].tolist()
  print(Actives)
  trend="Nan"
  miner="Nan"
  trend_anaylzer="Nan"
  pivot=0
  pivot1=0
  pivot2=0
  candle=""
  pos=0
  def closest(lst, K):
      pivot=lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]
      index = lst.index(pivot)
      index2 = index + 1
      index1 = index - 1
      # print(index1, index, index2)
      pivot1 = lst[index1]
      pivot2 = lst[index2]
        # print(pivot1, pivot, pivot2)
      return pivot1, pivot, pivot2
  expirations_mode = 1
  Money=1
  martaingale=0
  win=0
  tradecount=0
  Bets=[]
  
  while True:
    print("Money:",Money)
    remaning_time = iq.get_remaning(expirations_mode)
    purchase_time = remaning_time - 30
    print('For '+str(pair)+' ' +str(purchase_time))
    
    if purchase_time == 40:
        d = iq.get_candles(pair, 60, 3, time.time())
        current_close = d[2]["close"]
        prev_close = d[1]["close"]
        prev_open = d[2]["open"]
        print('For '+str(pair)+' ' +str(current_close))
        await asyncio.sleep(2)
        pivot1,pivot,pivot2=closest(Actives, current_close)
        await asyncio.sleep(1)
        print('For '+str(pair)+' ' +str(pivot1))
        print('For '+str(pair)+' ' +str(pivot))
        print('For '+str(pair)+' ' +str(pivot2))
        await asyncio.sleep(1)
        trend_anaylzer,trend,miner = await movingaverage(iq,pair)
        # true_low, buying_pre,true_hig, selling_pre =await pressure(iq,pair)
        if tradecount == 1:
          try:
            if Bets[-1]=="buy" and prev_close>current_close:
              win=-1
            elif Bets[-1]=="sell" and prev_close<current_close:
              win=-1
            elif Bets[-1]=="sell" or Bets[-1]=="buy"and prev_close==current_close:
              win=0
            else:
              win=1
            print("last_bet=",Bets[-1],"/",win)
            if win <0:
              martaingale=Money*1.75
              Money=martaingale
            elif win == 0:
              Money=Money
            else:
              Money=2
            tradecount==0
          except:
            print("NO TRADE FOR MARTINGALE")
          
        await asyncio.sleep(1)
    if purchase_time == 31:
        candle,pos = await patterns(iq,pair)
        await asyncio.sleep(0.5)
        print("trend_analyzer",trend_anaylzer,"trend:",trend,"miner",miner ,"--->",pair)
        print("candle",candle,"position",pos)
        # print(true_low, buying_pre,true_hig, selling_pre)
        
        #continuation if the uptrend
        if(trend_anaylzer=="continuation" and trend=="up" and miner=="up" ):
          print("continuation")
          id=higher(iq,Money,pair)
          # win=iq.check_win_v3(id)
          Bets.append("buy")
          tradecount=1
        if(trend_anaylzer=="continuation" and trend=="up" and miner=="down" ):
          print("continuation")
          id=lower(iq,Money,pair)
          # win=iq.check_win_v3(id)
          Bets.append("sell")
          tradecount=1
        
        #retracement of the uptrend
        if(trend_anaylzer=="retracement" and trend=="up" and miner=="up"  ):
          print("retracement")
          id=lower(iq,Money,pair)
          Bets.append("sell")
          tradecount=1
          # win=iq.check_win_v3(id)
        if(trend_anaylzer=="retracement" and trend=="up" and miner=="down") :
          print("retracement")
          id=higher(iq,Money,pair)
          Bets.append("buy")
          tradecount=1
          # win=iq.check_win_v3(id)

        #highest point of the uptrend
        if(trend_anaylzer=="higher point" and trend=="up" and miner=="up" ):
          print("highest point on market")
          id=lower(iq,Money,pair)
          Bets.append("sell")
          tradecount=1
          # win=iq.check_win_v3(id)
        if(trend_anaylzer=="higher point" and trend=="up" and miner=="down" ):
          print("highest point on market")
          id=higher(iq,Money,pair)
          Bets.append("buy")
          tradecount=1
          # win=iq.check_win_v3(id)

        #entry point of the uptrend
        if(trend_anaylzer=="entry" and trend == "up" and miner == "up" ):
          id=higher(iq,Money,pair)
          Bets.append("buy")
          tradecount=1
          # win=iq.check_win_v3(id)
          print("colse to the entry and buy")
        if(trend_anaylzer=="entry" and trend == "up" and miner == "down" ):
          print("colse to the entry and it may breakout")
          id=lower(iq,Money,pair)
          Bets.append("sell")
          tradecount=1
          # win=iq.check_win_v3(id)

        #continuation if the downtrend
        if(trend_anaylzer=="continuation" and trend=="down" and miner=="dowmn" ):
          print("continuation")
          id=lower(iq,Money,pair)
          Bets.append("sell")
          tradecount=1
          # win=iq.check_win_v3(id)
        if(trend_anaylzer=="continuation" and trend=="down" and miner=="up" ):
          print("continuation")
          id=higher(iq,Money,pair)
          Bets.append("buy")
          tradecount=1
          # win=iq.check_win_v3(id)

        #retracement if the downtrend
        if(trend_anaylzer=="retracement" and trend=="down" and miner=="down" ):
          print("retracement")
          id=lower(iq,Money,pair)
          Bets.append("sell")
          tradecount=1
          # win=iq.check_win_v3(id)
        if(trend_anaylzer=="retracement" and trend=="down" and miner=="up" ):
          print("retracement")
          id=higher(iq,Money,pair)
          Bets.append("buy")
          tradecount=1
          # win=iq.check_win_v3(id)

        #higher point if the downtrend
        if(trend_anaylzer=="higher point" and trend=="down" and miner=="down" ):
          print("highest point on market")
          id=higher(iq,Money,pair)
          Bets.append("buy")
          tradecount=1
          # win=iq.check_win_v3(id)
        if(trend_anaylzer=="higher point" and trend=="down" and miner=="up"):
          print("highest point on market")
          id=lower(iq,Money,pair)
          Bets.append("sell")
          tradecount=1
          # win=iq.check_win_v3(id)

        #entry point if the downtrend
        if(trend_anaylzer=="entry" and trend == "down" and miner == "down" ):
          id=lower(iq,Money,pair)
          Bets.append("sell")
          tradecount=1
          # win=iq.check_win_v3(id)
          print("colse to the entry to sell")
        if(trend_anaylzer=="entry" and trend == "down" and miner == "up" ):
          id=higher(iq,Money,pair)
          Bets.append("buy")
          tradecount=1
          # win=iq.check_win_v3(id)
          print("colse to the entry and it may breakout")
        if tradecount == 1:
          tradecount == 1
        else:
          tradecount=0
        await asyncio.sleep(1) 
    await asyncio.sleep(1)
    



def higher(iq,Money,pair):
    done,id = iq.buy(Money,pair,"call",1)
    if not done:
        print('Error call')
        print(done, id)
        exit(0)
    return id


def lower(iq,Money,pair):
    done,id = iq.buy(Money,pair,"put",1)
    if not done:
        print('Error put')
        print(done, id)
        exit(0)
    return id

async def pressure(iq,pair):
    candle = iq.get_candles(pair, 60, 3, time.time())
    buying_pre = 0
    current_low = candle[1]["min"]
    perivious_low = candle[0]["min"]
    current_close = candle[1]["close"]
    perivious_close = candle[0]["close"]
    true_low = min(current_low, perivious_low)
    buying_pre = abs(current_close - true_low)
    # print(true_low, buying_pre, current_close, perivious_close)
    current_hig = candle[1]["max"]
    perivious_hig = candle[0]["max"]
    true_hig = max(current_hig, perivious_hig)
    selling_pre = abs(current_close - true_hig)
    # print(true_hig, selling_pre, current_close, perivious_close)
    return true_low, buying_pre,true_hig, selling_pre




task1 = con()
pairs = ['EURUSD','EURJPY',"EURGBP","GBPUSD"]
loop = asyncio.get_event_loop()
try:
  # for pair in pairs:
  # asyncio.ensure_future(fibanoci(task1,pairs[0]))
  # asyncio.ensure_future(patterns(task1,pairs[0]))
    # asyncio.ensure_future(sartagy(task1,pair))
  # asyncio.ensure_future(sartagy(task1,pairs[1]))
  # asyncio.ensure_future(sartagy(task1,pairs[2]))
  asyncio.ensure_future(sartagy(task1,pairs[3]))
  loop.run_forever()
except KeyboardInterrupt:
  pass
finally:
  print("closing bot...")
  loop.close()

# def launch_event_loops():
#     task1 = con()
#     pairs = ['EURUSD','EURJPY',"EURGBP"]
#      # get a new event loop
#     loop = asyncio.new_event_loop()

#     # set the event loop for the current thread
#     asyncio.set_event_loop(loop)
#     try:
#       # for pair in pairs:
#       # asyncio.ensure_future(fibanoci(task1,pairs[0]))
#       # asyncio.ensure_future(patterns(task1,pairs[0]))
#         # asyncio.ensure_future(sartagy(task1,pair))
#       # asyncio.ensure_future(sartagy(task1,pairs[1]))
#       # asyncio.ensure_future(sartagy(task1,pairs[2]))
#       # asyncio.ensure_future(sartagy(task1,pairs[0]))
#       loop.run_until_complete(sartagy(task1,pairs[0]))
#       loop.run_until_complete(sartagy(task1,pairs[1]))
#       # loop.run_until_complete(sartagy(task1,pairs[1]))
#       # loop.run_forever()
#     except KeyboardInterrupt:
#       pass
#     finally:
#       print("closing bot...")
#       loop.close()


# if __name__ == "__main__":
#     t1 = Thread(target=launch_event_loops)
#     t2 = Thread(target=launch_event_loops)

#     t1.start()
#     t2.start()

#     print("Is event loop running in thread {0} = {1}\n".format(current_thread().getName(),
#                                                          asyncio.get_event_loop().is_running()))

#     t1.join()
#     t2.join()