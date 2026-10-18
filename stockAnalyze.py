import yfinance as yf
from datetime import datetime

def extractBasicInfo(data):
    keysToExtract = ['longName', 'website', 'sector', 'fullTimeEmployees', 'marketCap', 'totalRevenue', 'trailingEps']
    basicInfo = {}
    for key in keysToExtract:
        if key in data:
            basicInfo[key] = data[key]
        else:
            basicInfo[key] = ''
    return basicInfo

def getPriceHistory(company):
    historyDF = company.history(period='12mo')
    prices = historyDF['Open'].tolist()
    dates = historyDF.index.strftime("%Y-%m-%d").tolist()
    return{
        'price': prices,
        'date': dates
    }

def getEarningsDates(company):
    earningsDatesDf = company.earnings_dates
    allDates = earningsDatesDf.index.strftime("%Y-%m-%d").tolist()
    dateObjects = [datetime.strptime(date, "%Y-%m-%d") for date in allDates]
    currentDate = datetime.now()
    futureDates = [date.strftime("%Y-%m-%d") for date in dateObjects if date > currentDate]
    return futureDates

def getCompanyNews(company):
    search = yf.Search("MSFT", news_count=15)
    newsList = search.news
    allNewsArticles = []
    for newsDict in newsList:
        newsDictToAdd = {
            'title': newsDict['title'],
            'link': newsDict['link']
        }
        allNewsArticles.append(newsDictToAdd)
    return allNewsArticles

def getCompanyStockInfo(tickerSymbol):
    #Get data from yfinance API
    company = yf.Ticker(tickerSymbol)

    #Get basic info on company
    basicInfo = extractBasicInfo(company.info)
    priceHistory = getPriceHistory(company)
    futureEarningsDates = getEarningsDates(company)
    newsArticles = getCompanyNews(company)

getCompanyStockInfo("MSFT")


