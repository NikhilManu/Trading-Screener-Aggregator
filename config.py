# Situational Awareness scan
FIFTEEN_5DAYS = "( {cash} ( latest sma( latest volume , 20 ) * latest close >= 100000000 and latest close >= 5 days ago close * 1.15 ) )"
FIFTY_40DAYS = "( {cash} ( latest sma( latest volume , 20 ) * latest close >= 100000000 and latest close >= 50 days ago close * 1.5 ) )"

# Setups
IPOBASES = '( {cash} ( ( {cash} not( 12 months ago close > 0 ) ) and latest "close - 1 candle ago close / 1 candle ago close * 100" < 1 and latest "close - 1 candle ago close / 1 candle ago close * 100" > -1 and latest volume * latest close >= 10000000 and market cap > 100 ) )'
VELOCITY_SETUPS = '( {cash} ( ( {cash} ( latest sma( latest volume , 20 ) * latest close >= 150000000 and ( latest close <= 10000 ) and latest "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and latest "close - 1 candle ago close / 1 candle ago close * 100" >= -1 and latest sma( close,7 ) / latest sma( close,65 ) >= 1.05 ) ) ) )'
TTT_SETUPS = '( {cash} ( ( {cash} ( latest sma( latest volume , 20 ) * latest close >= 100000000 and latest "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and 1 day ago "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and 2 days ago "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and latest "close - 1 candle ago close / 1 candle ago close * 100" >= -1 and 1 day ago "close - 1 candle ago close / 1 candle ago close * 100" >= -1 and 2 days ago "close - 1 candle ago close / 1 candle ago close * 100" >= -1 and latest sma( close,7 ) / latest sma( close,65 ) >= 1.05 and( {166311} not( latest close > 0 ) ) ) ) ) ) '
TTT_ATR = "( {cash} ( ( {cash} ( latest sma( latest volume , 20 ) * latest close >= 100000000 and latest sma( close,7 ) / latest sma( close,65 ) >= 1.05 and latest max( 3 , latest high ) - latest min( 3 , latest low ) < latest avg true range( 14 ) and( {166311} not( latest close > 0 ) ) ) ) ) )"
TTT_IB = "( {cash} ( ( {cash} ( latest sma( latest volume , 20 ) * latest close >= 100000000 and latest sma( close,7 ) / latest sma( close,65 ) >= 1.05 and latest high < 2 days ago high and latest low > 2 days ago low and 1 day ago high < 2 days ago high and 1 day ago low > 2 days ago low and latest max( 2 , latest high ) - latest min( 2 , latest low ) <= latest avg true range( 14 ) ) ) and( {166311} not( latest close > 0 ) ) ) )"

clauses = {
    "IPO": [IPOBASES],
    "TTT_VELOCITY": [TTT_SETUPS],
    "TTT_ATR_IB": [TTT_ATR, TTT_IB],
    "15%+ Movers": [FIFTEEN_5DAYS],
    "50%+ Movers": [FIFTY_40DAYS],
}
