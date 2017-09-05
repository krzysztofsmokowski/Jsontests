import json
from pprint import pprint
import re

with open('changes_with_files.json') as data_file:
    data = json.load(data_file)

filename_array = []
for dat in data[0]["revisions"]:
    for more_dat in data[0]["revisions"][dat]:
        print(more_dat)
        if "files" in more_dat:
            for nevermore in data[0]["revisions"][dat][more_dat]:
                if "change" in nevermore:
                    filename_array.append(nevermore)

for dat in filename_array:
    datek = dat.split('/')
    datek = datek[-1]
    if "Change" in datek:
        print(dat)
