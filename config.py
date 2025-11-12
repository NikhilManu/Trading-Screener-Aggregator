# Weekend Scans
ONE_MONTH = '( {cash} ( daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 200000000 and latest close >= 21 days ago close * 1.30 and( {166311} not( latest close > 0 ) ) ) )'

# Daily Scan
FIVE_5DAYS = "( {cash} ( market cap >= 70000 and latest close >= 5 days ago close * 1.05 and( {166311} not( latest close > 0 ) ) ) )"
FIFTEEN_5DAYS = '( {cash} ( daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 200000000 and latest close >= 5 days ago close * 1.15 and( {166311} not( latest close > 0 ) ) ) )'
SIX_1DAY = '( {cash} ( daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 200000000 and daily close >= 1 day ago close * 1.06 and daily volume > 1 day ago volume and( {166311} not( daily close > 0 ) ) ) )'
GAP_UP = '( {cash} ( daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 200000000 and daily open > 1 day ago close * 1.04 and( {166311} not( daily close > 0 ) ) ) )'

# IPO Setups
IPOBASES = '( {cash} ( ( {cash} not( 12 months ago close > 0 ) ) and latest "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and latest "close - 1 candle ago close / 1 candle ago close * 100" => -1 and market cap > 5000 ) )'
IPO_IB = '( {cash} ( ( {cash} not( 12 months ago close > 0 ) ) and daily high <= 1 day ago high and daily low >= 1 day ago low and market cap > 5000 ) )'

# MB
DIB_TI65 = '( {cash} ( daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 200000000 and daily {custom_indicator_190070_start}"sma(  close , 7 ) /  sma(  close , 65 )"{custom_indicator_190070_end} >= 1.05 and daily high < 1 day ago high and daily low > 1 day ago low and 1 day ago high < 2 days ago high and 1 day ago low > 2 days ago low and( {166311} not( daily close > 0 ) ) ) )'
DIB_MOM = '( {cash} ( daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 200000000 and daily {custom_indicator_190151_start}"close /  min( 30 ,  close )"{custom_indicator_190151_end} >= 1.20 and daily high < 1 day ago high and daily low > 1 day ago low and 1 day ago high < 2 days ago high and 1 day ago low > 2 days ago low and( {166311} not( daily close > 0 ) ) ) )'
T_TI65 = '( {cash} ( daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 200000000 and daily {custom_indicator_190070_start}"sma(  close , 7 ) /  sma(  close , 65 )"{custom_indicator_190070_end} >= 1.05 and daily "close - 1 candle ago close / 1 candle ago close * 100" <= 0.4 and daily "close - 1 candle ago close / 1 candle ago close * 100" >= -0.4 and( {166311} not( daily close > 0 ) ) ) )'
T_MOM = '( {cash} ( daily {custom_indicator_190145_start}"volume *  close"{custom_indicator_190145_end} >= 200000000 and daily {custom_indicator_190151_start}"close /  min( 30 ,  close )"{custom_indicator_190151_end} >= 1.20 and daily "close - 1 candle ago close / 1 candle ago close * 100" <= 0.4 and daily "close - 1 candle ago close / 1 candle ago close * 100" >= -0.4 and( {166311} not( daily close > 0 ) ) ) )'

# FHP
FHP_TTT = '( {cash} ( market cap >= 70000 and daily "close - 1 candle ago close / 1 candle ago close * 100" <= 0.5 and daily "close - 1 candle ago close / 1 candle ago close * 100" >= -0.5 and 1 day ago "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and 1 day ago "close - 1 candle ago close / 1 candle ago close * 100" >= -1 and 2 days ago "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and 2 days ago "close - 1 candle ago close / 1 candle ago close * 100" >= -1 and( {166311} not( daily close > 0 ) ) ) )'
FHP_DIB = '( {cash} ( market cap >= 70000 and daily high < 2 days ago high and daily low > 2 days ago low and 1 day ago high < 2 days ago high and 1 day ago low > 2 days ago low and( {166311} not( daily close > 0 ) ) ) )'

clauses = {
    "DAILY SCAN": [FIFTEEN_5DAYS, SIX_1DAY, GAP_UP],
    "WEEKEND SCAN": [ONE_MONTH],
    "IPO": [IPOBASES, IPO_IB],
    "MB": [DIB_MOM, DIB_TI65, T_MOM, T_TI65],
    "FHP SETUP": [FHP_TTT, FHP_DIB],
    "FHP STUDY": [FIVE_5DAYS]
}
