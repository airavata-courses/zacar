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
    tracking = []
    for carrier in carriers_supported:
        if valid_tracking:
            break
        else:
            tracking.append(shippo.Track.get_status(carrier, tracking_number))
            if tracking['transaction'] == None:
                pass
            else:
                valid_tracking = True
    return(tracking)