# Situational Awareness scan
FIFTEEN_5DAYS = '( {cash} ( latest sma( latest volume , 20 ) * latest close >= 30000000 and latest close >= 5 days ago close * 1.15 ) )'
FIFTY_40DAYS = '( {cash} ( latest sma( latest volume , 20 ) * latest close >= 30000000 and latest close >= 50 days ago close * 1.5 ) )'
TEN_DECLINE_5DAYS = '( {cash} ( latest sma( latest volume , 20 ) * latest close >= 30000000 and latest close <= 5 days ago close * 0.90 ) )'

#
# Setups
IPOBASES = '( {cash} ( ( {cash} not( 12 months ago close > 0 ) ) and latest "close - 1 candle ago close / 1 candle ago close * 100" < 1 and latest "close - 1 candle ago close / 1 candle ago close * 100" > -1 and latest volume * latest close >= 10000000 and market cap > 100 ) )'
MAGNITUDE_SETUPS = '( {cash} ( 1 week ago close <= 2 weeks ago high and 1 week ago open <= 2 weeks ago high and 1 week ago close >= 2 weeks ago low and 1 week ago open >= 2 weeks ago low and latest close >= 50 and weekly close <= 1 week ago high and weekly open <= 1 week ago high and weekly close >= 1 week ago low and weekly open >= 1 week ago low and latest sma( latest volume , 20 ) * latest close >= 50000000 and weekly close <= 2 weeks ago high and weekly open <= 2 weeks ago high and weekly open <= 2 weeks ago high and weekly open >= 2 weeks ago low ) )'
VELOCITY_SETUPS ='( {cash} ( ( {cash} ( latest sma( latest volume , 20 ) * latest close >= 30000000 and latest "close - 1 candle ago close / 1 candle ago close * 100" <= 1 and latest "close - 1 candle ago close / 1 candle ago close * 100" >= -1 and latest sma( close,7 ) / latest sma( close,65 ) > 1.04 ) ) ) )'

clauses = {
    'IPO' : [IPOBASES],
    'MAGNITUDE' : [MAGNITUDE_SETUPS],
    'VELOCITY' : [VELOCITY_SETUPS]
    '15%+ Movers': [FIFTEEN_5DAYS],
    '10%- Movers': [TEN_DECLINE_5DAYS],
    '50%+ Movers': [FIFTY_40DAYS],
}
