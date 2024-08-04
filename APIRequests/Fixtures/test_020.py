
import csv
import pandas
import pandas as pd

# pip install pandas
class Test_CRUD(object):
    def test_update_1(self):
        # Read the file
        with open(r'C:\Users\joshna\PycharmProjects\pylearning\APIRequests\Fixtures\userdata.csv.csv') as csvfile:
            reader= csv.reader(csvfile)
            for row in reader:
                print(row)

