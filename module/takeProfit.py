from binanceAPI.user import um_futures_client
from binance.lib.utils import config_logging
from binance.error import ClientError
import logging

# TAKE PROFIT
def takeProfit(symbol,positionSide,side,type,stopPrice): 
    try:
        response = um_futures_client.new_order(
            symbol = symbol,
            positionSide = positionSide,
            side = side,
            type = type,
            stopPrice = stopPrice,
            timeInForce = "GTC",
            closePosition = "true",
        )
        #logging.info(response)
    except ClientError as error:
        logging.error(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )