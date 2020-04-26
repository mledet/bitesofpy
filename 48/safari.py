import os
import re
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)

def get_date(line):
    
    date = line[0:5]

    return date


def create_chart():

    previous_date = None

    with open(SAFARI_LOGS,"r") as f:
        lines = f.read().splitlines()

        for line in lines:

            if "sending to slack channel" in line:

                date = get_date(line)

                if date != previous_date:
                    if previous_date:
                        print("")
                    print(f"{date} ", end="")    

                if "python" in previous_line.lower():
                    print("🐍", end="")
                else:
                    print(".", end="")

                previous_date = date
            previous_line = line
                        

                

    