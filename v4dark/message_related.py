'''
All functions in this file will be in relation to messages.

which isn't the only possible kind, I've noticed.

They all need to be in the on_message() function, or else they won't work.
'''
from bs4 import BeautifulSoup
import requests
from v4dark.helper_functions import logger

my_logger = logger(log_filepath='logs/message_related.log', logger_name='message_related') 

def get_stock_price_from_yahoo(stock_ticker):
    '''
    urls used to write this function:

    https://medium.com/analytics-vidhya/how-to-get-stock-prices-in-real-time-using-python-2021-bf50c1d2378b

    https://stackoverflow.com/questions/34301815/understand-the-find-function-in-beautiful-soup
    '''
    url = 'https://finance.yahoo.com/quote/' + stock_ticker
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    price = soup.find('fin-streamer', class_ = 'Fw(b) Fz(36px) Mb(-4px) D(ib)').text
    return price


async def vineet_is_awesome(message):
    if 'vineet' in message.content.lower():
        await message.channel.send('Vineet is awesome!')

async def get_stock_price(message):
    if  message.content.lower().startswith('give_ticker'):
        stock_ticker = message.content.lower().split(" ")[1]
        await message.channel.send('Current price for ' + str(stock_ticker) + ":" + get_stock_price_from_yahoo(stock_ticker))