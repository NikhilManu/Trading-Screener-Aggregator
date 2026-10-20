# Daily Scans
TOP_GAINERS = '( {cash} (  daily close >=  1 day ago close *  1.04 and daily volume >= 1 day ago volume and daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 300000000) )'

EIGHT_5DAYS = '( {33489} (  daily close >=  5 days ago close *  1.08 ) )'
NEG_EIGHT_5DAYS = '( {33489} (  daily close <=  5 days ago close *  0.92 ) )'
FIFTEEN_5DAYS = '( {cash} (  daily close >=  5 days ago close *  1.15 and daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 300000000) )'
NEG_FIFTEEN_5DAYS = '( {cash} (  daily close <=  5 days ago close *  0.85 and daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 300000000) )'

#Weekly Scans
MOMENTUM_1MONTH = '( {cash} (  daily close >=  22 days ago close *  1.30 and daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 300000000) )'
MOMENTUM_3MONTH = '( {cash} (  daily close >=  66 days ago close *  1.50 and daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 300000000) )'
MOMENTUM_6MONTH = '( {cash} (  daily close >=  120 days ago close *  1.70 and daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 300000000) )'

# EP Scan
GAP_UP = '( {cash} ( daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 300000000 and daily open > 1 day ago close * 1.03 and( {166311} not( daily close > 0 ) ) ) )'

# MB Setup
ANT = '( {33489} (  daily "close - 1 candle ago close / 1 candle ago close * 100" <=  0.5 and  daily "close - 1 candle ago close / 1 candle ago close * 100" >=  -0.5 ) )'
T = '( {cash} (  daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >=  300000000 and  daily "close - 1 candle ago close / 1 candle ago close * 100" <=  1 and  daily "close - 1 candle ago close / 1 candle ago close * 100" >=  -1 and  daily close >=  daily min( 15 ,  daily close ) *  1.10 and( {166311} not(  daily close >  0 ) ) ) )'
TT = '( {cash} (  daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >=  300000000 and  daily "close - 1 candle ago close / 1 candle ago close * 100" <=  1.5 and  daily "close - 1 candle ago close / 1 candle ago close * 100" >=  -1.5 and  1 day ago "close - 1 candle ago close / 1 candle ago close * 100" <=  1.5 and  1 day ago "close - 1 candle ago close / 1 candle ago close * 100" >=  -1.5 and  daily close >=  daily min( 15 ,  daily close ) *  1.10 and( {166311} not(  daily close >  0 ) ) ) )'
REVERSAL = '( {33489} (  daily low =  daily min( 5 ,  daily low ) and(  daily open -  daily low ) >  (  daily close -  daily open ) and(  daily close -  daily low ) /  (  daily high -  daily low ) >=  0.6 ) )'

# IPO Setups
IPOBASES = '( {cash} ( ( {cash} not( 12 months ago close > 0 ) ) and latest "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and latest "close - 1 candle ago close / 1 candle ago close * 100" => -1 and daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 300000000) )'
IPO_IB = '( {cash} ( ( {cash} not( 12 months ago close > 0 ) ) and daily high <= 1 day ago high and daily low >= 1 day ago low and daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 300000000 ) )'

clauses = {
    "1 MONTH GAINERS": [MOMENTUM_1MONTH],
    "3 MONTH GAINERS": [MOMENTUM_3MONTH],
    "6 MONTH GAINERS": [MOMENTUM_6MONTH],
    "DAILY GAINERS": [TOP_GAINERS],
    "WEEKLY GAINERS": [EIGHT_5DAYS, FIFTEEN_5DAYS],
    "WEEKLY LOSERS": [NEG_FIFTEEN_5DAYS, NEG_EIGHT_5DAYS],
    "MB": [ANT],
    "ANTS": [T, TT],
    "REVERSAL": [REVERSAL],
    "EP": [GAP_UP],
    "IPO": [IPOBASES, IPO_IB],
}
