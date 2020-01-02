from dotenv import load_dotenv
load_dotenv()

from selenium import webdriver
import time
import os


class SpotifyUpdater:
    def __init__(self):
        self.SPOTIFY_USERNAME = os.environ['SPOTIFY_USERNAME']
        self.SPOTIFY_PASSWORD = os.environ['SPOTIFY_PASSWORD']
        self.SPOTIFY_SONG_URL = os.environ['SPOTIFY_SONG_URI']

    def update_feature_song(self):
        # Fire up a browser
        browser = webdriver.Chrome()
        browser.get('https://accounts.spotify.com/en/login?continue=https:%2F%2Fartists.spotify.com%2F')

        # Log in
        browser.find_element_by_id('login-username').send_keys(self.SPOTIFY_USERNAME)
        browser.find_element_by_id('login-password').send_keys(self.SPOTIFY_PASSWORD)
        browser.find_element_by_xpath("//label[starts-with(@class, 'ng-binding')]").click() # Uncheck "Remember me for next time"
        browser.find_element_by_id('login-button').click()

        # Give the server time to authenticate
        time.sleep(5)

        # Force a redirect and go to Profile
        browser.get('https://artists.spotify.com/c/')
        time.sleep(3)
        browser.get(browser.current_url.replace('home', 'profile'))
        time.sleep(3)

        # Update feature song
        browser.find_element_by_xpath("//*[contains(text(), 'feature music')]").click()
        browser.find_element_by_xpath("//input[starts-with(@class, 'EntityPicker')]").send_keys(self.SPOTIFY_SONG_URL)
        time.sleep(5) # Give the server time to render song selection
        browser.find_element_by_xpath("//div[starts-with(@class, 'ImageWithText')]").click()
        browser.find_element_by_xpath("//label[starts-with(@class, 'Checkbox')]").click()
        browser.find_element_by_xpath("//input[starts-with(@class, 'Comment')]").send_keys("Thank you!")
        browser.find_element_by_xpath("//span[contains(text(), 'Save')]").click()

        # Close browser
        browser.close()
