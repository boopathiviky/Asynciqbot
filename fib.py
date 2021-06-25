from datetime import datetime
from time import time,sleep
import sys
from iqoptionapi.stable_api import IQ_Option
import json

iq = IQ_Option("boopathiviky@gmail.com","ex$4,X.,tzDU5b?")
iq.connect()

if iq.check_connect():
    print("sucess")
else:
    print("error in connection")
    input("\n\n Enter the Pair")
    sys.exit()
genral={"pair":"","timeframe":5 ,"vmax":0 ,"vmin":1000, "value":0 ,"max":"max","min":"min","dec":0}
genral["pair"]="EURUSD"
genral["value"]=100
genral["timeframe"]=5

tipo =""
if tipo.upper()=="F":
    genral["max"]="close"
    genral["min"]="close"
def fibannoci():
    # global genral
    values=iq.get_candles(genral["pair"].strip(), (genral["timeframe"]*60),int(genral["value"]),time())
    # values = iq.get_candles("EURUSD",300,100,time.time())
    genral["dec"] = 7 - len(str(values[-1]["close"]).split(".")[0])
    for x in values:
        if x[genral["max"]] >genral["vmax"]: genral["vmax"] = x[genral["max"]]
        if x[genral["min"]] <genral["vmin"]: genral["vmin"] = x[genral["min"]]

    diff = genral["vmax"]- genral["vmin"]

    result ={
        "00.0%":round(genral["vmax"], genral["dec"]),
        "23.0%":round(genral["vmax"]- diff * 0.236, genral["dec"]),
        "38.2%":round(genral["vmax"] - diff * 0.382, genral["dec"]),
        "50.0%":round(genral["vmax"] - diff * 0.5, genral["dec"]),
        "61.8%":round(genral["vmax"] - diff * 0.618, genral["dec"]),
        "100.0%":round(genral["vmin"] , genral["dec"])
    }
    diff = 100
    d = 0
    proximo = ""
    proxi=""
    for name in result:
        test =values[-1]["close"] - result[name]
        if abs(test) <abs(diff) : diff,proximo =test,name
        if abs(test) >abs(diff) : diff,proxi=test,name
    
    return proximo,values[-1],result,proxi

proximo_de,vela ,fibo,proxi = fibannoci()
print(json.dumps(fibo,indent=1))

sec = time()
while True:
    proximo_de,vela ,fibo,proxi = fibannoci()

    tax_atual =round(vela["close"],genral["dec"])
    f=fibo[proxi]
    s=fibo[proximo_de]
    a=f-s
    per=tax_atual/a*100
    print(round(time()-sec,2 ),"| fib_percent",proximo_de,"| traget",tax_atual,"/",fibo[proximo_de],"/",f,"  ",end="\r")
    sec=time()