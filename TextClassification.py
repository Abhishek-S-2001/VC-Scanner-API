import re
from jobextraction import extract_job_title


class TextClassification:
    file = open("recognized.txt", "r")
    job = extract_job_title()
    emails = []
    web = []
    mobile_number = []
    alpha_character = []
    address = ''
    extra_words = ['Tel', 'Mob', 'Email', 'Website', 'Telephone', 'Mobile']
    pincode = []
    idx = -1

    for line in file:
        line = line.strip()
        emails = re.findall('[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', line)
        web = re.findall(r'\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(\))+)', line)
        mobile_number = re.findall(r'[+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', line)
        alpha_character = re.findall('[^A-Za-z0-9,-]+', line)

    fin = open("recognized.txt", "rt")
    # read file contents to string
    data = fin.read()

    # replace all occurrences of the required string

    for i in job:
        data = data.replace(i.capitalize(), "")
    for i in job:
        data = data.replace(i, "")
    for i in emails:
        data = data.replace(i, "")
    for i in web:
        data = data.replace(i, "")
    for i in mobile_number:
        data = data.replace(i, "")
    for i in alpha_character:
        data = data.replace(i, " ")
    for i in extra_words:
        data = data.replace(i, "")

    # close the input file
    fin.close()
    # open the input file in write mode
    fin = open("recognized.txt", "wt")
    # overwrite the input file with the resulting data
    fin.write(data)
    # close the file
    fin.close()

    file = open("recognized.txt", "r")

    for line in file:
        line = line.strip()
        idx = line.find(',')
        if idx > -1:
            address = line[idx:]
            data = line[:idx]
            break

    # print(idx)
    print(address)
    print(data)

    # close the input file
    file.close()
    # open the input file in write mode
    fin = open("recognized.txt", "wt")
    # overwrite the input file with the resulting data
    fin.write(data)
    # close the file
    fin.close()

    print('Classified')
