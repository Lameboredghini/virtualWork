import itertools

# define the categories and their respective time frames
categories = {
    'Restaurants': 1.5,
    'Bars': 2,
    'Clubs': 3,
    'Cafe': 2,
    'Cinemas': 3,
    'Parks': 1.5,
    'Museums': 1.5,
    'Galleries': 1,
    'Shopping Centres': 2,
    'Theatres': 2,
    'Amusement Parks': 3,
    'Swimming Pools': 2,
    'Sports Club': 1.5,
    'Beauty Salons': 2
}

# prompt the user for available time
total_time = round(float(input('How much time do you have (in hours)? ')) * 60)

# generate the list of arrays of places the user can visit
places_to_visit = []
max_places = 0
for n in range(len(categories)):
    for combination in itertools.combinations(categories.keys(), n + 1):
        time_frame = sum(categories[c] for c in combination)
        if total_time >= time_frame * 60 and len(combination) >= max_places:
            places_to_visit.append(list(combination))
            max_places = len(combination)
    if total_time < categories[list(categories.keys())[n]] * 60:
        break

# print the list of places where the user can visit the maximum number of places without any remaining time
if places_to_visit:
    print(f'You can visit the following places in {total_time // 60} hours and {total_time % 60} minutes:')
    for places in places_to_visit:
        if len(places) == max_places:
            print(places)
else:
    print('Sorry, you do not have enough time to visit any place.')
