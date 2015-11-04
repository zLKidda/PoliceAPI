def readJsonUrl(url):
    """This reads the contents of a URL.  Works for json data and Python 3"""
    #####################################################################
    # In this block of code:
    # - Python opens the url
    # - reads the data
    # - stores it as a string
    # - closes the url
    import urllib.request
    try:
        page = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print("There was an error opening the URL (description below).")
        print(e)
        print("Ask for help?")
        return(None)
    data_bytes = page.read()
    data_str = data_bytes.decode('utf-8')
    page.close()
    #####################################################################
    # In this block of code
    # - The json string is converted to a Python dictionary.
    # - This is returned
    import json
    try:
        output = json.loads(data_str)
    except:
        print("Error")
        return(None)
    return(output)
    #####################################################################


def main():
    postcode = input("Please enter the postcode\n")
    if postcode == "":
        postcode = "PR56XQ"
    URL = "http://api.postcodes.io/postcodes/"
    URL = URL + postcode
    jdata = readJsonUrl(URL)
    long = jdata["result"]["longitude"]
    lat = jdata["result"]["latitude"]
    print("longitude:",long)
    print("latitude:",lat)
    URL2 = "https://data.police.uk/api/crimes-at-location?date=2012-02&lat="+ str(lat) + "&lng=" + str(long)
    #       https://data.police.uk/api/stops-at-location?location_id=885142&date=2015-06
    print(URL2)
    print("CRIMES AT LOCATION")
    jdata2 = readJsonUrl(URL2)
    print(jdata2)
    print("STOPS AT LOCATION")
    URL3 = "https://data.police.uk/api/stops-street?lat=" + str(lat) + "&lng=" + str(long) + "&date=2015-01"
    #       https://data.police.uk/api/stops-street?lat=52.629729&lng=-1.131592&date=2015-05
    jdata3 = readJsonUrl(URL3)
    print(URL3)
    print(jdata3)
    URL4 =  "https://data.police.uk/api/stops-street?lat=" + str(lat) + "&lng=" + str(long)
    print("STOPS AND STREET")
    print(URL4)
    jdata4 = readJsonUrl(URL4)
    print(jdata4)
    #       https://data.police.uk/api/stops-street?lat=53.7264510190582&lng=-2.64514267543159





if __name__ == "__main__":
    main()
