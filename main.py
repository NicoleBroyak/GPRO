import requests
from bs4 import BeautifulSoup
Season = "83"
Race = "3"
Group = "Rookie"
GroupNo = 1
file = open("ViewStaff.txt", "w")
file.write('Sezon\tWyścig\tKlasa\tGrupa\t#\t\tNazwisko menadżera\tNazwisko '
           'kierowcy\tOW\tPensja\tDługość\tNazwisko dyr technicznego\tOW\t'
           'Pensja\tDługość\tOW Personelu\n')
file.close()
for GroupNo in range(1, 151):
    URL = "https://gpro.net/pl/ViewStaff.asp?Group={} - {}"\
        .format(Group, GroupNo)
    page = requests.get(URL)
    print(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    trs = soup.find_all("tr")
    tds = soup.find_all("td")
    ths = soup.find_all("th")
    count = 0
    for tr in tds:
        if count == 0:
            # print(Season + '\t')
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Season))
            file.close()
        if count == 1:
            # print(Race + '\t')
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Race))
            file.close()
        if count == 2:
            # print("{} \t".format(Group))
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Group))
            file.close()
        if count == 3:
            # print("{} \t".format(GroupNo))
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(GroupNo))
            file.close()
        soup.find("tr")
        file = open("ViewStaff.txt", "a")
        file.write(tr.text.strip())
        file.write('\t')
        file.close()
        # print(tr.text.strip(), end='\t')
        count += 1
        if count == 16:
            # print('')
            count = 0
            file = open("ViewStaff.txt", "a")
            file.write('\n')
            file.close()
    GroupNo += 1
GroupNo = 1
Group = "Amateur"
for GroupNo in range(1, 81):
    URL = "https://gpro.net/pl/ViewStaff.asp?Group={} - {}"\
        .format(Group, GroupNo)
    page = requests.get(URL)
    print(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    trs = soup.find_all("tr")
    tds = soup.find_all("td")
    ths = soup.find_all("th")
    count = 0
    for tr in tds:
        if count == 0:
            # print(Season + '\t')
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Season))
            file.close()
        if count == 1:
            # print(Race + '\t')
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Race))
            file.close()
        if count == 2:
            # print("{} \t".format(Group))
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Group))
            file.close()
        if count == 3:
            # print("{} \t".format(GroupNo))
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(GroupNo))
            file.close()
        soup.find("tr")
        file = open("ViewStaff.txt", "a")
        file.write(tr.text.strip())
        file.write('\t')
        file.close()
        # print(tr.text.strip(), end='\t')
        count += 1
        if count == 16:
            # print('')
            count = 0
            file = open("ViewStaff.txt", "a")
            file.write('\n')
            file.close()
    GroupNo += 1
GroupNo = 1
Group = "Pro"
for GroupNo in range(1, 26):
    URL = "https://gpro.net/pl/ViewStaff.asp?Group={} - {}"\
        .format(Group, GroupNo)
    page = requests.get(URL)
    print(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    trs = soup.find_all("tr")
    tds = soup.find_all("td")
    ths = soup.find_all("th")
    count = 0
    for tr in tds:
        if count == 0:
            # print(Season + '\t')
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Season))
            file.close()
        if count == 1:
            # print(Race + '\t')
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Race))
            file.close()
        if count == 2:
            # print("{} \t".format(Group))
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Group))
            file.close()
        if count == 3:
            # print("{} \t".format(GroupNo))
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(GroupNo))
            file.close()
        soup.find("tr")
        file = open("ViewStaff.txt", "a")
        file.write(tr.text.strip())
        file.write('\t')
        file.close()
        # print(tr.text.strip(), end='\t')
        count += 1
        if count == 16:
            # print('')
            count = 0
            file = open("ViewStaff.txt", "a")
            file.write('\n')
            file.close()
    GroupNo += 1
GroupNo = 1
Group = "Master"
for GroupNo in range(1, 6):
    URL = "https://gpro.net/pl/ViewStaff.asp?Group={} - {}"\
        .format(Group, GroupNo)
    page = requests.get(URL)
    print(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    trs = soup.find_all("tr")
    tds = soup.find_all("td")
    ths = soup.find_all("th")
    count = 0
    for tr in tds:
        if count == 0:
            # print(Season + '\t')
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Season))
            file.close()
        if count == 1:
            # print(Race + '\t')
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Race))
            file.close()
        if count == 2:
            # print("{} \t".format(Group))
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Group))
            file.close()
        if count == 3:
            # print("{} \t".format(GroupNo))
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(GroupNo))
            file.close()
        soup.find("tr")
        file = open("ViewStaff.txt", "a")
        file.write(tr.text.strip())
        file.write('\t')
        file.close()
        # print(tr.text.strip(), end='\t')
        count += 1
        if count == 16:
            # print('')
            count = 0
            file = open("ViewStaff.txt", "a")
            file.write('\n')
            file.close()
    GroupNo += 1
GroupNo = 1
Group = "Elite"
for GroupNo in range(1, 2):
    URL = "https://gpro.net/pl/ViewStaff.asp?Group={} - {}"\
        .format(Group, GroupNo)
    page = requests.get(URL)
    print(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    trs = soup.find_all("tr")
    tds = soup.find_all("td")
    ths = soup.find_all("th")
    count = 0
    for tr in tds:
        if count == 0:
            # print(Season + '\t')
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Season))
            file.close()
        if count == 1:
            # print(Race + '\t')
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Race))
            file.close()
        if count == 2:
            # print("{} \t".format(Group))
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(Group))
            file.close()
        if count == 3:
            # print("{} \t".format(GroupNo))
            count += 1
            file = open("ViewStaff.txt", "a")
            file.write('{}\t'.format(GroupNo))
            file.close()
        soup.find("tr")
        file = open("ViewStaff.txt", "a")
        file.write(tr.text.strip())
        file.write('\t')
        file.close()
        # print(tr.text.strip(), end='\t')
        count += 1
        if count == 16:
            # print('')
            count = 0
            file = open("ViewStaff.txt", "a")
            file.write('\n')
            file.close()
    GroupNo += 1
