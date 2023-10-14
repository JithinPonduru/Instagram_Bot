---

# Instagram Follower Analyzer

## Overview

The Instagram Follower Analyzer is a Python script designed to help you analyze your Instagram followers and identify who is not following you back. This tool leverages Selenium and ChromeDriver to automate the process of logging into your Instagram account and scraping the list of your followers. This README will guide you through the setup, usage, and considerations while using this script.

## Prerequisites

Before you begin using the Instagram Follower Analyzer, ensure that you have the following prerequisites installed on your system:

1. **Python 3:** This script is written in Python, so you need to have Python 3 installed on your computer. If you don't have it, you can download and install it from the [official Python website](https://www.python.org/).

2. **Selenium Library:** The script uses the Selenium library to automate web interactions. You can install Selenium using pip with the following command:

   ```shell
   pip install selenium
   ```

3. **ChromeDriver:** ChromeDriver is a WebDriver for the Chrome web browser. The script manages this requirement using the `webdriver_manager`, so you don't need to download it separately.

4. **Instagram Account:** You should have an active Instagram account with your username and password. The script will use these credentials to log in.

5. **Chrome Web Browser:** Make sure you have the Google Chrome web browser installed on your system. The script is designed to work with Chrome.[Chromedriver Download](https://chromedriver.chromium.org/downloads).

## Usage

Follow these steps to effectively use the Instagram Follower Analyzer:

### Step 1: Open the Script

- Open the Python script (typically with a `.py` file extension) in a text editor or integrated development environment (IDE) of your choice. You can edit the script with any plain text editor, such as Notepad or Visual Studio Code.

### Step 2: Update Account Information

- In the script, locate the following lines and update them with your Instagram account credentials:

   ```python
   username = "your_username"
   password = "your_password"
   ```

   Replace `"your_username"` with your Instagram username and `"your_password"` with your Instagram password
   ( Username = "testobj2" and password = "Test123#" are pre-set ).
  
### Step 3: Run the Script

- After updating your account information, save the script.

- Run the script using Python. To do this, open your command line or terminal, navigate to the directory where the script is located, and execute the following command:

   ```shell
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the actual name of the script file.

### Step 4: Choose Login Method

- Upon running the script, you will be prompted to choose a login method:

   1. **Login using Facebook:** Select option 1 if you prefer to log in using your Facebook account associated with Instagram.
   2. **Login using username and password:** Select option 2 if you wish to log in using your Instagram account's username and password.

### Step 5: Script Execution

- The script will then proceed to automate the following tasks:

   - Logging in to Instagram.
   - Navigating to your profile
   - Navigating to your list of followers.
   - Scrolling to load the number of followers you specify (the default is 5, but you may modify)
   - Scraping the list of your followers.

- The script may take some time to complete these tasks, depending on the number of followers you have.

### Step 6: Review Results

- After the script has finished running, it will present you with two lists of followers:

   - Followers who are currently following you.
   - Followers who are not following you back.

- Additionally, the script will save the list of followers who are following you in a file named `your_username_following.txt`.

**Note:** Keep in mind that the script may require manual updates if Instagram's website structure changes. It is developed for educational purposes and should be used responsibly and within Instagram's terms of service.

## Disclaimer

This Instagram Follower Analyzer script utilizes web scraping techniques to interact with Instagram's website. Such interactions may be subject to Instagram's terms of service and policies. Therefore, it is important to use this tool responsibly, respecting other users' privacy and Instagram's guidelines.

- **Responsible Use:** Please use this script responsibly and avoid excessive use or any actions that might violate Instagram's policies. Automating interactions with Instagram may result in temporary or permanent restrictions on your account.

Make sure there is a 5 to 10-minute interval before using this tool again to avoid Instagram assuming you are a spammer and blocking your account. 

Enjoy using the Instagram Follower Analyzer and gain a better understanding of python selenium and webscraping 
---

#### This expanded README file provides users with comprehensive instructions and guidance on using the Instagram Follower Analyzer script while emphasizing responsible usage and respect for Instagram's policies.
