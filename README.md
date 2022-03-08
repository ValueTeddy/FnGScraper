Python repo for scraping the Fear and Greed indicator from the wayback machine using requests and beautifulsoup4

URLgetter.py gets an unformated list of URLS that needs to be manually fixed

URLListCleaner.py removes URLs of duplicate dates from the outputted list of URLS

fearandgreed.py contains the scraper


-------

Investors are driven by two emotions: fear and greed. Too much fear can sink stocks well below where they should be. When investors get greedy, they can bid up stock prices way too far.

So what emotion is driving the market now? CNNMoney's Fear & Greed index makes it clear.

We look at 7 indicators:

•Stock Price Momentum: The S&P 500 (SPX) versus its 125-day moving average

•Stock Price Strength: The number of stocks hitting 52-week highs and lows on the New York Stock Exchange

•Stock Price Breadth: The volume of shares trading in stocks on the rise versus those declining.

•Put and Call Options: The put/call ratio, which compares the trading volume of bullish call options relative to the trading volume of bearish put options

•Junk Bond Demand: The spread between yields on investment grade bonds and junk bonds

•Market Volatility: The VIX (VIX), which measures volatility

•Safe Haven Demand: The difference in returns for stocks versus Treasuries

For each indicator, we look at how far they've veered from their average relative to how far they normally veer. We look at each on a scale from 0 - 100. The higher the reading, the greedier investors are being, and 50 is neutral.

Then we put all the indicators together - equally weighted - for a final index reading
-------