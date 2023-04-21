from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from concurrent import futures
from selenium_recaptcha_solver import RecaptchaSolver
import random
# Set up the driver




def do_stuff(i):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    # Create a new instance of the Chrome driver with custom options
 
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    
    driver = webdriver.Chrome('./chromedriver',options=options)
    driver.delete_all_cookies()
    solver = RecaptchaSolver(driver=driver)

    driver.get('chrome://settings/clearBrowserData')
    driver.find_element('xpath','//settings-ui').send_keys(Keys.ENTER)
    # Navigate to the website
    driver.get("https://portal.311.nyc.gov/article/?kanumber=KA-01074")
    time.sleep(3)
    nextlink1 = driver.find_element('xpath','/html/body/form/div[5]/div/div[2]/div[1]/div/div/div[4]/div[1]/h4/button').click()
    time.sleep(2)
    nextlink2 = driver.find_element('xpath','/html/body/form/div[5]/div/div[2]/div[1]/div/div/div[4]/div[2]/div/div[2]/h5/a').click()

    # Wait for the page to load
    time.sleep(2)
    address_select_button = driver.find_element('xpath','/html/body/form/div[5]/div[1]/div[4]/div[6]/div/div[1]/div[2]/div/div/fieldset[11]/table/tbody/tr[2]/td[1]/div[2]/div[4]/div/button')
    anon_radio = driver.find_element('xpath','/html/body/form/div[5]/div[1]/div[4]/div[6]/div/div[1]/div[2]/div/div/fieldset[2]/table/tbody/tr/td[1]/div[2]/span/input[2]').click()
    address_select_button.click()
    time.sleep(2)


    address_text_input = driver.find_element('xpath','/html/body/form/div[5]/div[1]/div[4]/div[6]/div/div[2]/section[1]/div/div/div[2]/div[1]/div[1]/input')
    try:
        address_text_input.send_keys('510 MAIN STREET, NEW YORK')
        time.sleep(2)
        address_text_input.send_keys(Keys.DOWN)
        time.sleep(2)
        address_text_input.send_keys(Keys.ENTER)
    except Exception as e:
        pass
    address_submit_button = driver.find_element('xpath','/html/body/form/div[5]/div[1]/div[4]/div[6]/div/div[2]/section[1]/div/div/div[2]/div[4]/input[1]')
    address_submit_button.click()
    time.sleep(2)
    next1 = driver.find_element('xpath','/html/body/form/div[5]/div[1]/div[4]/div[6]/div/div[2]/div[1]/div/input[2]').click()
    time.sleep(2)
    # find the select element
    select_element1 = driver.find_element('id',"n311_problemid_select")
    select_object1 = Select(select_element1)
    select_object1.select_by_visible_text("Heat/Hot Water")
    time.sleep(1)
    select_element2 = driver.find_element('id',"n311_problemdetailid_select")
    select_object2 = Select(select_element2)
    select_object2.select_by_visible_text("Entire Building")
    time.sleep(1)

    select_element3 = driver.find_element('id',"n311_additionaldetailsid_select")
    select_object3 = Select(select_element3)
    select_object3.select_by_visible_text("No Hot Water")
    time.sleep(1)

    select_element4 = driver.find_element('id',"n311_locationdetailid_select")
    select_object4 = Select(select_element4)
    select_object4.select_by_visible_text("Building-Wide")
    time.sleep(1)

    select_element5 = driver.find_element('id',"n311_whattimeofthedayoptionset")
    select_object5 = Select(select_element5)
    select_object5.select_by_visible_text("All the time")


    next2 = driver.find_element('xpath','/html/body/form/div[5]/div[1]/div[4]/div/div/div[2]/input[2]').click()

    time.sleep(2)
    phone= driver.find_element('xpath','/html/body/form/div[5]/div[1]/div[5]/div[3]/div[1]/div/div/div[1]/div[2]/div/div/fieldset[10]/table/tbody/tr[3]/td[1]/div[2]/input').send_keys('2123483248')
    time.sleep(1)

    next3 = driver.find_element('xpath','/html/body/form/div[5]/div[1]/div[5]/div[3]/div[1]/div/div/div[2]/div[1]/div/input[3]').click()
    time.sleep(5)
    recaptcha_iframe = driver.find_element('xpath', '//iframe[@title="reCAPTCHA"]')
    try:
        solver.click_recaptcha_v2(iframe=recaptcha_iframe)
    except Exception:
        pass
    time.sleep(3)
    final = driver.find_element('xpath','/html/body/form/div[5]/div[1]/div[5]/div/div/div[2]/div/div/input[2]').click()
    time.sleep(5)

# default number of threads is optimized for cpu cores 
# but you can set with `max_workers` like `futures.ThreadPoolExecutor(max_workers=...)`

for i in range(1):
    with futures.ThreadPoolExecutor() as executor: 
        future_test_results = [ executor.submit(do_stuff, i)  
            for i in range(5) ] # running same test 6 times, using test number as url
    for future_test_result in future_test_results: 
        try:        
            test_result = future_test_result.result() # can use `timeout` to wait max seconds for each thread               
            #... do something with the test_result
        except Exception as exc: # can give a exception in some thread, but 
            print(f'thread generated an exception: {exc}')