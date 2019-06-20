import shippo

'''
In this tutorial we have an order with a sender address,
recipient address and parcel information that we need to ship.
'''

# Replace <API-KEY> with your key
shippo.config.api_key = "shippo_test_727263a08f4bd4394a35ce93275d00b5eabdc601 "

# Tracking based on carrier and tracking number
tracking_number = 'SHIPPO_TRANSIT'
# For full list of carrier tokens see https://goshippo.com/docs/reference#carriers
carrier_token = 'shippo'
tracking = shippo.Track.get_status(carrier_token, tracking_number)
key = 'detail'
if key in tracking.keys():
    print("ERROR")
else:
    print(tracking)
# For more tutorals of address validation, tracking, returns, refunds, and other functionality, check out our
# complete documentation: https://goshippo.com/docs/