from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import uuid
import os
import sys
import json
import datetime
from argparse import ArgumentParser



parser = ArgumentParser(prog = 'CDLDownloader', description = 'Downloads PDF results files from ewyniki.cdl.pl site')
parser.add_argument('pesel')
parser.add_argument('barcode')
parser.add_argument('--headless', action = 'store_true')
parser.add_argument('--path', default = os.getcwd())
args = parser.parse_args()

id = str(uuid.uuid1())
directory = os.path.join(args.path, id)

options = Options()
if (args.headless):
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("prefs", {"download.default_directory": directory,
                                             'download.prompt_for_download': False,
                                             'plugins.always_open_pdf_externally': True})

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://ewyniki.cdl.pl/kl322-n/index.php?page=logowanie&barcodeLogin=true")


def click(element):
    driver.execute_script("arguments[0].click();", element)



barcode_textbox = driver.find_element(By.NAME, "barcode")
pesel_textbox = driver.find_element(By.NAME, "pesel")
submit_button = driver.find_element(By.CLASS_NAME, "loginButton")

barcode_textbox.send_keys(args.barcode)
pesel_textbox.send_keys(args.pesel)
click(submit_button)

while True:
    try:
        if driver.find_element(By.CLASS_NAME, "error").is_displayed():
            print(json.dumps({
                "success": False,
            }))
            sys.exit()
    except NoSuchElementException:
        pass
    try:
        if driver.find_element(By.CLASS_NAME, "fa-cloud-download").is_displayed():
            break
    except NoSuchElementException:
        pass
    time.sleep(1)

click(driver.find_element(By.CLASS_NAME, "fa-cloud-download"))

result_table_html = None
try:
    if driver.find_element(By.CLASS_NAME, "resultTable").is_displayed():
        result_table_html = driver.find_element(By.CLASS_NAME, "resultTable").get_attribute('outerHTML')
except:
    pass

date_text = driver.find_element(By.CLASS_NAME, "kiedy")
date = date_text.get_attribute('innerHTML')[:-6]

show_document_button = driver.find_element(By.CLASS_NAME, "dokument")
document_href = show_document_button.get_attribute('href')

os.system("mkdir " + directory)

driver.get(document_href)

while True:
    if len(os.listdir(directory)) == 1 and os.listdir(directory)[0].endswith('.pdf'):
        break
    time.sleep(1)

file_path = os.listdir(directory)[0]

print(json.dumps({
    "success": True,
    "id": id,
    "fileName": file_path,
    "formattedDate": datetime.datetime.strptime(date, "%d-%m-%Y").strftime("%Y.%m.%d"),
    "resultTableHTML": result_table_html,
}))
sys.exit()