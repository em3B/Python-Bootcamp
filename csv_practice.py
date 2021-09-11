#Activity Instructions: function takes and first and last name. 
#It updates users.csv such that that name is removed.
# Then returns count of how many users removed 

import csv
def delete_users(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = csv.reader(file) #read file first
        rows = list(csv_reader)
    count = 0
    with open("users.csv", "w") as file:
        csv_writer = csv.writer(file)
        for row in rows: 
            if row[0] == first_name and row[1] == last_name: 
                count += 1 #count number of deleted users
            else:
                csv_writer.writerow(row)
    return "Users deleted: {}.".format(count)