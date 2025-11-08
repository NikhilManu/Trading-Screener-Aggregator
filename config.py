# Weekend Scans
ONE_MONTH = "( {cash} ( latest volume * latest close >= 100000000 and latest close >= 21 days ago close * 1.30 and( {166311} not( latest close > 0 ) ) ) )"

# Daily Scan
FIFTEEN_5DAYS = "( {cash} ( latest volume * latest close >= 100000000 and latest close >= 5 days ago close * 1.15 and( {166311} not( latest close > 0 ) ) ) )"
SIX_1DAY = "( {cash} ( daily close >= 1 day ago close * 1.06 and daily volume > daily sma( daily volume , 50 ) * 3 and latest volume * daily close >= 100000000 and( {166311} not( daily close > 0 ) ) ) )"
GAP_UP = "( {cash} ( daily open > 1 day ago close * 1.04 and latest volume * daily close >= 100000000 and( {166311} not( daily close > 0 ) ) ) )"

# IPO Setups
IPOBASES = '( {cash} ( ( {cash} not( 12 months ago close > 0 ) ) and latest "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and latest "close - 1 candle ago close / 1 candle ago close * 100" => -1 and market cap > 5000 ) )'
IPO_IB = '( {cash} ( ( {cash} not( 12 months ago close > 0 ) ) and daily high <= 1 day ago high and daily low >= 1 day ago low and market cap > 5000 ) )'

# Momentum Setups
T_ATR = '( {cash} ( ( {cash} ( latest volume * latest close >= 100000000 and daily sma( close,7 ) / daily sma( close,65 ) >= 1.05 and daily high - daily low <= daily avg true range( 14 ) / 2 and( {166311} not( daily close > 0 ) ) ) ) ) )'
DIB_SETUP = '( {cash} ( ( {cash} ( daily volume * daily close >= 100000000 and daily sma( close,7 ) / daily sma( close,65 ) >= 1.05 and daily high < 1 day ago high and daily low > 1 day ago low and 1 day ago high < 2 days ago high and 1 day ago low > 2 days ago low ) ) and( {166311} not( daily close > 0 ) ) ) )'
TT_SETUP = '( {cash} ( ( {cash} ( daily volume * daily close >= 100000000 and daily "close - 1 candle ago close / 1 candle ago close * 100" <= .5 and 1 day ago "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and daily "close - 1 candle ago close / 1 candle ago close * 100" >= -.5 and 1 day ago "close - 1 candle ago close / 1 candle ago close * 100" >= -1 and daily sma( close,7 ) / daily sma( close,65 ) >= 1.05 and( {166311} not( daily close > 0 ) ) ) ) ) )'

clauses = {
    "DAILY SCAN": [FIFTEEN_5DAYS, SIX_1DAY, GAP_UP],
    "WEEKEND SCAN": [ONE_MONTH],
    "IPO": [IPOBASES, IPO_IB],
    "MB": [T_ATR, DIB_SETUP, TT_SETUP],
}
