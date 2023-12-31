import pandas as pd
"""
upload csv file with list of hospitals and cities in florida
"""
hosp = pd.read_csv('hosp_nm.csv')
print(hosp)

"""
hospital is a function that reads the csv file, hosp_nm and looks for a match in the city column. If a match is found, it will output the corresponding hospital in a list called indlist. The list of hospitals in the city is returned at the end of the code
"""
def hospital(df,name: str):
    indlist = []
    for b in range(len(df)):
        if str(df['City'][b]) == name:
            indlist.append(df['Hospital Name'][b])
    if indlist == []:
      return []
    return indlist
"""
The following code is meant to output a map of the cities located in the csv file of hospital and show the average gross patient revenue for the city by a gradient.
"""
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim


def map(df,location):
  data = hospital(df,location)
  new df =
  df = px.data.gapminder().query()
  fig = px.scatter_geo(df, locations="iso_alpha",
                     size="pop", # size of markers, "pop" is one of the columns of gapminder
                     )
  fig.show()

"""
The missing code is meant to create a histogram of the average number of hospital beds for the hospitals in the city
"""


  #this portion of the code takes in user input, asking questions to determine the state of the users condition and responding with an output that includes the nearest hospitals based on the city they inputted using the hospital function defined previously.
name=input("What is your name?")
location=input("What city do you live in? (First letter of city should be capitalized)")
while hospital(hosp,location) == []:
  print('Sorry, there are no hospitals in that city. Try another city.')
  location = input('What city do you live in? (First letter of city should be capitalized)')
answer=input("have you taken a tuberculosis test? (answer should be 'yes' or 'no')")
if answer=="yes":
  answer2=input("was your test positive? (answer should be 'yes' or 'no')")
  if answer2=="yes":
    answer3=input("Have you been feeling fatigued or experiencing weight loss, fever, night sweats, or coughing up blood? (answer should be 'yes' or 'no')")
    if answer3=="yes":
      print("you have active tuberculosis. In order to treat this, you should take isoniazid INH in combination with three other drugs-rifampin, pyrazinamide and ethambutol.")
      print('This is/These are the hospitals where you can get treatment in your city:', hospital(hosp,location))
    else:
      print("you have Latent tuberculosis. In order to treat this, you should take Isoniazid and rifapentine. You can find this at ")
      print('This is/These are the hospitals where you can get treatment in your city:', hospital(hosp,location))
  else:
    answer4=input("have you taken the vaccine? (answer should be 'yes' or 'no')")
    if answer4=="yes":
      answer5=input("what year did you get the vaccine?")
      print(int(answer5)+15, "is the year that you need to be revaccinated")
      print('You can get vaccinated at these hospitals in your city:',hospital(hosp,location))
    else:
      print('You can get vaccinated at these hospitals in your city:',hospital(hosp,location))
else:
  print('you can get tested at these locations:', hospital(hosp,location))
