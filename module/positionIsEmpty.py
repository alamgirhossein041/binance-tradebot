from binanceAPI.user import um_futures_client
from binance.lib.utils import config_logging
from binance.error import ClientError
import logging

# CHECK IF POSITION IS EMPTY
def positionIsEmpty():
    try:
        response = um_futures_client.get_position_risk(symbol = "ETHUSDT")
        trigger1 = float(response[0]["positionAmt"])
        trigger2 = float(response[1]["positionAmt"])
        
        if trigger1 == 0 and trigger2 == 0:
            return True
        else:
            return False         
    except ClientError as error:
        logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
