import pandas as pd

all_trades = []

def log_trades_in_loop(exchange, instruments):
    """This funciton logs all the trades that occur in a loop of the
    trading algorithm in a list. Combine this list with an aggregate list
    containing all the trades that occur in a session

    Returns:
        list: list of lists where each list represents a trade.
        [order_id, instrument_id, price, volume, side]
    """
    trades_in_loop = []
    # loop over all the instruments to check for new trades in each loop
    for instrument in instruments: #substitute "instruments" with the appropriate variable
        # getting the new trades within the loop for each instrument
        latest_trades_for_instrument = exchange.poll_new_trades(instrument) # we assume that e is the variable that we assigned as the exchange
        # looping over the new trades, if any, for a particular instrument inn algo loop
        for trade in latest_trades_for_instrument:
            # store the data of the trade in a list to append to our cummulative list of lists
            trade_instance = [trade.order_id, trade.instrument_id, trade.price, trade.volume, trade.side]
            # append the trade instance to the log of all the trades out of the loop.
            trades_in_loop.append(trade_instance)
    # add print function if you want
    print(trades_in_loop)
    return trades_in_loop
            

