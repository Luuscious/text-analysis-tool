import yfinance as yf
import requests
import analyze
import json
from datetime import datetime
from bs4 import BeautifulSoup


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

def extractNewsArticleTextFromHtml(soup):
    allText = ""
    result = soup.find_all("div", {"class":"body yf-v6n2s3"})
    for res in result:
        allText += res.text
    return allText

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 16; Pixel 10) AppleWebKit/537.36 (KHTML, like Gecko) Edg/155.0.0.0 Mobile Safari/537.36'
}

def extractCompanyNewsArticles(newsArticles):
    allArticlesText = ""
    for newsArticle in newsArticles:
        url = newsArticle['link']
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        if not soup.findAll(string="Continue reading"):
            allArticlesText += extractNewsArticleTextFromHtml(soup)
    return allArticlesText

def getCompanyStockInfo(tickerSymbol):
    #Get data from yfinance API
    company = yf.Ticker(tickerSymbol)

    #Get basic info on company
    basicInfo = extractBasicInfo(company.info)
    priceHistory = getPriceHistory(company)
    futureEarningsDates = getEarningsDates(company)
    newsArticles = getCompanyNews(company)
    newsArticlesAllText = extractCompanyNewsArticles(newsArticles)
    newsTextAnalysis = analyze.analyzeText(newsArticlesAllText)


    finalStockAnalysis = {
        "basicInfo": basicInfo,
        "priceHistory": priceHistory,
        "futureEarningsDates": futureEarningsDates,
        "newsArticles": newsArticles,
        "newsTextAnalysis": newsTextAnalysis
    }

    return finalStockAnalysis
    # finalResultJson = json.dumps(newsTextAnalysis, indent=4)
    # print(finalResultJson)

# companyStockAnalysis = getCompanyStockInfo("MSFT")
# print(json.dumps(companyStockAnalysis, indent=4))



