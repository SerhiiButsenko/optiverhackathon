import random
from optibook.synchronous_client import Exchange

# Step 1: Connect to the exchange
e = Exchange()
e.connect()

# Step 2: Choose an instrument
instrument_id = list(e.get_tradable_instruments().keys())[0]
print(f"Using instrument: {instrument_id}")

# Step 3: Insert 10 sell orders with high prices (> 100,000)
order_ids = []
for i in range(10):
    high_price = random.uniform(100000, 101000)
    response = e.insert_order(
        instrument_id=instrument_id,
        price=high_price,
        volume=10,
        side='ask',
        order_type='limit'
    )
    order_ids.append(response.order_id)
    print(f"Inserted order {i+1}: ID={response.order_id}, Price={high_price:.2f}")

# Step 4: Check outstanding orders
outstanding = e.get_outstanding_orders(instrument_id)
print("\nOutstanding Orders:")
for oid, status in outstanding.items():
    print(f"Order ID {oid}: Price={status.price}, Volume={status.volume}")

# Step 5: Amend each order to only 5 lots
print("\nAmending all outstanding orders to 5 lots...")
for oid in order_ids:
    amend_response = e.amend_order(instrument_id, order_id=oid, volume=5)
    print(f"Amended Order ID {oid}: Success={amend_response.success}")

# Check again
outstanding = e.get_outstanding_orders(instrument_id)
print("\nOutstanding Orders After Amendment:")
for oid, status in outstanding.items():
    print(f"Order ID {oid}: Price={status.price}, Volume={status.volume}")

# Step 6: Cancel all outstanding orders
print("\nCancelling all outstanding orders...")
e.delete_orders(instrument_id)

# Final check
outstanding = e.get_outstanding_orders(instrument_id)
print("\nOutstanding Orders After Deletion:")
if not outstanding:
    print("✅ All orders successfully cancelled.")
else:
    for oid, status in outstanding.items():
        print(f"❌ Still active: Order ID {oid}: Price={status.price}, Volume={status.volume}")
