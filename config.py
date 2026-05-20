# Daily Scans
MB_MOVERS = '( {33489} (  daily close >=  1 day ago close *  1.02 and daily volume >= 1 day ago volume ) )'
EIGHT_5DAYS = '( {33489} (  daily close >=  5 days ago close *  1.08 ) )'
NEG_MB_MOVERS = '( {33489} (  daily close <=  1 day ago close *  0.98 and daily volume >= 1 day ago volume ) )'
NEG_EIGHT_5DAYS = '( {33489} (  daily close <=  5 days ago close *  0.92 ) )'

# EP Scan
GAP_UP = '( {cash} ( daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 200000000 and daily open > 1 day ago close * 1.03 and( {166311} not( daily close > 0 ) ) ) )'

# MB Setup
ANT = '( {33489} (  daily "close - 1 candle ago close / 1 candle ago close * 100" <=  0.5 and  daily "close - 1 candle ago close / 1 candle ago close * 100" >=  -0.5 ) )'

# IPO Setups
IPOBASES = '( {cash} ( ( {cash} not( 12 months ago close > 0 ) ) and latest "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and latest "close - 1 candle ago close / 1 candle ago close * 100" => -1 and market cap > 5000 ) )'
IPO_IB = '( {cash} ( ( {cash} not( 12 months ago close > 0 ) ) and daily high <= 1 day ago high and daily low >= 1 day ago low and market cap > 5000 ) )'

clauses = {
    "MB TODAY": [MB_MOVERS],
    "EIGHT_5DAYS": [EIGHT_5DAYS],
    "NEG MB TODAY": [NEG_MB_MOVERS],
    "NEG_EIGHT_5DAYS": [NEG_EIGHT_5DAYS],
    "MB": [ANT],
    "EP": [GAP_UP],
    "IPO": [IPOBASES, IPO_IB],
}
