# to find a trend
    if(candle["MA_20"].iloc[-1]>candle["MA_50"].iloc[-1]):
      trend="up"
      #to find a level 1 trend
      if(candle["MADIFF"].iloc[-1]<=100):
        #trend with continuation or retracement
        if(candle["EMADIFF"].iloc[-1]<=20):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
          #trend is new
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="NEW TREND IS FORMED RECENTLY"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="MAY BE IT AGAIN GO BACK"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
          #trend is new
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="ITS MAKE A TREND IN MINUTES"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="CONFORMLY TO MAKE A NEW TREND"
        #to find a level 1 trend with middle point
        if(candle["EMADIFF"].iloc[-1]<=60):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="STRONG CONTINUATION OF NEW TREND"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="STRONG RETRACMENT OF NEW TREND"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="I THINK BAD TREND GOES ON"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="ITS MAY RETRACE AND CCAUES BRAKOUT"
        #to find a level 1 trend with final point
        if(candle["EMADIFF"].iloc[-1]<=100):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="THIS TREND IS STROGER AND READY TO RETRACEMENT"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="THIS TREND IS STROGER AND BEGIN TO RETRACEMENT"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAY COSOLIDATED MARKET SUDENLY"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAY COSOLIDATED BREAKOUT MARKET SUDENLY"
        if(candle["EMADIFF"].iloc[-1]>100):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="AT HIGHT POINT EMA IT SHOULD BE RETRACED"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT BEGIN RETRACEMET"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAKE A NEW TREND IN FUTURE"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT CONFORM NEW TREND FUTURE"
      #level 2 of trend 
      elif(candle["MADIFF"].iloc[-1]>100 and candle["MADIFF"].iloc[-1]<=200):
        #trend with continuation or retracement
        if(candle["EMADIFF"].iloc[-1]<=20):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
          #trend is new
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="NEW TREND IS FORMED RECENTLY FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="MAY BE IT AGAIN GO BACK FOR LEVEL 2"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
          #trend is new
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="ITS MAKE A TREND IN MINUTES FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="CONFORMLY TO MAKE A NEW TREND FOR LEVEL 2"
        #to find a level 1 trend with middle point
        if(candle["EMADIFF"].iloc[-1]<=60):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="STRONG CONTINUATION OF NEW TREND FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="STRONG RETRACMENT OF NEW TREND FOR LEVEL 2"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="I THINK BAD TREND GOES ON FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="ITS MAY RETRACE AND CCAUES BRAKOUT FOR LEVEL 2"
        #to find a level 1 trend with final point
        if(candle["EMADIFF"].iloc[-1]<=100):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="THIS TREND IS STROGER AND READY TO RETRACEMENT FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="THIS TREND IS STROGER AND BEGIN TO RETRACEMENT FOR LEVEL 2"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAY COSOLIDATED MARKET SUDENLY FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAY COSOLIDATED BREAKOUT MARKET SUDENLY FOR LEVEL 2"
        if(candle["EMADIFF"].iloc[-1]>100):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="AT HIGHT POINT EMA IT SHOULD BE RETRACED FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT BEGIN RETRACEMET FOR LEVEL 2"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAKE A NEW TREND IN FUTURE FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT CONFORM NEW TREND FUTURE FOR LEVEL 2"
      elif(candle["MADIFF"].iloc[-1]>200 and candle["MADIFF"].iloc[-1]<=300):
        #trend with continuation or retracement
        if(candle["EMADIFF"].iloc[-1]<=20):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
          #trend is new
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="NEW TREND IS FORMED RECENTLY FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="MAY BE IT AGAIN GO BACK FOR LEVEL 3"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
          #trend is new
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="ITS MAKE A TREND IN MINUTES FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="CONFORMLY TO MAKE A NEW TREND FOR LEVEL 3"
        #to find a level 1 trend with middle point
        if(candle["EMADIFF"].iloc[-1]<=60):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="STRONG CONTINUATION OF NEW TREND FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="STRONG RETRACMENT OF NEW TREND FOR LEVEL 3"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="I THINK BAD TREND GOES ON FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="ITS MAY RETRACE AND CCAUES BRAKOUT FOR LEVEL 3"
        #to find a level 1 trend with final point
        if(candle["EMADIFF"].iloc[-1]<=100):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="THIS TREND IS STROGER AND READY TO RETRACEMENT FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="THIS TREND IS STROGER AND BEGIN TO RETRACEMENT FOR LEVEL 3"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAY COSOLIDATED MARKET SUDENLY FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAY COSOLIDATED BREAKOUT MARKET SUDENLY FOR LEVEL 3"
        if(candle["EMADIFF"].iloc[-1]>100):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="AT HIGHT POINT EMA IT SHOULD BE RETRACED FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT BEGIN RETRACEMET FOR LEVEL 3"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAKE A NEW TREND IN FUTURE FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT CONFORM NEW TREND FUTURE FOR LEVEL 3"
      elif(candle["MADIFF"].iloc[-1]>300):
        trend_anaylzer="trend exhasted"
    if(candle["MA_20"].iloc[-1]<candle["MA_50"].iloc[-1]):
      trend="down"
      if(candle["MADIFF"].iloc[-1]<=100):
        #trend with continuation or retracement
        if(candle["EMADIFF"].iloc[-1]<=20):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
          #trend is new
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="NEW TREND IS FORMED RECENTLY"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="MAY BE IT AGAIN GO BACK"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
          #trend is new
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="ITS MAKE A TREND IN MINUTES"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="CONFORMLY TO MAKE A NEW TREND"
        #to find a level 1 trend with middle point
        if(candle["EMADIFF"].iloc[-1]<=60):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="STRONG CONTINUATION OF NEW TREND"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="STRONG RETRACMENT OF NEW TREND"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="I THINK BAD TREND GOES ON"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="ITS MAY RETRACE AND CCAUES BRAKOUT"
        #to find a level 1 trend with final point
        if(candle["EMADIFF"].iloc[-1]<=100):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="THIS TREND IS STROGER AND READY TO RETRACEMENT"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="THIS TREND IS STROGER AND BEGIN TO RETRACEMENT"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAY COSOLIDATED MARKET SUDENLY"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAY COSOLIDATED BREAKOUT MARKET SUDENLY"
        if(candle["EMADIFF"].iloc[-1]>100):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="AT HIGHT POINT EMA IT SHOULD BE RETRACED"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT BEGIN RETRACEMET"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAKE A NEW TREND IN FUTURE"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT CONFORM NEW TREND FUTURE"
      #level 2 of trend 
      elif(candle["MADIFF"].iloc[-1]>100 and candle["MADIFF"].iloc[-1]<=200):
        #trend with continuation or retracement
        if(candle["EMADIFF"].iloc[-1]<=20):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
          #trend is new
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="NEW TREND IS FORMED RECENTLY FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="MAY BE IT AGAIN GO BACK FOR LEVEL 2"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
          #trend is new
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="ITS MAKE A TREND IN MINUTES FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="CONFORMLY TO MAKE A NEW TREND FOR LEVEL 2"
        #to find a level 1 trend with middle point
        if(candle["EMADIFF"].iloc[-1]<=60):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="STRONG CONTINUATION OF NEW TREND FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="STRONG RETRACMENT OF NEW TREND FOR LEVEL 2"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="I THINK BAD TREND GOES ON FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="ITS MAY RETRACE AND CCAUES BRAKOUT FOR LEVEL 2"
        #to find a level 1 trend with final point
        if(candle["EMADIFF"].iloc[-1]<=100):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="THIS TREND IS STROGER AND READY TO RETRACEMENT FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="THIS TREND IS STROGER AND BEGIN TO RETRACEMENT FOR LEVEL 2"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAY COSOLIDATED MARKET SUDENLY FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAY COSOLIDATED BREAKOUT MARKET SUDENLY FOR LEVEL 2"
        if(candle["EMADIFF"].iloc[-1]>100):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="AT HIGHT POINT EMA IT SHOULD BE RETRACED FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT BEGIN RETRACEMET FOR LEVEL 2"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAKE A NEW TREND IN FUTURE FOR LEVEL 2"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT CONFORM NEW TREND FUTURE FOR LEVEL 2"
      elif(candle["MADIFF"].iloc[-1]>200 and candle["MADIFF"].iloc[-1]<=300):
        #trend with continuation or retracement
        if(candle["EMADIFF"].iloc[-1]<=20):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
          #trend is new
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="NEW TREND IS FORMED RECENTLY FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="MAY BE IT AGAIN GO BACK FOR LEVEL 3"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
          #trend is new
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="ITS MAKE A TREND IN MINUTES FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="CONFORMLY TO MAKE A NEW TREND FOR LEVEL 3"
        #to find a level 1 trend with middle point
        if(candle["EMADIFF"].iloc[-1]<=60):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="STRONG CONTINUATION OF NEW TREND FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="STRONG RETRACMENT OF NEW TREND FOR LEVEL 3"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="I THINK BAD TREND GOES ON FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="ITS MAY RETRACE AND CCAUES BRAKOUT FOR LEVEL 3"
        #to find a level 1 trend with final point
        if(candle["EMADIFF"].iloc[-1]<=100):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="THIS TREND IS STROGER AND READY TO RETRACEMENT FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="THIS TREND IS STROGER AND BEGIN TO RETRACEMENT FOR LEVEL 3"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAY COSOLIDATED MARKET SUDENLY FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAY COSOLIDATED BREAKOUT MARKET SUDENLY FOR LEVEL 3"
        if(candle["EMADIFF"].iloc[-1]>100):
          if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="AT HIGHT POINT EMA IT SHOULD BE RETRACED FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT BEGIN RETRACEMET FOR LEVEL 3"
          elif(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
            if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT MAKE A NEW TREND IN FUTURE FOR LEVEL 3"
            if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
              trend_anaylzer="IT CONFORM NEW TREND FUTURE FOR LEVEL 3"



# if(candle["MA_20"].iloc[-1]>candle["MA_50"].iloc[-1]):
    #   trend="up"
    #   if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2]):
    #     if(candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2]):
    #       #enter to up trend 
    #       if(candle["EMADIFF"].iloc[-1]<30 and candle["MADIFF"].iloc[-1]<100):
    #         print(" you are enter into new trend")
    #         trend_anaylzer="you are enter into new trend"
    #       if(candle["EMADIFF"].iloc[-1]<60 and candle["MADIFF"].iloc[-1]<200):
    #           print(" you are enter into medium trend")
    #           trend_anaylzer="you are enter into medium trend"
    #       if(candle["EMADIFF"].iloc[-1]<150 and candle["MADIFF"].iloc[-1]<300):
    #         print(" you are enter into final trend")
    #         trend_anaylzer="you are enter into final trend"
    #   if(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2]):
    #     if(candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2]):
    #        #enter to up trend 
    #       if(candle["EMADIFF"].iloc[-1]<30 and candle["MADIFF"].iloc[-1]<100):
    #         print(" you are make into new trend")
    #         trend_anaylzer="you are enter into new trend"
    #       if(candle["EMADIFF"].iloc[-1]<60 and candle["MADIFF"].iloc[-1]<200):
    #           print(" you are retracement")
    #           trend_anaylzer="you are retracement"
    #       if(candle["EMADIFF"].iloc[-1]<150 and candle["MADIFF"].iloc[-1]<300):
    #         print(" you are it may break out trend reach highest point on trend")
    #         trend_anaylzer="you are it may break out trend reach highest point on trend"
    # for down trend 
    # if(candle["MA_20"].iloc[-1]<candle["MA_50"].iloc[-1]):
    #   trend="down"
    #       #enter to down trend 
    #   if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2] and candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2] and candle["EMADIFF"].iloc[-1]<30 and candle["MADIFF"].iloc[-1]<100):
    #     print(" you are enter into new trend")
    #     trend_anaylzer="you are enter into new trend"
    #   if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2] and candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2] and candle["EMADIFF"].iloc[-1]<60 and candle["MADIFF"].iloc[-1]<200):
    #       print(" you are enter into medium trend")
    #       trend_anaylzer="you are enter into medium trend"
    #   if(candle["MADIFF"].iloc[-1]>candle["MADIFF"].iloc[-2] and candle["EMADIFF"].iloc[-1]>candle["EMADIFF"].iloc[-2] and candle["EMADIFF"].iloc[-1]<150 and candle["MADIFF"].iloc[-1]<300):
    #     print(" you are enter into final trend")
    #     trend_anaylzer="you are enter into final trend"
    #     #enter to up trend 
    #   if(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2] and candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2] and candle["EMADIFF"].iloc[-1]<30 and candle["MADIFF"].iloc[-1]<100):
    #     print(" you are make into new trend")
    #     trend_anaylzer="you are make into new trend"
    #   if(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2] and candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2] and candle["EMADIFF"].iloc[-1]<60 and candle["MADIFF"].iloc[-1]<200):
    #       print(" you are retracement")
    #       trend_anaylzer=" you are retracement"
    #   if(candle["MADIFF"].iloc[-1]<candle["MADIFF"].iloc[-2] and candle["EMADIFF"].iloc[-1]<candle["EMADIFF"].iloc[-2] and candle["EMADIFF"].iloc[-1]<150 and candle["MADIFF"].iloc[-1]<300):
    #     print(" you are it may break out trend reach highest point on trend")
    #     trend_anaylzer="you are it may break out trend reach highest point on trend"