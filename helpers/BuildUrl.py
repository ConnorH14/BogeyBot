def buildUrl(reservation):

    reservation.date = reservation.date.replace("/", "%2F")
    reservation.time = reservation.time.replace(":", "%3A").replace(" ", "+")

    url_prefix = (
        "https://web2.myvscloud.com/wbwsc/idboisewt.wsc/search.html?Action=Start&SubAction=&"
    )
    url_body = (
        f"secondarycode={reservation.course}"
        + f"&begindate={reservation.date}"
        + f"&numberofplayers={reservation.player_count}"
        + f"&begintime={reservation.time}"
        + f"&numberofholes={reservation.holes}"
    )
    url_suffix = "&display=detail&module=gr&multiselectlist_value=&grwebsearch_buttonsearch=yes"

    url = url_prefix + url_body + url_suffix

    return url
