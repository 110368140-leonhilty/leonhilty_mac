seasons = ['Spring', 'Summer', 'Fall', 'Winter']



combined_dict = {index:season for index,season in enumerate(seasons,start=1)}

combined_list = [[index,season] for index,season in enumerate(seasons,start=1)]

print(combined_dict)

print(combined_list)