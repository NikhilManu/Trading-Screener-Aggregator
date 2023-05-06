INSIDEBAR = '( {cash} ( latest close >= latest max( 250 , latest high ) * 0.75 and latest close >= latest min( 250 , latest low ) * 1.3 and latest sma( latest volume , 20 ) * latest close >= 30000000 and latest high < 1 day ago high and latest low > 1 day ago low and latest close >= latest sma( latest close , 50 ) ) )'
DOUBLEINSIDEBAR = '( {cash} ( latest close >= latest max( 250 , latest high ) * 0.75 and latest close >= latest min( 250 , latest low ) * 1.3 and latest sma( latest volume , 20 ) * latest close >= 30000000 and latest close >= latest sma( latest close , 50 ) and latest high < 2 days ago high and 1 day ago high < 2 days ago high and latest low > 2 days ago low and 1 day ago low > 2 days ago low ) )'
TIGHTCLOSETHREEDAY = '( {cash} ( ( {cash} ( latest sma( latest volume , 20 ) * latest close >= 30000000 and latest close >= latest max( 250 , latest high ) * 0.75 and latest close >= latest min( 250 , latest low ) * 1.3 and latest close >= latest sma( latest close , 50 ) and latest close <= 1 day ago close * 1.01 and latest close >= 1 day ago close * .99 and 1 day ago close <= 2 days ago close * 1.01 and 1 day ago close >= 2 days ago close * .99 and 2 days ago close <= 3 days ago close * 1.01 and 2 days ago close >= 3 days ago close * .99 ) ) ) )'

WEEKLYINSIDEBAR = '( {cash} ( weekly high < 1 week ago high and weekly low > 1 week ago low and latest sma( latest volume , 20 ) * latest close >= 30000000 and latest close >= latest sma( latest close , 100 ) and latest close >= latest max( 250 , latest high ) * 0.75 and latest close >= latest min( 250 , latest low ) * 1.3 ) ) '
TWOWEEKLYINSIDEBAR = '( {cash} ( latest close >= latest max( 250 , latest high ) * 0.75 and latest close >= latest min( 250 , latest low ) * 1.3 and latest sma( latest volume , 20 ) * latest close >= 30000000 and latest close >= latest sma( latest close , 100 ) and weekly high < 2 weeks ago high and 1 week ago high < 2 weeks ago high and weekly low > 2 weeks ago low and 1 week ago low > 2 weeks ago low ) )'

#Stocks that moved 30 percent in a month
ONEMONTHGAINERS = '( {cash} ( latest sma( latest volume , 20 ) * latest close >= 20000000 and latest max( 22 , latest close ) >= latest min( 22 , latest open ) * 1.30 and latest close >= latest sma( latest close , 20 ) ) )'

#Stocks that moved 80 percent in 8 week
POWERPLAYS = '( {cash} ( ( {cash} ( latest high >= weekly min( 8 , weekly low ) * 1.8 and latest high > 20 and latest high <= 25000 and latest sma( latest volume , 20 ) * latest close >= 30000000 ) ) ) )'

#Stocks 10% down in 4 Days
DOWN_10 = '( {cash} ( ( {cash} ( latest sma( latest volume , 20 ) * latest close >= 30000000 and latest close <= 4 days ago close * 0.90 ) ) ) )'

#Deep Dive Study screeners
TWENTY_5DAYS = '( {cash} ( latest sma( latest volume , 20 ) * latest close >= 30000000 and latest close >= 5 days ago close * 1.2 ) )'
FIFTY_40DAYS = '( {cash} ( latest sma( latest volume , 20 ) * latest close >= 30000000 and latest close >= 40 days ago close * 1.5 ) )'

clauses = {
    'DAILY INSIDEBAR': [ INSIDEBAR, DOUBLEINSIDEBAR, TIGHTCLOSETHREEDAY ],
    'WEEKLY INSIDEBARS': [WEEKLYINSIDEBAR, TWOWEEKLYINSIDEBAR],
    'REVERSALS' : [DOWN_10],
    '20% IN 5 DAYS' : [TWENTY_5DAYS],
    '50% IN 40 DAYS' : [FIFTY_40DAYS]
}