INSIDEBAR = '( {cash} ( latest close >= latest max( 250 , latest high ) * 0.75 and latest sma( latest volume , 20 ) * latest close >= 20000000 and latest high < 1 day ago high and latest low > 1 day ago low and latest volume < latest sma( latest volume , 20 ) and latest close >= latest sma( latest close , 50 ) ) )'
DOUBLEINSIDEBAR = '( {cash} ( latest close >= latest max( 250 , latest high ) * 0.75 and latest sma( latest volume , 20 ) * latest close >= 20000000 and latest close >= latest sma( latest close , 50 ) and latest high < 2 days ago high and 1 day ago high < 2 days ago high and latest low > 2 days ago low and 1 day ago low > 2 days ago low ) )'
TIGHTCLOSETHREEDAYS = '( {cash} ( ( {cash} ( latest sma( latest volume , 20 ) * latest close >= 20000000 and latest close >= latest max( 250 , latest high ) * 0.75 and latest close >= latest sma( latest close , 50 ) and latest close <= 1 day ago close * 1.01 and latest close >= 1 day ago close * .99 and 1 day ago close <= 2 days ago close * 1.01 and 1 day ago close >= 2 days ago close * .99 and 2 days ago close <= 3 days ago close * 1.01 and 2 days ago close >= 3 days ago close * .99 ) ) ) )'
ONEMONTHGAINERS = '( {cash} ( latest sma( latest volume , 20 ) * latest close >= 20000000 and latest max( 22 , latest close ) >= latest min( 22 , latest open ) * 1.30 and latest close >= latest sma( latest close , 50 ) ) )'

clauses = {
    'IB_Output': [ INSIDEBAR, DOUBLEINSIDEBAR, TIGHTCLOSETHREEDAYS ],
    'Monthly_Gainers': [ ONEMONTHGAINERS ]
}