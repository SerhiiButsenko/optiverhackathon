def calculate_pnl(exchange, instrument_id):
    # Get positions and cash
    pos_cash = exchange.get_positions_and_cash()
    position_data = pos_cash.get(instrument_id, {"volume": 0, "cash": 0})
    position = position_data["volume"]
    cash = position_data["cash"]

    # Get last traded price (public market trade tick)
    trade_ticks = exchange.get_trade_tick_history(instrument_id)
    if not trade_ticks:
        print("No trades yet for this instrument, can't calculate PnL.")
        return None

    last_price = trade_ticks[-1].price

    # PnL formula: cash + (position * valuation)
    pnl = cash + (position * last_price)
    return pnl
