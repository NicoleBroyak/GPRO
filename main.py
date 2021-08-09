import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import mechanize
import urllib3
import http.cookiejar


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


def man_sponsors():
    group = "Rookie"
    season = "83"
    race = "3"
    file = open("ManSponsors.txt", "w")
    file.write("")
    file.close()
    for group_no in range(1, 151):
        url = "https://gpro.net/pl/ManSponsors.asp?group={} - {}" \
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
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group_no))
                file.close()
            if 4 <= count <= 8 or count == 15:
                file = open("ManSponsors.txt", "a")
                file.write(tr.text.strip())
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if 9 <= count <= 14:
                script = str(tr.find("script"))
                lvl = (script[48:49])
                lvl = int(lvl) + 1
                file = open("ManSponsors.txt", "a")
                file.write(str(lvl))
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if count == 16:
                # print('')
                count = 0
                file = open("ManSponsors.txt", "a")
                file.write('\n')
                file.close()
        group_no += 1
    group = "Amateur"
    for group_no in range(1, 81):
        url = "https://gpro.net/pl/ManSponsors.asp?group={} - {}" \
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
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group_no))
                file.close()
            if 4 <= count <= 8 or count == 15:
                file = open("ManSponsors.txt", "a")
                file.write(tr.text.strip())
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if 9 <= count <= 14:
                script = str(tr.find("script"))
                lvl = (script[48:49])
                lvl = int(lvl) + 1
                file = open("ManSponsors.txt", "a")
                file.write(str(lvl))
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if count == 16:
                # print('')
                count = 0
                file = open("ManSponsors.txt", "a")
                file.write('\n')
                file.close()
        group_no += 1
    group = "Pro"
    for group_no in range(1, 26):
        url = "https://gpro.net/pl/ManSponsors.asp?group={} - {}" \
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
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group_no))
                file.close()
            if 4 <= count <= 8 or count == 15:
                file = open("ManSponsors.txt", "a")
                file.write(tr.text.strip())
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if 9 <= count <= 14:
                script = str(tr.find("script"))
                lvl = (script[48:49])
                lvl = int(lvl) + 1
                file = open("ManSponsors.txt", "a")
                file.write(str(lvl))
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if count == 16:
                # print('')
                count = 0
                file = open("ManSponsors.txt", "a")
                file.write('\n')
                file.close()
        group_no += 1
    group = "Master"
    for group_no in range(1, 6):
        url = "https://gpro.net/pl/ManSponsors.asp?group={} - {}" \
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
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group_no))
                file.close()
            if 4 <= count <= 8 or count == 15:
                file = open("ManSponsors.txt", "a")
                file.write(tr.text.strip())
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if 9 <= count <= 14:
                script = str(tr.find("script"))
                lvl = (script[48:49])
                lvl = int(lvl) + 1
                file = open("ManSponsors.txt", "a")
                file.write(str(lvl))
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if count == 16:
                # print('')
                count = 0
                file = open("ManSponsors.txt", "a")
                file.write('\n')
                file.close()
        group_no += 1
    group = "Elite"
    for group_no in range(1, 2):
        url = "https://gpro.net/pl/ManSponsors.asp?group={} - {}" \
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
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("ManSponsors.txt", "a")
                file.write('{}\t'.format(group_no))
                file.close()
            if 4 <= count <= 8 or count == 15:
                file = open("ManSponsors.txt", "a")
                file.write(tr.text.strip())
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if 9 <= count <= 14:
                script = str(tr.find("script"))
                lvl = (script[48:49])
                lvl = int(lvl) + 1
                file = open("ManSponsors.txt", "a")
                file.write(str(lvl))
                file.write('\t')
                file.close()
                # print(tr.text.strip(), end='\t')
                count += 1
            if count == 16:
                # print('')
                count = 0
                file = open("ManSponsors.txt", "a")
                file.write('\n')
                file.close()
        group_no += 1

def money_levels():
    group = "Elite"
    season = "83"
    race = "3"
    group_no = 1
    file = open("MoneyLevels.txt", "w")
    user = input("User")
    password = input("Pass")
    file.write('Sezon\tWyścig\tKlasa\tGrupa\t#\t\tNazwisko menadżera\tNazwisko '
               'kierowcy\tOW\tPensja\tDługość\tNazwisko dyr technicznego\tOW\t'
               'Pensja\tDługość\tOW Personelu\n')
    driver = webdriver.Chrome()
    driver.get("https://gpro.net/pl/Login.asp?Redirect=MoneyLevels.asp")
    driver.find_element_by_name("textLogin").send_keys(user)
    driver.find_element_by_name("textPassword").send_keys(password)
    driver.find_element_by_name("LogonFake").click()
    file.close()
    for group_all in range(1, 262):
        with open('page.html', 'w') as f:
            f.write(driver.page_source)
        p = open('page.html', 'r')
        page = p.read()

        soup = BeautifulSoup(page, "html.parser")
        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                # print(season + '\t')
                count += 1
                file = open("MoneyLevels.txt", "a")
                file.write('{}\t'.format(season))
                file.close()
            if count == 1:
                # print(race + '\t')
                count += 1
                file = open("MoneyLevels.txt", "a")
                file.write('{}\t'.format(race))
                file.close()
            if count == 2:
                # print("{} \t".format(group))
                count += 1
                file = open("MoneyLevels.txt", "a")
                file.write('{}\t'.format(group))
                file.close()
            if count == 3:
                # print("{} \t".format(group_no))
                count += 1
                file = open("MoneyLevels.txt", "a")
                file.write('{}\t'.format(group_no))
                file.close()
            soup.find("tr")
            file = open("MoneyLevels.txt", "a")
            file.write(tr.text.strip())
            file.write('\t')
            file.close()
            # print(tr.text.strip(), end='\t')
            count += 1
            if count == 12:
                # print('')
                count = 0
                file = open("MoneyLevels.txt", "a")
                file.write('\n')
                file.close()
        group_no += 1
        if group_all == 1:
            group = "Master"
            group_no = 1
        if group_all == 6:
            group = "Pro"
            group_no = 1
        if group_all == 31:
            group = "Amateur"
            group_no = 1
        if group_all == 111:
            group = "Rookie"
            group_no = 1
        driver.find_element_by_class_name("next").click()

konsola = 1
while konsola != "0":
    konsola = input("Wpisz komende\n[1] RichDad\n[2] BestFans\
                    \n[3] Wydatki\n[4] Personel\n[5] MoneyLevels\n[6] Sponsorzy menedżerów\n:")
    if konsola == "1":
        print("uruchamiam funkcje rich")
        rich()
    if konsola == "2":
        print("uruchamiam funkcje bestfans")
        best_cars()
    if konsola == "3":
        print("uruchamiam funkcje wydatki")
        expenses()
    if konsola == "4":
        print("uruchamiam funkcje personel")
        view_staff()
    if konsola == "5":
        print("uruchamiam funkcje moneylevels")
        money_levels()
    if konsola == "6":
        print("uruchamiam funkcje sponsorzymenedzerow")
        man_sponsors()
    else:
        print("Wpisz wlasciwy numer")

print("Koniec programu")