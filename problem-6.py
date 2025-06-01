def print_order_book(price_book):
    bids = price_book.bids
    asks = price_book.asks

    # Combine bid and ask prices into one list of all price levels
    all_prices = set([b.price for b in bids] + [a.price for a in asks])
    all_prices = sorted(all_prices, reverse=True)  # Descending order

    print("bid | price | ask")
    for price in all_prices:
        bid_vol = next((b.volume for b in bids if b.price == price), "")
        ask_vol = next((a.volume for a in asks if a.price == price), "")
        print(f"{bid_vol:>3} | {price:>5} | {ask_vol}")
