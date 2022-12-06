from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class StockPriceHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DATETIME(timezone=True))
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    opn = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Float)
    adjClose = db.Column(db.Float)

# class StockInfo(db.Model):
#     zip
#     sector
#     fullTimeEmployees
#     longBusinessSummary
#     city
#     phone
#     state
#     country
#     companyOfficers
#     website
#     maxAge
#     address1
#     industry
#     ebitdaMargins
#     profitMargins
#     grossMargins
#     operatingCashflow
#     revenueGrowth
#     operatingMargins
#     ebitda
#     targetLowPrice
#     recommendationKey
#     grossProfits
#     freeCashflow
#     targetMedianPrice
#     currentPrice
#     earningsGrowth
#     currentRatio
#     returnOnAssets
#     numberOfAnalystOpinions
#     targetMeanPrice
#     debtToEquity
#     returnOnEquity
#     targetHighPrice
#     totalCash
#     totalDebt
#     totalRevenue
#     totalCashPerShare
#     financialCurrency
#     revenuePerShare
#     quickRatio
#     recommendationMean
#     exchange
#     shortName
#     longName
#     exchangeTimezoneName
#     exchangeTimezoneShortName
#     isEsgPopulated
#     gmtOffSetMilliseconds
#     quoteType
#     symbol
#     messageBoardId
#     market
#     annualHoldingsTurnover
#     enterpriseToRevenue
#     beta3Year
#     enterpriseToEbitda
#     52WeekChange
#     morningStarRiskRating
#     forwardEps
#     revenueQuarterlyGrowth
#     sharesOutstanding
#     fundInceptionDate
#     annualReportExpenseRatio
#     totalAssets
#     bookValue
#     sharesShort
#     sharesPercentSharesOut
#     fundFamily
#     lastFiscalYearEnd
#     heldPercentInstitutions
#     netIncomeToCommon
#     trailingEps
#     lastDividendValue
#     SandP52WeekChange
#     priceToBook
#     heldPercentInsiders
#     nextFiscalYearEnd
#     yield
#     mostRecentQuarter
#     shortRatio
#     sharesShortPreviousMonthDate
#     floatShares
#     beta
#     enterpriseValue
#     priceHint
#     threeYearAverageReturn
#     lastSplitDate
#     lastSplitFactor
#     legalType
#     lastDividendDate
#     morningStarOverallRating
#     earningsQuarterlyGrowth
#     priceToSalesTrailing12Months
#     dateShortInterest
#     pegRatio
#     ytdReturn
#     forwardPE
#     lastCapGain
#     shortPercentOfFloat
#     sharesShortPriorMonth
#     impliedSharesOutstanding
#     category
#     fiveYearAverageReturn
#     previousClose
#     regularMarketOpen
#     twoHundredDayAverage
#     trailingAnnualDividendYield
#     payoutRatio
#     volume24Hr
#     regularMarketDayHigh
#     navPrice
#     averageDailyVolume10Day
#     regularMarketPreviousClose
#     fiftyDayAverage
#     trailingAnnualDividendRate
#     open
#     toCurrency
#     averageVolume10days
#     expireDate
#     algorithm
#     dividendRate
#     exDividendDate
#     circulatingSupply
#     startDate
#     regularMarketDayLow
#     currency
#     trailingPE
#     regularMarketVolume
#     lastMarket
#     maxSupply
#     openInterest
#     marketCap
#     volumeAllCurrencies
#     strikePrice
#     averageVolume
#     dayLow
#     ask
#     askSize
#     volume
#     fiftyTwoWeekHigh
#     fromCurrency
#     fiveYearAvgDividendYield
#     fiftyTwoWeekLow
#     bid
#     tradeable
#     dividendYield
#     bidSize
#     dayHigh
#     coinMarketCapLink
#     regularMarketPrice
#     preMarketPrice
#     logo_url
#     trailingPegRatio