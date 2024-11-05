This is small project I have built analyse data from stock market. In this project, we will build a web application that use API data from EODHD api to analye stock price and other relevant data structures. 

# This is a non-algorithmic way to analyse stock market data.
- programming language : Python
- API - EODHD API
- libraries : api.financial_data, config, 
- packages in python - flask


# EODHD API - 
EODHD API is a financial data provider that offers APIs to access financial data, including historical and real-time prices, fundamental data, and more.
visit: https://eodhd.com/
Using the api will allow the user of this application to explore data via the browser url.

# prerequisites -
1. buy an API from EODHD website - (there is a free api version)
2. python installed inthe computer
3. IDE 
4. libraries including flask

# program strcture:

|---README.md
|---stock_market.py
|---configure.py
|-API
  |- _init_.py
  |- financial.py
|---exchange.html

# configure.py
this python script contains the api token for the API service we are using.

# stock_market.py
this is the main scirpt in our program. this execute the foundational structure and connect with flask and api and html template to communicate among them inside the program. 
“http://127.0.0.1:5000/”, will request a list of exchanges from “data_fetcher“. The result from this function will be delivered as a JSON response.

Then the JSON response will be forwarded to HTML template.

# exchanges.html
This is the html template for the program to excute in a URL in a your default browser. 
Its primary function is to illustrate how to import the “exchanges” variable array and iterate through it. Each iteration returns a row as “exchange”, with “Code” being a row attribute.

# financial_data.py
This python file includes the class EODHDAPIsDataFetcher.