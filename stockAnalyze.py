import yfinance as yf

def extractBasicInfo(data):
    keysToExtract = ['longName', 'website', 'sector', 'fullTimeEmployees', 'marketCap', 'totalRevenue', 'trailingEps']
    basicInfo = {}
    for key in keysToExtract:
        if key in data:
            basicInfo[key] = data[key]
        else:
            basicInfo[key] = ''
    return basicInfo

def getCompanyStockInfo(tickerSymbol):
    company = yf.Ticker(tickerSymbol)
    basicInfo = extractBasicInfo(company.info)
    print(basicInfo)
    company.info
    company.calendar
    company.analyst_price_targets
    company.quarterly_income_stmt
    company.history(period='1mo')
    company.option_chain(company.options[0]).calls

getCompanyStockInfo("MSFT")


