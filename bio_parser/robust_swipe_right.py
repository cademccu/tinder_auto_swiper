#! /usr/bin/env python3

import time
import sys
import tinder_constants as tc
from selenium import webdriver as wd

# prints the usage messages
def print_help():
    print("-------------------------------------------------------")
    print("This program opens up an instance of chrome and runs Tinder. You need to\n" +
            "specify the path to your default google profile in the tinder_constants.py file\n" +
            "to get chrome to open up with tinder already logged in, since tinder uses 2-step\n" +
            "authentication, getting the codes from your texts and emails would be unnecessary\n" +
            "when you could just use your chrome profile.\n")
    print("[USAGE]")
    print("-n | --number-of-swipes     <INT>        A set number of swipes to run before exiting. Defaults to running until process stopper by user.")
    print("-f | --filename             <STRING>     The name of the CSV file with the words to swipe left on. Defaults to \"bad_words.csv\".")
    print("-h                                       This documentation.")
    print("-------------------------------------------------------\n")

# get the arguments from the command line
# kinda hackey but i don't like argparse and this is MY
# program so whatever
def get_args():
    defaults = { "filename" : "bad_words.csv",
            "number-of-swipes" : -1}
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-h" or sys.argv[i] == "--help":
            print_help()
            sys.exit(0)
        elif sys.argv[i] == "-f" or sys.argv[i] == "--filename":
            i += 1
            defaults["filename"] = sys.argv[i]
        elif sys.argv[i] == "-n" or sys.argv[i] == "--number-of-swipes":
            i += 1
            defaults["number-of-swipes"] = sys.argv[i]
        else:
            print("UNKNOWN ARGUMENT [", sys.argv[i], "] SEE USAGE:\n")
            print("\n")
            print_help()
            sys.exit()

        i += 1
    return defaults

# fetches the chrome webdriver 
def get_webdriver():
    print("Fetching webdriver...")
    options = wd.ChromeOptions()
    path_to_chrome = "/home/switchblade/.config/google-chrome"
    options.add_argument("--user-data-dir=" + path_to_chrome)
    try:
        driver = wd.Chrome(options=options)
        print("...DONE")
        return driver
    except:
        print("The default isntance of chrome specified in tinder_constants.py is already in use\n" +
                "Closing all instances of chrome may solve this problem.\n")
        sys.exit(-1)

def main():
    args = get_args()

    driver = get_webdriver()

    driver.get("https://tinder.com/app/recs")

    # give a second to load
    time.sleep(2)

    while True:
        like_button = driver.find_elements_by_xpath(tc.like_button)[0]
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
