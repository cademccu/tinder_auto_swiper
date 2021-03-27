#! /usr/bin/env python3

import time
import sys
from selenium import webdriver as wd


def get_webdriver():
    print("Fetching webdriver...")
    options = wd.ChromeOptions()
    path_to_chrome = "/home/switchblade/.config/google-chrome"
    options.add_argument("--user-data-dir=" + path_to_chrome)
    driver = wd.Chrome(options=options)
    print("...DONE")
    return driver

def main():
    driver = get_webdriver()
    driver.get("https://tinder.com/app/recs")

    # give a second to load
    time.sleep(2)

    while True:
        like_button = driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]")[0]
        like_button.click()
        print("Liked")
        time.sleep(1)
        try:
            exit_match_button = driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button")[0]
            exit_match_button.click()
            print("\tMATCH")
            time.sleep(.5)
        except:
            print("\tno match...")
        try:
            close_super_like_button = driver.find_elements_by_xpath("/html/body/div[2]/div/div/button[2]")[0]
            close_super_like_button.click()
            time.sleep(.5)
        except:
            print("FUCK YOU SUPER LIKE")
    # close driver 
    driver.close()

if __name__ == "__main__":
    main()
    


# exit out of match button
# /html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button
