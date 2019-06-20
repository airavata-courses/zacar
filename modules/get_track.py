#!/usr/bin/python
import shippo

def config():
    shippo.config.api_key = "shippo_live_721cc5b0872819518eeeecbfd2dc742e274105b4"
    shippo.config.api_version = "2017-03-29"
    shippo.config.verify_ssl_certs = True
    shippo.config.rates_req_timeout = 30.0

def get_tracking_info(tracking_number):
    carriers_supported = ['fedex', 'ups', 'usps']
    valid_tracking = False
    for carrier in carriers_supported:
        tracking = shippo.Track.get_status(carrier, tracking_number)
        if tracking['transaction'] == None:
            pass
        else:
            print(tracking)
            valid_tracking = True
            break
    if valid_tracking:
        pass
    else:
        print("Invalid Tracking Number")