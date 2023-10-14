import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


username = "testobj2"
password = "Test123#"


def loginWithFacebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(5)
    # Corrected the button selector
    button_css = "#loginForm > div > div:nth-child(5) > button"
    print("Please provide the username and password")
    click_button_with_css(driver, button_css)
    username1 = input("Username: ")
    password1 = input("Password: ")
    search = driver.find_element(by=By.NAME, value="email")
    search1 = driver.find_element(by=By.NAME, value="pass")
    search.send_keys(username1)
    search1.send_keys(password1)
    search1.send_keys(Keys.RETURN)
    navigate_to_followes(driver)
    time.sleep(2)
    time.sleep(100)


def click_button_with_css(driver, css):
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css))
    )
    button.click()


def navigate_to_followes(driver):
    try:
        not_now_button = 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._a9_1'
        click_button_with_css(driver, not_now_button)
    except:
        pass

    followers_button = "[href*=\"/"+username+"/followers/\"]"
    profile_css = "[href*=\""+username+"\"]"
    following_button = "[href*=\"/"+username+"/following/\"]"

    try:
        button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._a9_1"))
        )
        button.click()
    except Exception as e:
        pass
    click_button_with_css(driver, profile_css)
    time.sleep(2)
    click_button_with_css(driver, followers_button)
    time.sleep(3)
    yep = get_usernames_from_daialog(driver, 1)
    print("Returned form function 1")
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.x1qjc9v5.x78zum5.xdt5ytf > div > div._ac7b._ac7d > div > button"))
    )
    button.click()
    time.sleep(0.5)
    click_button_with_css(driver, following_button)
    time.sleep(0.5)
    yep1 = get_usernames_from_daialog(driver, 2)
    print("People who are  following are .....")
    print(yep)
    print("People who are not following are .....")
    print(yep1.difference(yep))


def get_usernames_from_daialog(driver: webdriver.Chrome, numbe: int):
    users = set()
    # scroll_down(driver)
    body = driver.find_element(by=By.CSS_SELECTOR,  value='body')
    body.click()
    print("Enter the number of followers you want to scrape: ")
    number_of_followers = 5
    temp = 0
    while temp < number_of_followers:
        try:
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
            temp += 1
            print("Scrolling down")
        except Exception as e:
            temp = 101

    print("Please wait, scraping followers\n", end="")

    for i in range(1, number_of_followers+1):
        try:
            if numbe == 1:
                strpassing = str(
                    f"body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1) > div > div:nth-child({i}) > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.x1iyjqo2.xs83m0k.xeuugli.x1qughib.x6s0dn4.x1a02dak.x1q0g3np.xdl72j9 > div > div > div > div > div > a > div > div > span")
                followers = driver.find_elements(By.CSS_SELECTOR, strpassing)
                users.add(followers[0].text)
                print(followers[0].text)
                with open(f'{username}_following.txt', 'r') as file:
                    lines = file.readlines()
                    if followers[0].text + "\n" not in lines:
                        # If not present, append it to the file
                        with open(f'{username}_following.txt', 'a') as append_file:
                            append_file.write(followers[0] + "\n")
            elif numbe == 2:
                strpassing = str("/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div["+str(
                    i)+"]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span")

                followers = driver.find_elements(By.XPATH, strpassing)
                users.add(followers[0].text)
                with open(f'{username}_following.txt', 'a') as file:
                    file.write((followers[0].text) + "\n")
        except Exception as e:
            print(f"[Info] - Saving followers for {username}_followers.txt...")
            break
    return users


def loginWithInstagram():
    print("please wait, logging in ....... ", end="")

    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)
    search = driver.find_element(by=By.NAME, value="username")
    search1 = driver.find_element(by=By.NAME, value="password")
    search.send_keys(username)
    search1.send_keys(password)
    time.sleep(2)
    search1.send_keys(Keys.RETURN)
    navigate_to_followes(driver)
    time.sleep(100)


def __main__():
    print("\n\n")
    print("===========================================")
    print("           Command Prompt Login           ")
    print("===========================================")
    print("Enter the number corresponding to your choice:")
    print("1 - Login using Facebook")
    print("2 - Login using username and password")
    print("===========================================")
    print("\n")
    choice = int(input())
    if choice == 1:
        loginWithFacebook()
    elif choice == 2:
        loginWithInstagram()
    return 0


__main__()
