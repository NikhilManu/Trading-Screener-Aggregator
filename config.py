ANT = '( {cash} ( latest sma( latest volume , 20 ) * latest close >= 30000000 and latest "close - 1 candle ago close / 1 candle ago close * 100" <= .5 and latest "close - 1 candle ago close / 1 candle ago close * 100" >= -.5 and latest close >= latest max( 250 , latest close ) * 0.75 and latest close >= latest min( 250 , latest close ) * 1.3 and latest close >= latest sma( latest close , 50 ) ) ) '
TURNOVER = '( {cash} ( latest {custom_indicator_97318_start}"vwap *  volume"{custom_indicator_97318_end} >= latest ema( latest {custom_indicator_97318_start}"vwap *  volume"{custom_indicator_97318_end} , 20 ) * 3 and latest close > 10 and latest close <= 5000 and market cap >= 300 and latest {custom_indicator_59995_start}"(  sma(  close , 50 ) *  sma(  volume , 50 ) ) / 10000000"{custom_indicator_59995_end} >= 5 and latest sma( latest volume , 20 ) * latest close >= 30000000 ) )'

BIGMOVERS = '( {cash} ( latest sma( latest volume , 20 ) * latest close >= 40000000 and latest close - 1 day ago close >= 1 day ago avg true range( 14 ) * 2 and latest volume >= latest sma( latest volume , 20 ) * 2 ) )'
TEN_DECLINE_5DAYS = '( {cash} ( latest sma( latest volume , 20 ) * latest close >= 40000000 and latest close <= 5 days ago close * 0.80 ) )'

#Deep Dive Study screeners
FIFTEEN_5DAYS = '( {cash} ( latest sma( latest volume , 20 ) * latest close >= 30000000 and latest close >= 5 days ago close * 1.2 ) )'
FIFTY_40DAYS = '( {cash} ( latest sma( latest volume , 20 ) * latest close >= 40000000 and latest close >= 40 days ago close * 1.5 ) )'
TRIPLED_252DAYS = '( {cash} ( latest max( 126 , latest high ) / latest min( 126 , latest close ) >= 3.0 and latest sma( latest volume , 20 ) * latest close >= 30000000 and latest close > 30 ) )'

IPOBASES = '( {cash} ( ( {cash} not( 12 months ago close > 0 ) ) and latest "close - 1 candle ago close / 1 candle ago close * 100" < 1 and latest "close - 1 candle ago close / 1 candle ago close * 100" > -1 and latest volume * latest close >= 10000000 and market cap > 100 ) )'

clauses = {
    'BIG MOVERS': [BIGMOVERS],
    'REVERSALS': [TEN_DECLINE_5DAYS],
    'MONEYFLOW': [FIFTEEN_5DAYS],
    'DEEPDIVE' : [FIFTY_40DAYS],
    'IPO' : [IPOBASES],
    'ANT' : [ANT],
    'STOCKS IN PLAY' : [TURNOVER]
}