DASHBOARD_URL = "https://chartink.com/dashboard/180916"

WIDGET_URL = "https://chartink.com/widget/process"

QUERY = (
    "select groupcount({cash} 1 where daily close > daily ema(daily close, 20))"
    " / groupcount({cash} 1) * 100 as 'E20',"
    " groupsum({cash} Daily \"close - 1 candle ago close / 1 candle ago close * 100\" >= 2"
    " where daily volume > 1 day ago volume) as 'U2',"
    " groupsum({cash} Daily \"close - 1 candle ago close / 1 candle ago close * 100\" <= -2"
    " where daily volume > 1 day ago volume) as 'D2',"
    " groupcount({cash} 1 where daily close >= 5 days ago close * 1.10) as 'W10',"
    " groupcount({cash} 1) as 'UNIVERSE'"
    " WHERE({33489} (({166311} not(daily close > 0)))) ORDER BY 1 desc"
)