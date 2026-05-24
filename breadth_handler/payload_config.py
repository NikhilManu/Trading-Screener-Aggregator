DASHBOARD_URL = "https://chartink.com/dashboard/180916"

WIDGET_URL = "https://chartink.com/widget/process"

QUERY = (
    "select groupcount({cash} 1 where daily close > daily ema(daily close, 20))"
    " / groupcount({cash} 1) * 100 as 'MR20',"
    " groupsum({cash} Daily \"close - 1 candle ago close / 1 candle ago close * 100\" >= 4"
    " where daily volume > 1 day ago volume) as 'U4',"
    " groupsum({cash} Daily \"close - 1 candle ago close / 1 candle ago close * 100\" <= -4"
    " where daily volume > 1 day ago volume) as 'D4',"
    " groupcount({cash} 1 where daily close >= 5 days ago close * 1.20) as 'W20',"
    " groupcount({cash} 1) as 'UNIVERSE'"
    " WHERE({cash} (daily close >= 10 and daily close <= 20000 and daily {custom_indicator_191409_start}\"sma(volume, 10) * close\"{custom_indicator_191409_end} >= 100000000 and ({166311} not(daily close > 0))))"
    " ORDER BY 1 desc"
)