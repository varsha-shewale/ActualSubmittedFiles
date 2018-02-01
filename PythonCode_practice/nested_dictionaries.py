"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

def add_city(input,locations):
    inp = input.split(',')
    continent = inp[2].strip()
    country = inp[1].strip()
    city = inp[0].strip()
    #check if continent exists in dictionary
    if continent in locations:
        country_dict = locations[continent]

        #check if country exists in dictionary
        if country in country_dict:
            city_list = country_dict[country]

            #check if city exists in list
            if city in city_list:
                print '%s is already present in city list' %city
            else:
                city_list.append(city)
                locations[continent] = {country:city_list}

        else:
            #update country dictionary to add new country and city for existing continent
            country_dict.update({country:[city]})
    else:
        #add new continent, and thus new country and city in the locations dictionary
        locations[continent] = {country : [city]}

    return locations


loc = {'North America': {'USA': ['Mountain View']}}

loc = add_city('Bangalore, India, Asia', loc)
loc = add_city('Atlanta ,USA, North America', loc)
loc = add_city('Cairo ,Egypt, Africa', loc)





for k,v in loc.iteritems():
    print k,v