import sys
 
def most_occurance_country(countryMax):
    dMax = max(countryMax,key=countryMax.get)
    print(dMax,countryMax[dMax])

def Main():
    for line in sys.stdin:
        line = line.strip()
        prefix , keyvalue = line.split("##")
        key, value = keyvalue.split("\t",1)
        if prefix == 'most_occurance_country':
            countryMax[key] = value
    if prefix == 'most_occurance_country':
        most_occurance_country(countryMax)

            print("{0}\t{1}".format(key,value))

Main()


