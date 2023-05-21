#!/usr/bin/env python3

# Budget data

import csv, random

# Create a list of lists of budget data using list comprehension
rows =  [ 
          [ 'Count =>', '','Count Delta_Squared =>' ],
          [ 'Sum =>', '','Sum Delta_Squared =>' ],
          [ 'Mean =>', '', 'Standard Deviation=>' ],
          [  ],
          [ 'ID','Samples', 'Delta', 'Delta_Squared' ],
        ] + \
        [ [ i+1, x] for i, x in enumerate( random.sample(range(1,1001),1000)) ]


# Write out the list of lists in CSV format
with open('desc_stats.csv', 'w', newline='') as file:
  writer = csv.writer( file )
  writer.writerows( rows )



