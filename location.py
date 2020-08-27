import requests
import json

filelocation="C:\Users\\venuved\OneDrive - Microsoft\Desktop\locationhistory-new-small.csv"
apikey="vxcvzxcvzxcv"
file=open(filelocation, "r")
for line in file:
    a=line.split(",")
    latitude=a[1]
    longitude=a[2]

   # stringd="The lattitude of " + latitude + " and longitude of " + longitude   version 1:2
    httpurl="https://atlas.microsoft.com/search/address/reverse/json?api-version=1.0&subscription-key="+apikey+"&language=en-US&query="+latitude+","+longitude+"&number=1"
    response = requests.get(httpurl)
    #jsonobject = {"summary":{"queryTime":135,"numResults":1},"addresses":[{"address":{"buildingNumber":"1505","streetNumber":"1505","routeNumbers":[],"street":"Edgar Martinez Drive South","streetName":"Edgar Martinez Drive South","streetNameAndNumber":"1505 Edgar Martinez Drive South","countryCode":"US","countrySubdivision":"WA","countrySecondarySubdivision":"King","municipality":"Seattle","postalCode":"98134","municipalitySubdivision":"Downtown Seattle","country":"United States","countryCodeISO3":"USA","freeformAddress":"1505 Edgar Martinez Drive South, Seattle, WA 98134","boundingBox":{"northEast":"47.590293,-122.332326","southWest":"47.590286,-122.333248","entity":"position"},"countrySubdivisionName":"Washington","localName":"Seattle"},"position":"47.590290,-122.332726"}]}
    jsonobject = response.json()
    freedom = jsonobject['addresses'][0]['address']['country']
    print("On "+a[0]+ ", I was in " + freedom)

file.close

#https://atlas.microsoft.com/search/address/reverse/json?api-version=1.0&subscription-key=dfasdffsadfa0&language=en-US&query=47.591180,-122.332700&number=1
