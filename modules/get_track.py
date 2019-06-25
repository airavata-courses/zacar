#!/usr/bin/python
import shippo

def config():
    shippo.api_key = "shippo_live_721cc5b0872819518eeeecbfd2dc742e274105b4"
    shippo.api_version = "2017-03-29"
    shippo.verify_ssl_certs = True
    shippo.rates_req_timeout = 30.0

def get_tracking_info(tracking_number):
    carriers_supported = ['fedex', 'ups', 'usps']
    valid_tracking = False
    info = []
    for carrier in carriers_supported:
        if valid_tracking:
            break
        else:
            tracking = shippo.Track.get_status(carrier, tracking_number)
            if tracking['address_to'] != None:
                info.append('------------------------------------------------------')
                status = tracking['tracking_status']
                location = status['location']
                info.append(status['status'])
                info.append(status['status_date'])
                info.append(status['status_details'])
                info.append(location['city'])
                info.append(location['state'])
                info.append(location['zip'])
                info.append('------------------------------------------------------')
                return(info)
            else:
                pass
    return None