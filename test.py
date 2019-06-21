import modules.get_track as gt

gt.config()
result = gt.get_tracking_info('9505506699919169169801')
for info in result:
    print(info)