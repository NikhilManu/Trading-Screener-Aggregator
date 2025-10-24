# Weekend Scans
ONE_MONTH = "( {cash} ( latest sma( latest volume , 20 ) * latest close >= 100000000 and latest close >= 21 days ago close * 1.30 and( {166311} not( latest close > 0 ) ) ) )"
THREE_MONTH = "( {cash} ( latest sma( latest volume , 20 ) * latest close >= 100000000 and latest close >= 63 days ago close * 1.5 and( {166311} not( latest close > 0 ) ) ) )"
SIX_MONTH = "( {cash} ( latest sma( latest volume , 20 ) * latest close >= 100000000 and latest close >= 126 days ago close * 2 and( {166311} not( latest close > 0 ) ) ) )"

# Situational Awareness scan
FIFTEEN_5DAYS = "( {cash} ( latest sma( latest volume , 20 ) * latest close >= 100000000 and latest close >= 5 days ago close * 1.15 and( {166311} not( latest close > 0 ) ) ) )"
TEN_1DAY = "( {cash} ( daily close >= 1 day ago close * 1.10 and daily volume > daily sma( daily volume , 20 ) * 2 and daily sma( daily volume , 20 ) * daily close >= 100000000 and( {166311} not( daily close > 0 ) ) ) )"
GAP_UP = "( {cash} ( daily open > 1 day ago close * 1.04 and daily sma( daily volume , 20 ) * daily close >= 100000000 and( {166311} not( daily close > 0 ) ) ) )"

# Setups
IPOBASES = '( {cash} ( ( {cash} not( 12 months ago close > 0 ) ) and latest "close - 1 candle ago close / 1 candle ago close * 100" < 1 and latest "close - 1 candle ago close / 1 candle ago close * 100" > -1 and latest volume * latest close >= 10000000 and market cap > 100 ) )'
TTT_SETUPS = '( {cash} ( ( {cash} ( latest sma( latest volume , 20 ) * latest close >= 100000000 and latest "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and 1 day ago "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and 2 days ago "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and latest "close - 1 candle ago close / 1 candle ago close * 100" >= -1 and 1 day ago "close - 1 candle ago close / 1 candle ago close * 100" >= -1 and 2 days ago "close - 1 candle ago close / 1 candle ago close * 100" >= -1 and latest sma( close,7 ) / latest sma( close,65 ) >= 1.05 and( {166311} not( latest close > 0 ) ) ) ) ) ) '
TT_SETUPS = '( {cash} ( ( {cash} ( daily sma( daily volume , 20 ) * daily close >= 100000000 and daily "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and 1 day ago "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and daily "close - 1 candle ago close / 1 candle ago close * 100" >= -1 and 1 day ago "close - 1 candle ago close / 1 candle ago close * 100" >= -1 and daily sma( close,7 ) / daily sma( close,65 ) >= 1.05 and( {166311} not( daily close > 0 ) ) ) ) ) )'
TTT_ATR = "( {cash} ( ( {cash} ( latest sma( latest volume , 20 ) * latest close >= 100000000 and latest sma( close,7 ) / latest sma( close,65 ) >= 1.05 and latest max( 3 , latest high ) - latest min( 3 , latest low ) < latest avg true range( 14 ) and( {166311} not( latest close > 0 ) ) ) ) ) )"
TTT_IB = "( {cash} ( ( {cash} ( latest sma( latest volume , 20 ) * latest close >= 100000000 and latest sma( close,7 ) / latest sma( close,65 ) >= 1.05 and latest high < 2 days ago high and latest low > 2 days ago low and 1 day ago high < 2 days ago high and 1 day ago low > 2 days ago low and latest max( 2 , latest high ) - latest min( 2 , latest low ) <= latest avg true range( 14 ) ) ) and( {166311} not( latest close > 0 ) ) ) )"

clauses = {
    "IPO": [IPOBASES],
    "TTT_VELOCITY": [TTT_ATR, TTT_IB, TT_SETUPS],
    "15%+ Movers": [FIFTEEN_5DAYS],
    "10%+ Movers": [TEN_1DAY],
    "Gap Up": [GAP_UP],
    "1 Month": [ONE_MONTH],
    "3 Month": [THREE_MONTH],
    "6 Month": [SIX_MONTH],
}
