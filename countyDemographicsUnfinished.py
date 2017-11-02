import json, random

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))
    print(your_interesting_demographic_function(counties))
    

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first = counties[0]["County"]
    for c in counties:
        if c["County"] < first:
            first = c["County"]
            
    return first

def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    first = counties[0]["Age"]["Percent Under 18 Years"]
    nme = counties[0]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > first:
            first = c["Age"]["Percent Under 18 Years"]
            nme = c
        
    return nme["County"], nme["State"]
    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    first = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > first:
            first = c["Age"]["Percent Under 18 Years"]
            
    return first
    
def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    first = counties[0]["Age"]["Percent Under 18 Years"]
    nme = counties[0]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > first:
            first = c["Age"]["Percent Under 18 Years"]
            nme = c
        
    return nme["County"], nme["State"], first
    
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    state = counties[0]["State"]
    count = 1
    d = {}
    
    for value in counties:
        if state == value["State"]:
            count += 1
        else:
            d[state] = count
            state = value["State"]
            count = 1
    
    #Find the state in the dictionary with the most counties
    v = d["CA"]
    for key, value in d.items():
        if value > v:
            v = value
            nme = key
    
    #Return the state with the most counties
    return nme
    
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    num = random.randint(0, len(counties))
    state = counties[num]["State"] 
    county = counties[num]["County"]
    word = "Employment: Private Non-farm Establisment: "
    employ = counties[num]["Employment"]["Private Non-farm Establishments"]
    return state + ": " + county + ": " + word + str(employ)
    
if __name__ == '__main__':
    main()
