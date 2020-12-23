import glob
import os
import pandas as pd
import tkinter as tk
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import string


def deletedash(email, password):
    driver = webdriver.Chrome(executable_path="chromedriver.exe")

    driver.get("http://unlimitedmailinglists.com/site/auth/login.asp")
    driver.find_element_by_name("Email").send_keys(email)
    driver.find_element_by_name("Password").send_keys(password)
    driver.find_element_by_css_selector("input[alt=Submit]").click()
    driver.find_element_by_link_text('Dashboard').click()
    time.sleep(1)
    links = driver.find_elements_by_tag_name("a")

    while (len(links) - 3):
        # time.sleep(1)
        links[13].click()
        # time.sleep(1)
        driver.switch_to_alert().accept()
        time.sleep(1)  # 3sec is perfect try reducing and then see if it works
        links = driver.find_elements_by_tag_name("a")
        # time.sleep(1)

    driver.close()


def excel():
    # CHANGE PATH FOR JAGDEEP PC
    # subject_path = r"C:\Users\Sanwal\Downloads"
    subject_path = os.path.expanduser("~")+r"\Downloads"
    all_files = glob.glob(subject_path + "/*.csv")
    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, usecols=["Phone"])
        li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)

    frame.drop_duplicates(subset="Phone", keep='first', inplace=True)  # to remove duplicates
    # CHANGE PATH FOR JAGDEEP PC
    # frame.to_csv(r"C:\Users\Sanwal\Desktop\final.csv", index=False, header=True)  # TO GET FILE ON DESKTOP
    frame.to_csv(os.path.expanduser("~")+"\Desktop\\final.csv", index=None, header=True)#TO GET FILE IN SETUP FOLDER


def download(email, password):
    driver = webdriver.Chrome(executable_path="chromedriver.exe")

    driver.get("http://unlimitedmailinglists.com/site/auth/login.asp")
    driver.find_element_by_name("Email").send_keys(email)
    driver.find_element_by_name("Password").send_keys(password)
    driver.find_element_by_css_selector("input[alt=Submit]").click()
    driver.find_element_by_link_text('Dashboard').click()

    links = driver.find_elements_by_tag_name('a')

    for i in range(11, len(links) - 3):
        if (i - 11) % 3 == 0:
            links[i].click()

    time.sleep(15)
    driver.close()

    excel()
    deletedash(email, password)


def search(email, password, state, gender, start, ed):
    lt = list(string.ascii_uppercase)
    lt2 = list(string.ascii_uppercase)
    m = 1
    # ADD INCOME DICTIONARY HERE
    income = {
        '$0 -$10, 000': 1,
        '$10, 000 -$14, 999': 2,
        '$15, 000 -$19, 999': 3,
        '$20, 000 -$24, 999': 4,
        '$25, 000 -$29, 999': 5,
        '$30, 000 -$34, 999': 6,
        '$35, 000 -$39, 999': 7,
        '$40, 000 -$44, 999': 8,
        '$45, 000 -$49, 999': 9,
        '$50, 000 -$54, 999': 10,
        '$55, 000 -$59, 999': 11,
        '$60, 000 -$64, 999': 12,
        '$65, 000 -$74, 999': 13,
        '$75, 000 -$99, 999': 14,
        '$100, 000 -$149, 999': 15,
        '$150, 000 -$174, 999': 16,
        '$175, 000 -$199, 999': 17,
        '$200, 000 -$249, 999': 18,
        '$250, 000 +': 19
    }

    states = {
        'Alabama': 1,
        'California': 2,
        'Florida': 3,
        'Georgia': 4,
        'Idaho': 5,
        'Illinois': 6,
        'Indiana': 7,
        'Iowa': 8,
        'Kansas': 9,
        'Kentucky': 10,
        'Maine': 11,
        'Marshall Islands': 12,
        'Maryland': 13,
        'Massachusetts': 14,
        'Michigan': 15,
        'Minnesota': 16,
        'Minor Outlying Islands': 17,
        'Mississippi': 18,
        'Missouri': 19,
        'Montana': 20,
        'Nebraska': 21,
        'Nevada': 22,
        'New Hampshire': 23,
        'New Jersey': 24,
        'New Mexico': 25,
        'New York': 26,
        'North Carolina': 27,
        'North Dakota': 28,
        'Northern Mariana Islands': 29,
        'Ohio': 30,
        'Oklahoma': 31,
        'Oregon': 32,
        'Palau': 33,
        'Pennsylvania': 34,
        'Philippine Islands': 35,
        'Puerto Rico': 36,
        'Rhode Island': 37,
        'South Carolina': 38,
        'South Dakota': 39,
        'Tennessee': 40,
        'Texas': 41,
        'Utah': 42,
        'Vermont': 43,
        'Virgin Islands': 44,
        'Virginia': 45,
        'Washington': 46,
        'West Virginia': 47,
        'Wisconsin': 48,
        'Wyoming': 49
    }

    driver = webdriver.Firefox(executable_path="geckodriver.exe")
    wait = WebDriverWait(driver, 20)
    driver.get("http://unlimitedmailinglists.com/site/auth/login.asp")
    driver.find_element_by_name("Email").send_keys(email)
    driver.find_element_by_name("Password").send_keys(password)
    driver.find_element_by_css_selector("input[alt=Submit]").click()

    # ADD LOOPS HERE FOR AGE,GENDER,INCOME
    for i in lt[income.get(start):income.get(ed)+1]:  # THIS LOOP IS FOR INCOME ...i is used for income
        for j in lt2[3:7]:  # this loop is for age

            # SELECTING STATE
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='type1']")))
            driver.find_element_by_css_selector("input[value=C]").click()
            dp = Select(driver.find_element_by_name("statecode"))  # choosing drop down box
            dp.select_by_index(states.get(state))  # Selecting State
            driver.find_element_by_id("sb3").click()  # CLICKING ON FILTERs

            # SELECTING GENDER
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='gender']")))
            if gender == "MALE":
                driver.find_element_by_css_selector("input[value=M]").click()
            else:
                driver.find_element_by_css_selector("input[value=F]").click()

            # SELECTING AGE

            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='age']")))
            driver.find_element_by_xpath("//*[@id='age'][@value='" + j + "']").click()

            # SELECTING INCOME
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='income']")))
            driver.find_element_by_xpath("//*[@id='income'][@value='" + i + "']").click()

            # CLICKING ON DOWNLOAD
            driver.find_element_by_id("sb4").click()  # CLICKING ON DOWNLOAD
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='DownloadDescription']")))
            driver.find_element_by_id("DownloadDescription").send_keys(m)
            m += 1
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sb5']")))
            driver.find_element_by_id("sb5").click()  # CLICKING ON START DOWNLOAD
            driver.find_element_by_link_text('Search').click()

    driver.close()
    download(email, password)


HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

email = tk.Entry(canvas, font=40)
email.place(relx=0.5, rely=0.05, relwidth=0.3, relheight=0.05)

password = tk.Entry(canvas, font=40)
password.place(relx=0.5, rely=0.15, relwidth=0.3, relheight=0.05)

emaillabel = tk.Label(canvas, text='EMAIL', font=40)
emaillabel.place(relx=0.1, rely=0.05, relwidth=0.3, relheight=0.05)

passwordlabel = tk.Label(canvas, text='PASSWORD', font=40)
passwordlabel.place(relx=0.1, rely=0.15, relwidth=0.3, relheight=0.05)

states = [
    'Alabama',
    'California',
    'Florida',
    'Georgia',
    'Idaho',
    'Illinois',
    'Indiana',
    'Iowa',
    'Kansas',
    'Kentucky',
    'Maine',
    'Marshall Islands',
    'Maryland',
    'Massachusetts',
    'Michigan',
    'Minnesota',
    'Minor Outlying Islands',
    'Mississippi',
    'Missouri',
    'Montana',
    'Nebraska',
    'Nevada',
    'New Hampshire',
    'New Jersey',
    'New Mexico',
    'New York',
    'North Carolina',
    'North Dakota',
    'Northern Mariana Islands',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Palau',
    'Pennsylvania',
    'Philippine Islands',
    'Puerto Rico',
    'Rhode Island',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Vermont',
    'Virgin Islands',
    'Virginia',
    'Washington',
    'West Virginia',
    'Wisconsin',
    'Wyoming'
]
# INCOME LIST
inc = [
    '$0 -$10, 000',
    '$10, 000 -$14, 999',
    '$15, 000 -$19, 999',
    '$20, 000 -$24, 999',
    '$25, 000 -$29, 999',
    '$30, 000 -$34, 999',
    '$35, 000 -$39, 999',
    '$40, 000 -$44, 999',
    '$45, 000 -$49, 999',
    '$50, 000 -$54, 999',
    '$55, 000 -$59, 999',
    '$60, 000 -$64, 999',
    '$65, 000 -$74, 999',
    '$75, 000 -$99, 999',
    '$100, 000 -$149, 999',
    '$150, 000 -$174, 999',
    '$175, 000 -$199, 999',
    '$200, 000 -$249, 999',
    '$250, 000 +'
]

statevar = tk.StringVar()
StateMenu = tk.OptionMenu(root, statevar, *states)
StateMenu.place(relx=0.5, rely=0.25, relwidth=0.3, relheight=0.05)

statelabel = tk.Label(canvas, text='STATE', font=40)
statelabel.place(relx=0.1, rely=0.25, relwidth=0.3, relheight=0.05)

gender = tk.StringVar()
gendermenu = tk.OptionMenu(root, gender, "MALE", "FEMALE")
gendermenu.place(relx=0.5, rely=0.35, relwidth=0.3, relheight=0.05)

genderlabel = tk.Label(canvas, text='GENDER', font=40)
genderlabel.place(relx=0.1, rely=0.35, relwidth=0.3, relheight=0.05)

incomestart = tk.StringVar()
incomeend = tk.StringVar()
incomemenu = tk.OptionMenu(root, incomestart, *inc)
incomemenu.place(relx=0.5, rely=0.45, relwidth=0.1, relheight=0.05)

incomemenu2 = tk.OptionMenu(root, incomeend, *inc)
incomemenu2.place(relx=0.7, rely=0.45, relwidth=0.1, relheight=0.05)

incomelabel = tk.Label(canvas, text='INCOME', font=40)
incomelabel.place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.05)

incomelabel2 = tk.Label(canvas, text='TO', font=40)
incomelabel2.place(relx=0.5, rely=0.45, relwidth=0.3, relheight=0.05)

age = tk.Label(canvas, text='AGE IS FIXED BETWEEN 40 AND 80', font=40)
age.place(relx=0.2, rely=0.55, relwidth=0.6, relheight=0.05)

button = tk.Button(root, text="START",
                   command=lambda: search(email.get(), password.get(), statevar.get(),gender.get(), incomestart.get(), incomeend.get()))
button.place(relx=0.2, rely=0.65, relwidth=0.6, relheight=0.05)

root.mainloop()
