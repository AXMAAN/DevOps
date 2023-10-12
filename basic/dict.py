def get_status(is_busy):
    # create a dictionary with one key "status" and one value depending on is_busy
    status_dict = {"status": "busy" if is_busy else "available"}
    # return the dictionary to the caller
    return status_dict