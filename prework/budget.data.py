#!/usr/bin/env python3

# Budget data

import csv, uuid

# Create a list of lists of budget data using list comprehension
rows =  [ ['Project ID', 'Year', 'Month', 'Projected Budget', 'Actual Budget'] ] + \
        [
          [ "Proj-" + project_id,
            year,
            month,
            ( 9500 + i * 500 ),
            ( 9500 + i * 500 ) - 200,
          ]
            for i, project_id in enumerate([ str(uuid.uuid4()).split("-")[1] for x in range(4) ])
              for year in ['2020', '2021', '2022']
                for month in ['January', 'February', 'March',
                              'April', 'May', 'June',
                              'July', 'August', 'September',
                              'October', 'November', 'December']
        ]



# Write out the list of lists in CSV format
with open('budget_data.csv', 'w', newline='') as file:
    writer = csv.writer( file )
    writer.writerows( rows )


