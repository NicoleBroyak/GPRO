import datetime
import time
from datetime import date

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pathlib
import logging
import os
import shutil


def group_scrap(_):
    if _ in range(112, 262):
        group = "Rookie"
    if _ in range(32, 112):
        group = "Amateur"
    if _ in range(7, 32):
        group = "Pro"
    if _ in range(2, 7):
        group = "Master"
    if _ == 1:
        group = "Elite"
    return group


def group_scrap_mode_type(_):
    if _ in range(112, 262):
        group = "R"
    if _ in range(32, 112):
        group = "A"
    if _ in range(7, 32):
        group = "P"
    if _ in range(2, 7):
        group = "M"
    if _ == 1:
        group = "E"
    return group


def rich_or_exp_scrap(string, file_path, max_pageno, scraptype):
    count = 0
    countall = 0
    for page_no in range(1, max_pageno):
        url = str(f"https://gpro.net/pl/Stats.asp?type={scraptype}&P"
                  f"age={page_no}")
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        tbs = soup.find(id="Table16")
        tds = tbs.find_all("td")
        for tr in tds:
            if countall < 4:
                countall += 1
                continue
            if count == 0:
                write("a", f"{season},{race}.{datatime},", file_path)
            tbs.find("tr")
            if count == 1:
                s = str(tr.text.strip())
                text_without_digits = ''.join(
                    i for i in s if not i.isdigit())
                write("a", f"{text_without_digits}", file_path)
            if count == 0 or count in range(2, 5):
                write("a", tr.text.strip().replace(".", "").replace("$", ""),
                      file_path)
            if count != 3:
                write("a", ",", file_path)
            count += 1
            countall += 1
            if count == 4:
                count = 0
                write("a", "\n", file_path)
        print(f"[{string}] {page_no}/{max_pageno - 1} "
              f"Ukończono: "
              f"{float(page_no/(max_pageno - 1)*100).__round__(2)}%")
        page_no += 1
        countall = 0


def write(mode, string, file_path):
    try:
        with open(file_path, mode=mode, encoding="utf-8") as file:
            file.write(string)
    except OSError:
        logging.error("Error")


def max_page(soup):
    max_page_calc = soup.find_all("u")
    max_page_number = None
    for _ in max_page_calc:
        max_page_number = _
    max_pageno = int(max_page_number.text.strip()) + 1
    return max_pageno


def best_cars_scrap(file_path, max_pageno):
    for page_no in range(1, max_pageno):
        count = 0
        countall = 0
        url = f"https://gpro.net/pl/Stats.asp?typ" \
              f"e=bestcars&Page={page_no}"
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
                count += 1
                write("a", f"{season},{race}.{datatime},", file_path)
            if count == 2:
                s = str(tr.text.strip())
                text_without_digits = ''.join(
                    i for i in s if not i.isdigit())
                write("a", f"{text_without_digits},", file_path)
            if count in range(3, 5) or count == 1:
                write("a", tr.text.strip().replace(".", ""), file_path)
                if count != 3:
                    write("a", ",", file_path)
                lvl = 0
            if count == 5:
                tr.find_all("img")
                for _ in tr:
                    lvl += 1
                lvl -= 2
                write("a", str(lvl), file_path)
            count += 1
            countall += 1
            if count == 6:
                write("a", "\n", file_path)
                count = 0
        print(f"[BESTCARS] {page_no}/{max_pageno - 1} "
              f"Ukończono: {float(page_no/(max_pageno - 1)*100).__round__(2)}%")
        page_no += 1


def man_spons_scrap(file_path):
    groupsall = group_dict[mode_type2] - group_dict[mode_type1] + 1
    countgroupcalc = 1
    for _ in range(group_dict[mode_type1], group_dict[mode_type2] + 1):
        group = group_scrap(_)
        if _ == 1 or _ == 2 or _ == 7 or _ == 32 or _ == 112:
            group_no = 1
        url = f"https://gpro.net/pl/ManSponsors.asp?group={group} - {group_no}"
        page = requests.get(url)
        print(f"[SPONSORZY] Pobieranie strony {group} - {group_no} "
              f"{countgroupcalc}/{group_dict[mode_type2]} "
              f"Ukończono: "
              f"{float((countgroupcalc / groupsall) * 100).__round__(2)}%")
        soup = BeautifulSoup(page.content, "html.parser")
        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                write("a", f"{season},{race}.{datatime},{group}"
                           f" - {group_no},", file_path)
                count += 4
            if 4 <= count <= 8 or count == 15:
                if count == 6:
                    s = str(tr.text.strip())
                    text_without_digits = ''.join(
                        i for i in s if not i.isdigit())
                    write("a", f"{text_without_digits},", file_path)
                if count not in range(4, 7):
                    write("a", f"{tr.text.strip()}", file_path)
                    if count == 6 or count == 7:
                        write("a", ",", file_path)
                count += 1
            if 9 <= count <= 14:
                script = str(tr.find("script"))
                lvl = (script[48:49])
                lvl = int(lvl) + 1
                write("a", f"{str(lvl)},", file_path)
                count += 1
            if count == 16:
                write("a", "\n", file_path)
                count = 0
        group_no += 1
        countgroupcalc += 1


def view_staff_scrap(file_path):
    groupsall = group_dict[mode_type2] - group_dict[mode_type1] + 1
    countgroupcalc = 1
    for _ in range(group_dict[mode_type1], group_dict[mode_type2] + 1):
        group = group_scrap(_)
        if _ == 1 or _ == 2 or _ == 7 or _ == 32 or _ == 112:
            group_no = 1
        url = str(f"https://gpro.net/pl/ViewStaff.asp?group={group} "
                  f"- {group_no}")
        page = requests.get(url)
        print(f"[PERSONEL] Pobieranie strony {group} - {group_no} "
              f"{countgroupcalc}/{group_dict[mode_type2]} "
              f"Ukończono: "
              f"{float((countgroupcalc / groupsall) * 100).__round__(2)}%")
        soup = BeautifulSoup(page.content, "html.parser")
        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                write("a", f"{season},{race}.{datatime},{group} - {group_no},",
                      file_path)
                soup.find("tr")
            soup.find("tr")
            if count == 2:
                s = str(tr.text.strip())
                text_without_digits = ''.join(i for i in s if not i.isdigit())
                write("a", f"{text_without_digits},", file_path)
            if count > 2:
                write("a", tr.text.strip().replace(".", "").
                      replace("$", "").replace("\n", ""), file_path)
                if count != 11:
                    write("a", ",", file_path)
            count += 1
            if count == 12:
                count = 0
                write("a", "\n", file_path)
        group_no += 1
        countgroupcalc += 1


def best_cars():
    file_path = os.getcwd() + "/BestCarsBase.csv"
    file_path2 = os.getcwd() + "/BestCars.csv"
    write("w", "", file_path2)
    write("w", f"Sezon,Wyścig,Poz.,Nazwisko,Grupa,lvl\n", file_path)
    url = "https://gpro.net/pl/Stats.asp?type=bestcars&Page=1"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    max_pageno = max_page(soup)
    best_cars_scrap(file_path, max_pageno)
    rookie_del = "Rookie"
    ama_del = "Amateur"
    with open("BestCarsBase.csv") as oldfile, open("BestCars.csv", 'w') \
            as newfile:
        for line in oldfile:
            if rookie_del not in line and ama_del not in line:
                newfile.write(line)
    os.remove("BestCarsBase.csv")


def view_staff():

    file_path = os.getcwd() + "/Staff.csv"
    write("w", 'Sezon,Wyścig,Grupa,Nazwisko menadżera,Nazwisko kierowcy,OW,'
               'Pensja,Długość,Nazwisko dyrtechnicznego,OW,Pensja,Długość,'
               'OW Personelu\n', file_path)
    view_staff_scrap(file_path)


def rich():
    file_path = os.getcwd() + "/RichBase.csv"
    file_path2 = os.getcwd() + "/Rich.csv"
    write("w", "", file_path2)
    write("w", "Sezon,Wyścig,Poz,Nazwisko,Grupa,Budżet\n", file_path)
    urlbase = "https://gpro.net/pl/Stats.asp?type=richmanagers&Page=1"
    page = requests.get(urlbase)
    soup = BeautifulSoup(page.content, "html.parser")
    max_pageno = max_page(soup)
    scraptype = "richmanagers"
    rich_or_exp_scrap("BUDŻETY", file_path, max_pageno, scraptype)
    rookie_del = "Rookie"
    ama_del = "Amateur"
    with open("RichBase.csv") as oldfile, open("Rich.csv", 'w') \
            as newfile:
        for line in oldfile:
            if rookie_del not in line and ama_del not in line:
                newfile.write(line)
    os.remove("RichBase.csv")


def expenses():
    file_path = os.getcwd() + "/ExpensesBase.csv"
    file_path2 = os.getcwd() + "/Expenses.csv"
    write("w", "Sezon,Wyścig,Poz.,Nazwisko,Grupa,Wydatki\n", file_path)
    write("w", "", file_path2)
    url = "https://gpro.net/pl/Stats.asp?type=mostcost&Page=1"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    max_pageno = max_page(soup)
    scraptype = "mostcost"
    rich_or_exp_scrap("WYDATKI", file_path, max_pageno, scraptype)
    rookie_del = "Rookie"
    ama_del = "Amateur"
    with open("ExpensesBase.csv") as oldfile, \
            open("Expenses.csv", "w") as newfile:
        for line in oldfile:
            if rookie_del not in line and ama_del not in line:
                newfile.write(line)
    os.remove("ExpensesBase.csv")


def man_sponsors():
    file_path = os.getcwd() + "/ManSponsors.csv"
    write("w", "Sezon,Wyścig,Grupa,Nazwisko,Sponsor,Finanse,Oczekiwania,"
          "Cierpliwość,Reputacja,Wizerunek,Negocjacje,Czastrwania\n", file_path)
    man_spons_scrap(file_path)


def money_levels():
    file_path = os.getcwd() + "/MoneyLevels.csv"
    write("w", "Sezon,Wyścig,Grupa,Nazwisko,Budżet,Poziom samochodu"
          ",Dopasowanie,Punkty\n", file_path)
    user = "NeilLight"
    password = "GPRO2137"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=800,800')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome()
    driver.get("https://gpro.net/pl/Login.asp?Redirect=MoneyLevels.asp")
    driver.find_element_by_name("textLogin").send_keys(user)
    driver.find_element_by_name("textPassword").send_keys(password)
    driver.find_element_by_name("LogonFake").click()
    groupsall = group_dict[mode_type2] - group_dict[mode_type1] + 1
    groupsall = (groupsall * 100)
    countgroupcalc = 1
    for _ in range(group_dict[mode_type1], group_dict[mode_type2] + 1):

        group = group_scrap(_)
        if _ == 1 or _ == 2 or _ == 7 or _ == 32 or _ == 112:
            group_no = 1
        print(f"[MONEYLEVELS] Pobieranie strony {group} - {group_no} "
              f"{countgroupcalc}/{group_dict[mode_type2]} "
              f"Ukończono: "
              f"{float(countgroupcalc / groupsall * 100).__round__(2)}%")
        with open('page.html', 'w') as f:
            f.write(driver.page_source)
        p = open('page.html', 'r')
        page = p.read()
        p.close()
        soup = BeautifulSoup(page, "html.parser")
        tds = soup.find_all("td")
        count = 0
        for tr in tds:
            if count == 0:
                count += 1
                write("a", f"{season},{race}.{datatime},{group}"
                           f" - {group_no},", file_path)
            soup.find("tr")
            if count != 1 and count != 4:
                if count == 2:
                    s = str(tr.text.strip())
                    text_without_digits = ''.join(
                        i for i in s if not i.isdigit())
                    write("a", f"{text_without_digits}", file_path)
                if count > 2:
                    write("a", tr.text.strip().replace(".", "").
                          replace("$", ""), file_path)
                if count != 8 and count != 7:
                    write("a", ",", file_path)
            count += 1
            if count == 9:
                count = 0
                write("a", "\n", file_path)
        group_no += 1
        _ += 1
        countgroupcalc += 1
        driver.find_element_by_class_name("next").click()
    driver.close()
    os.remove("page.html")


def analiza():
    user = input("User")
    password = input("Pass")
    driver = webdriver.Chrome()
    driver.get("https://gpro.net/pl/Login.asp?Redirect=RaceAnalysis.asp")
    driver.find_element_by_name("textLogin").send_keys(user)
    driver.find_element_by_name("textPassword").send_keys(password)
    driver.find_element_by_name("LogonFake").click()
    with open('page.html', 'w') as file:
        file.write(driver.page_source)
    p = open('page.html', 'r')
    page = p.read()
    soup = BeautifulSoup(page, "html.parser")
    tds = soup.find_all("td")
    for tr in tds:
        file = open("Analiza.txt", "a")
        soup.find("tr")
        file.write(tr.text.strip())
        file.write('\n')
        file.close()
    file = open("Analiza1.txt", "a")
    file.write(soup.text.strip())
    file.close()


datenow = datetime.datetime.now()
weekday = date.isoweekday(datenow)
strdatenow = str(datenow)
hour = int(strdatenow[11:13])
minute = strdatenow[14:16]
group_dict = {}
allgroups = 1
if weekday == 2 or weekday == 5:
    if hour in range(19, 22):
        datatime = "3"
    if hour in range(22, 24):
        datatime = "1"
    else:
        datatime = f"{strdatenow[5:]}"
else:
    datatime = f"{strdatenow[5:]}"
if weekday == 1 or weekday == 4 and hour in range(19, 21):
    datatime = "2"
else:
    datatime = f"{strdatenow[5:]}"
for count_dict in range(1, 262):
    group_code = group_scrap_mode_type(count_dict)
    if count_dict == 1:
        group_dict[group_code] = count_dict
    else:
        group_dict[(group_code + str(allgroups))] = count_dict
    allgroups += 1
    count_dict += 1
    if count_dict == 2 or count_dict == 7 or \
       count_dict == 32 or count_dict == 112:
        allgroups = 1
mainurl = "https://gpro.net"
mainpage = requests.get(mainurl)
mainsoup = BeautifulSoup(mainpage.content, "html.parser")
racebar = mainsoup.find(id="racebar").text.strip()
season = racebar[23:25]
race = racebar[34:36].replace(":", "")
mode_type = input("Wpisz [1] aby wybrać zakres grup np. od [E] do [R150]\n"
                  "inna wartość = tryb domyślny (od [E] do [P25])")
mode_type1 = "E"
mode_type2 = "P25"
if mode_type == "1":
    mode_type1 = input("Wpisz grupę startową")
    mode_type2 = input("Wpisz grupę końcową")
konsola = 1
base_dir = os.getcwd()
os.mkdir(f"S{season}_R{race}_N{datatime}___{time.strftime('%d_%m___%H%M')}")
mkdir = str(f"S{season}_R{race}_N{datatime}___{time.strftime('%d_%m___%H%M')}")
os.chdir(base_dir + f"/{mkdir}")
newdir = os.getcwd()
while konsola != "0":
    konsola = input("Wpisz komende:\n[1] RichDad\t[2] BestFans"
                    "\t[3] Wydatki\n[4] Personel\t[5] MoneyLevels\t"
                    "[6] Sponsorzy menedżerów\n[7] Analiza\t"
                    "[8] Wszystko z logowaniem\n"
                    "[9] Wszystko bez logowania i wydatków\t[0] Wyjdź\n:")
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
    if konsola == "7":
        print("Funkcja do wdrożenia")
    if konsola == "8":
        print("Funkcja do wdrożenia")
    if konsola == "9":
        rich()
        best_cars()
        man_sponsors()
        view_staff()
print("Koniec programu")
os.chdir(base_dir)
shutil.make_archive(pathlib.Path(f"{mkdir}").absolute()
                    .as_posix(), "zip", pathlib.Path(f"{mkdir}")
                    .absolute().as_posix())
shutil.rmtree(mkdir, ignore_errors=True)
