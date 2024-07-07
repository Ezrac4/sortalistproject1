
# start, 7-7-2024 v.1

import csv

class CSVfunctions:
    def __init__(self, file):
        if file.endswith('.csv'):
            with open(file) as csv_file:
                first_line = csv_file.readline().strip()
                if first_line == 'Name,Start Date,End Date':
                    self.file = file
                else: 
                    return 'Invalid CSV file'
        else:
            return 'Invalid file type'

    def csv_to_list(self):
        main_list = []
        with open(self.file) as csv_file:
            main_dict = csv.DictReader(csv_file)
            for i in main_dict:
                name = i['Name']
                start_date = i['Start Date']
                end_date = i['End Date']
                main_list.append([name, {'Start Date': start_date, 'End Date': end_date}])
        return main_list
    
    def sort_list(self, start_or_end, late_or_early):
        if start_or_end == 'by start date':
            main_list_sorted = sorted(self.csv_to_list(), key=lambda x: x[1]['Start Date'], reverse=True if late_or_early == 'by most recent first' else False)
        elif start_or_end == 'by end date':
            main_list_sorted = sorted(self.csv_to_list(), key=lambda x: x[1]['End Date'], reverse=True if late_or_early == 'by most recent first' else False)
        return main_list_sorted
    
    def sorted_list_to_csv(sorted_list, file_name):
        with open(file_name, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Name', 'Start Date', 'End Date'])
            for i in sorted_list:
                csv_writer.writerow([i[0], i[1]['Start Date'], i[1]['End Date']])
        return file_name

list_of_hackathons = CSVfunctions('datalisthackathons.csv')
# print(CSVfunctions.sort_list_by_latest(list_of_hackathons))


# the following creates a new csv file based on data from the original csv 'datalisthackathons.csv', 
#   and sorts it by start or end date ('by start date' or 'by end date'), 
#       and by latest or earliest instance of a hackathon ('by most recent first' or 'by oldest first').
#
# I.E.: 'by start date', 'by most recent first' would sort the csv by the most recently started hackathons
# it will also print the name of the new csv file created
print(CSVfunctions.sorted_list_to_csv(CSVfunctions.sort_list(CSVfunctions('datalisthackathons.csv'), 'by start date', 'by most recent first'), 'HackathonsSorted1.csv'))
# print(constant__.constant__________(constant____.constant (constant____('ORIGINAL_CSV_FILE.csv'),  'by strt/nd d8', 'by mrcnt/oldst first'), 'NEW_CSV_FILE.csv'_____)) 

# end, 7-7-2024 v.1
