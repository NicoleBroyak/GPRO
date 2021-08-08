import requests
from bs4 import BeautifulSoup


def best_cars():
    season = "83"
    race = "3"
    lvl = 0
    file = open("BestCars.txt", "w")
    file.write("")
    file.close()
    url = "https://gpro.net/pl/Stats.asp?type=bestcars&Page=1"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    max_page = soup.find_all("u")
    for u in max_page:
        max_page_number = u
    max_pageno = int(max_page_number.text.strip()) + 1
    count = 0
    countall = 0
    for page_no in range(1, max_pageno):
        url = "https://gpro.net/pl/Stats.asp?typ" \
              "e=bestcars&Page={}".format(page_no)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        tbs = soup.find(id="Table16")
        tds = tbs.find_all("td")
        for tr in tds:
            if countall < 4:
                countall += 1
                continue
            tbs.find("tr")
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("BestCars.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("BestCars.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count <= 5:
                file = open("BestCars.txt", "a")
                file.write(tr.text.strip())
                file.write("\t")
                file.close()
            if count == 6:
                imgs = tr.find_all("img")
                for imgs in tr:
                    lvl += 1
                lvl -= 2
                file = open("BestCars.txt", "a")
                file.write(str(lvl))
                file.write("\t")
                file.close()
                lvl = 0
            count += 1
            countall += 1
            if count == 7:
                file = open("BestCars.txt", "a")
                file.write("\n")
                file.close()
                count = 0
        print(page_no)
        page_no += 1
        countall = 0


def view_staff():
    season = "83"
    race = "3"
    group = "Rookie"
    file = open("ViewStaff.txt", "w")
    file.write('Sezon\tWyścig\tKlasa\tGrupa\t#\t\tNazwisko menadżera\tNazwisko '
               'kierowcy\tOW\tPensja\tDługość\tNazwisko dyr technicznego\tOW\t'
               'Pensja\tDługość\tOW Personelu\n')
    file.close()
    for group_no in range(1, 151):
        url = "https://gpro.net/pl/ViewStaff.asp?group={} - {}" \
            .format(group, group_no)
        page = requests.get(url)
        print(url)

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(group_no))
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
        group_no += 1
    group = "Amateur"
    for group_no in range(1, 81):
        url = "https://gpro.net/pl/ViewStaff.asp?group={} - {}"\
            .format(group, group_no)
        page = requests.get(url)
        print(url)

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(group_no))
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
        group_no += 1
    group = "Pro"
    for group_no in range(1, 26):
        url = "https://gpro.net/pl/ViewStaff.asp?group={} - {}"\
            .format(group, group_no)
        page = requests.get(url)
        print(url)

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(group_no))
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
        group_no += 1
    group = "Master"
    for group_no in range(1, 6):
        url = "https://gpro.net/pl/ViewStaff.asp?group={} - {}"\
            .format(group, group_no)
        page = requests.get(url)
        print(url)

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(group_no))
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
        group_no += 1
    group = "Elite"
    for group_no in range(1, 2):
        url = "https://gpro.net/pl/ViewStaff.asp?group={} - {}"\
            .format(group, group_no)
        page = requests.get(url)
        print(url)

        soup = BeautifulSoup(page.content, "html.parser")

        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ViewStaff.txt", "a")
                file.write('{}\t'.format(group_no))
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
        group_no += 1


def rich():
    season = "83"
    race = "3"
    file = open("Rich.txt", "w")
    file.write("")
    file.close()
    url = "https://gpro.net/pl/Stats.asp?type=richmanagers&Page=1"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    max_page = soup.find_all("u")
    for u in max_page:
        max_page_number = u
    max_pageno = int(max_page_number.text.strip()) + 1
    count = 0
    countall = 0
    for page_no in range(1, max_pageno):
        url = "https://gpro.net/pl/Stats.asp?type=" \
              "richmanagers&Page={}".format(page_no)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        tbs = soup.find(id="Table16")
        tds = tbs.find_all("td")
        for tr in tds:
            if countall < 4:
                countall += 1
                continue
            tbs.find("tr")
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("Rich.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("Rich.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            file = open("Rich.txt", "a")
            file.write(tr.text.strip())
            file.write("\t")
            file.close()
            count += 1
            countall += 1
            if count == 6:
                file = open("Rich.txt", "a")
                file.write("\n")
                file.close()
                count = 0
        print(page_no)
        page_no += 1
        countall = 0


def expenses():
    season = "83"
    race = "3"
    file = open("Expenses.txt", "w")
    file.write("")
    file.close()
    url = "https://gpro.net/pl/Stats.asp?type=mostcost&Page=1"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    max_page = soup.find_all("u")
    for u in max_page:
        max_page_number = u
    max_pageno = int(max_page_number.text.strip()) + 1
    count = 0
    countall = 0
    for page_no in range(1, max_pageno):
        url = "https://gpro.net/pl/Stats.asp?type=" \
              "mostcost&Page={}".format(page_no)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        tbs = soup.find(id="Table16")
        tds = tbs.find_all("td")
        for tr in tds:
            if countall < 4:
                countall += 1
                continue
            tbs.find("tr")
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("Expenses.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("Expenses.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            file = open("Expenses.txt", "a")
            file.write(tr.text.strip())
            file.write("\t")
            file.close()
            count += 1
            countall += 1
            if count == 6:
                file = open("Expenses.txt", "a")
                file.write("\n")
                file.close()
                count = 0
        print(page_no)
        page_no += 1
        countall = 0


expenses()
rich()
view_staff()
best_cars()
