# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def convert_float(costs):
    converted_damages = []
    conversion = {'M': 1000000, 'B': 1000000000}
    for cost in costs:
      if 'M' in cost:
          str_cost = cost.strip('M')
          new_cost = float(str_cost) * conversion.get('M')
          converted_damages.append(new_cost)
      elif 'B' in cost:
          str_cost = cost.strip('B')
          new_cost = float(str_cost) * conversion.get('B')
          converted_damages.append(new_cost)
      else:
          converted_damages.append(cost)
    return converted_damages

print(convert_float(damages))

# write your construct hurricane dictionary function here:

def hurricane_dictionary(Name, Month, Year, Max_Sustained_Wind, Areas_Affected, Damage, Death):
    hurricane_dict = {}
    for n in range(len(Name)):
        hurricane_dict[Name[n]] = {'Name': Name[n], 'Month': Month[n], 'Year': Year[n], 'Max Sustained Wind': Max_Sustained_Wind[n], 'Areas Affected': Areas_Affected[n], 'Damage': Damage[n], 'Deaths': Death[n]}
    return hurricane_dict

print(hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths))

# write your construct hurricane by year dictionary function here:
def hurricanes_year(hurricane_dict):
  hurricane_years = {}
  for key in hurricane_dict.keys():
    year = hurricane_dict[key]['Year']
    hurricane = hurricane_dict[key]
    if year not in hurricane_years:
        hurricane_years.update({year: hurricane_dict[key]})
    else:
        hurricane_years[year].update(hurricane_dict[key])
  return hurricane_years

print(hurricanes_year(hurricane_dict))

# write your count affected areas function here:
def damaged_areas(hurricane_dict):
  damaged_areas_dictionary = {}
  for key in hurricane_dict.keys():
    damaged_areas_list = hurricane_dict[key]['Areas Affected']
    for area in damaged_areas_list:
      if area not in damaged_areas_dictionary:
        damaged_areas_dictionary.update({area: 1})
      else:
        damaged_areas_dictionary[area] += 1
  return damaged_areas_dictionary

print(damaged_areas(hurricane_dict))

# write your find most affected area function here:

def most_affected(damaged_areas_dict):
  max_area = ''
  max_area_count = 0
  for area in damaged_areas_dict:
    count_area = damaged_areas_dict[area]
    if count_area > max_area_count:
      max_area = area
      max_area_count = count_area
    else:
      max_area_count += 0
  return max_area, max_area_count

most_affected_area = most_affected(damaged_areas_dict)
print(most_affected_area)

# write your greatest number of deaths function here:
def most_deadly(hurricane_dict):
  most_deadly_name = ''
  most_death_count = 0
  for hurricane in hurricane_dict:
    total_deaths = hurricane_dict[hurricane]['Deaths']
    if total_deaths > most_death_count:
      most_deadly_name = hurricane
      most_death_count = total_deaths
    else:
      most_death_count += 0
  return most_deadly_name, most_death_count

deadlist_hurricane = most_deadly(hurricane_dict)
print(deadlist_hurricane)

# write your catgeorize by mortality function here:
def mortality_rating(hurricane_dict):
  hurricanes_mort_ratings = {'0':0, '1':0, '2':0, '3':0, '4':0}
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  for hurricane in hurricane_dict:
    total_deaths = hurricane_dict[hurricane]['Deaths']  
    if total_deaths == 0:
      hurricanes_mort_ratings['0'] += 1
    elif total_deaths <= 100:
      hurricanes_mort_ratings['1'] += 1
    elif total_deaths <= 500:
      hurricanes_mort_ratings['2'] += 1
    elif total_deaths <= 1000:
      hurricanes_mort_ratings['3'] += 1
    else:
      hurricanes_mort_ratings['4'] += 1
  return hurricanes_mort_ratings

hurricane_mortality = mortality_rating(hurricane_dict)
print(hurricane_mortality)

def h_mortality_rating(hurricane_dict):
  hurricanes_mort_ratings = {0: [], 1: [], 2: [], 3: [], 4: []}
  for key in hurricane_dict:
    deaths = hurricane_dict[key]['Deaths']
    if deaths == 0:
      hurricanes_mort_ratings[0].append(hurricane_dict[key])
    elif deaths <= 100:
      hurricanes_mort_ratings[1].append(hurricane_dict[key])
    elif deaths <= 500:
      hurricanes_mort_ratings[2].append(hurricane_dict[key])
    elif deaths <= 1000:
      hurricanes_mort_ratings[3].append(hurricane_dict[key])
    else:
      hurricanes_mort_ratings[4].append(hurricane_dict[key])

  return hurricanes_mort_ratings

h_hurricane_mortality = h_mortality_rating(hurricane_dict)
print(h_hurricane_mortality)

# write your greatest damage function here:
def most_damaging(hurricane_dict):
  most_damaging_name = ''
  most_damage_dollars = 0
  for hurricane in hurricane_dict:
    total_damage = hurricane_dict[hurricane]['Damage']
    if total_damage == 'Damages not recorded':
      most_damage_dollars += 0
    elif total_damage > most_damage_dollars:
      most_damaging_name = hurricane
      most_damage_dollars = total_damage
    else:
      most_damage_dollars += 0
  return most_damaging_name, most_damage_dollars

damagingest_hurricane = most_damaging(hurricane_dict)
print(damagingest_hurricane)

# write your catgeorize by damage function here:
def damage_ratings(hurricane_dict):
  hurricanes_damage_ratings = {0: [], 1: [], 2: [], 3: [], 4: [], 'Unknown': []}
  for key in hurricane_dict:
    damage = hurricane_dict[key]['Damage']
    if damage == 'Damages not recorded':
      hurricanes_damage_ratings['Unknown'].append(hurricane_dict[key]) 
    elif damage == 0:
      hurricanes_damage_ratings[0].append(hurricane_dict[key])
    elif damage <= 100000000:
      hurricanes_damage_ratings[1].append(hurricane_dict[key])
    elif damage <= 1000000000:
      hurricanes_damage_ratings[2].append(hurricane_dict[key])
    elif damage <= 10000000000:
      hurricanes_damage_ratings[3].append(hurricane_dict[key])
    else: 
      hurricanes_damage_ratings[4].append(hurricane_dict[key])
  return hurricanes_damage_ratings

hurricanes_ratings_damage = damage_ratings(hurricane_dict)
print(hurricanes_ratings_damage)
