import asyncio
from iqoptionapi.stable_api import IQ_Option
import pandas as pd
import numpy as np
import logging
import time
import os

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
async def getcandles(iq,Actives):
    con(iq = iq, checkConnection = True)
    candles = []
    for i in range(20):
      candle=iq.get_candles(Actives, 300, 1000, time.time())
      candles +=candle
    price_data = pd.DataFrame(candles)
    # price_data=price_data.sort_values(by=["from"], inplace=True, ascending=True)
    price_data = price_data[
        [
            "from",
            "open",
            "close",
            "min",
            "max",
            "volume",
        ]
    ]
    price_data.to_csv("candlesdata/"+str(Actives)+".csv")
    print("candles: \n",price_data)
    await asyncio.sleep(10)
async def levels(pair):
  df=pd.read_csv("candlesdata/"+str(pair)+".csv")


  def isSupport(df, i):
      support = (
          df["min"][i] < df["min"][i - 1]
          and df["min"][i] < df["min"][i + 1]
          and df["min"][i + 1] < df["min"][i + 2]
          and df["min"][i - 1] < df["min"][i - 2]
      )
      return support


  def isResistance(df, i):
      resistance = (
          df["max"][i] > df["max"][i - 1]
          and df["max"][i] > df["max"][i + 1]
          and df["max"][i + 1] > df["max"][i + 2]
          and df["max"][i - 1] > df["max"][i - 2]
      )
      return resistance


  levels = []
  for i in range(2, df.shape[0] - 2):
      if isSupport(df, i):
          levels.append((i, df["min"][i]))
      elif isResistance(df, i):
          levels.append((i, df["max"][i]))

  s = np.mean(df["max"] - df["min"])

  def isFarFromLevel(l):
    return np.sum([abs(l - x) < s for x in levels]) == 0

  levels = []

  for i in range(2, df.shape[0]-2):
      if isSupport(df, i):
          l = df["min"][i]
          if isFarFromLevel(l):
              levels.append((i, l))
      elif isResistance(df, i):
          l = df["max"][i]
          if isFarFromLevel(l):
              levels.append((i, l))
      else:
          continue

  l = []
  for i in range(len(levels)):
      l.append(levels[i][1])
      l.sort(reverse=False)
  
  dl=pd.DataFrame(l)
  dl.to_csv("candlesdata/"+"l_"+str(pair)+".csv")
  print("l:",pair,"\n",l)

async def sartagy(iq,Actives):
  con(iq = iq, checkConnection = True)
  print("For=",Actives)
  while True:
   candle=iq.get_candles(Actives, 60, 500, time.time())
   price_data = pd.DataFrame(candle)
   price_data = price_data[
        [
            "from",
            "open",
            "close",
            "min",
            "max",
            "volume",
        ]
    ]
   print(price_data)
   await asyncio.sleep(1)
async def main():
    task1 = con()
    # iqcon = await task1
    pairs = ['EURUSD','EURGBP','EURJPY','AUDUSD','GBPUSD']
    for pair in pairs:
        task2 = asyncio.create_task(getcandles(task1,pair))
        task3 = asyncio.create_task(levels(pair))
   
    

asyncio.run(main())
