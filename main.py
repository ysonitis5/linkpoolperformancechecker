from cffi.cffi_opcode import CLASS_NAME
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import tweepy
import re
import pandas as pd
import statistics
import pyautogui

data = []
data_two = []
data_three = []
data_four = []
final_answer = 0

def page_one():
  global data
  # Set up a webdriver instance using the Chrome browser
  driver = webdriver.Chrome()

  # Navigate to the staking page
  driver.get('https://staking.chain.link/')

  # Wait for the page to load
  time.sleep(15)

  # Get the fully rendered HTML of the page
  html = driver.page_source

  # Parse the HTML of the staking page
  soup = BeautifulSoup(html, 'html.parser')

  # Find the table element containing the data you want to extract
  table_element = soup.find('table')

  # Check if the table element was found
  if table_element is not None:
    # Extract the data from the table element
    rows = table_element.find_all('tr')
    for row in rows:
      cols = row.find_all('td')
      cols = [ele.text.strip() for ele in cols]
      data.append([ele for ele in cols if ele]) # Get rid of empty values

  # Print the extracted data
  # print(data)

  # Close the webdriver instance
  driver.close()

def page_two():
  global data_two
  # Set up a webdriver instance using the Chrome browser
  driver = webdriver.Chrome()

  # Navigate to the staking page
  driver.get('https://staking.chain.link/')

  # Wait for the page to load
  time.sleep(5)

  # Find all elements matching the XPath expression for the "Next" button
  next_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[3]/div[3]/button[2]')

  # Click
  next_button.click()

  # Wait for the page to load
  time.sleep(5)

  # Get the fully rendered HTML of the page
  html = driver.page_source

  # Parse the HTML of the staking page
  soup = BeautifulSoup(html, 'html.parser')

  # Find the table element containing the data you want to extract
  table_element = soup.find('table')

  # Check if the table element was found
  if table_element is not None:
    # Extract the data from the table element
    rows = table_element.find_all('tr')
    for row in rows:
      cols = row.find_all('td')
      cols = [ele.text.strip() for ele in cols]
      data_two.append([ele for ele in cols if ele])  # Get rid of empty values

  # Print the extracted data
  # print(data_two)

  # Close the webdriver instance
  driver.close()

def page_three():
  global data_three
  # Set up a webdriver instance using the Chrome browser
  driver = webdriver.Chrome()

  # Navigate to the staking page
  driver.get('https://staking.chain.link/')

  # Wait for the page to load
  time.sleep(5)

  # Find all elements matching the XPath expression for the "Next" button
  next_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[3]/div[3]/button[2]')

  # Click
  next_button.click()

  # Wait for the page to load
  time.sleep(5)

  # Find all elements matching the XPath expression for the "Next" button
  next_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[3]/div[3]/button[2]')

  # Click
  next_button.click()

  # Wait for the page to load
  time.sleep(5)

  # Get the fully rendered HTML of the page
  html = driver.page_source

  # Parse the HTML of the staking page
  soup = BeautifulSoup(html, 'html.parser')

  # Find the table element containing the data you want to extract
  table_element = soup.find('table')

  # Check if the table element was found
  if table_element is not None:
    # Extract the data from the table element
    rows = table_element.find_all('tr')
    for row in rows:
      cols = row.find_all('td')
      cols = [ele.text.strip() for ele in cols]
      data_three.append([ele for ele in cols if ele])  # Get rid of empty values

  # Print the extracted data
  # print(data_three)

  # Close the webdriver instance
  driver.close()

def page_four():
  global data_four
  # Set up a webdriver instance using the Chrome browser
  driver = webdriver.Chrome()

  # Navigate to the staking page
  driver.get('https://staking.chain.link/')

  # Wait for the page to load
  time.sleep(5)

  # Find all elements matching the XPath expression for the "Next" button
  next_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[3]/div[3]/button[2]')

  # Click
  next_button.click()

  # Wait for the page to load
  time.sleep(5)

  # Find all elements matching the XPath expression for the "Next" button
  next_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[3]/div[3]/button[2]')

  # Click
  next_button.click()

  # Wait for the page to load
  time.sleep(5)

  # Find all elements matching the XPath expression for the "Next" button
  next_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[3]/div[3]/button[2]')

  # Click
  next_button.click()

  # Wait for the page to load
  time.sleep(5)

  # Get the fully rendered HTML of the page
  html = driver.page_source

  # Parse the HTML of the staking page
  soup = BeautifulSoup(html, 'html.parser')

  # Find the table element containing the data you want to extract
  table_element = soup.find('table')

  # Check if the table element was found
  if table_element is not None:
    # Extract the data from the table element
    rows = table_element.find_all('tr')
    for row in rows:
      cols = row.find_all('td')
      cols = [ele.text.strip() for ele in cols]
      data_four.append([ele for ele in cols if ele])  # Get rid of empty values

  # Print the extracted data
  # print(data_four)

  # Close the webdriver instance
  driver.close()

def get_trusted():
  global final_answer
  # Set up a webdriver instance using the Chrome browser
  driver = webdriver.Chrome()

  # Navigate to the staking page
  driver.get('https://staking.chain.link/')

  # Wait for the page to load
  time.sleep(15)

  # Find all elements matching the XPath expression for the "Next" button
  next_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[3]/div[3]/button[2]')

  # Click
  next_button.click()

  # Wait for the page to load
  time.sleep(15)

  # Get the fully rendered HTML of the page
  html = driver.page_source

  # Parse the HTML of the staking page and extract the trusted answers
  soup = BeautifulSoup(html, 'html.parser')

  answers = {
    'trusted': '',
    'linkpools': ''
  }

  # Find the body element
  body_element = soup.find('body')

  # Check if the body element was found
  if body_element is not None:
    # Find the div element with the data-reactroot attribute
    div_element = body_element.find('div', attrs={'data-reactroot': ''})

    # Check if the div element was found
    if div_element is not None:
      # Find the main element with the stakingLayout_container__WzwO_ class
      main_element = div_element.find('main', class_='stakingLayout_container__WzwO_')

      # Check if the main element was found
      if main_element is not None:
        # Find the div element with the homeView_container__8zV5Z class
        home_view_element = main_element.find('div', class_='homeView_container__8zV5Z')

        # Check if the home_view element was found
        if home_view_element is not None:
          # Find the div element with the dataFeed
          data_feed_element = main_element.find('div', class_='dataFeedsSecured_container__SEadr card_container__XeKX6')
          if data_feed_element is not None:
            # Find the div element with feed_data__cGKC_
            feed_data_element = main_element.find('div', class_='feed_data__cGKC_')
            if feed_data_element is not None:
              trusted_answer = feed_data_element.find('h4')
              final_answero = trusted_answer.getText().strip()
              final_answer = final_answero.strip('$')


def main():
  global linkpool_in_top_5
  global final_answer
  # Replace these with your own API keys and tokens
  consumer_key = "..."
  consumer_secret = "..."
  access_token = "..."
  access_token_secret = "..."

  # Set up the OAuth1 authentication
  auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  # Create the API client
  api = tweepy.API(auth)

  # Set up a webdriver instance using the Chrome browser
  driver = webdriver.Chrome()

  # Navigate to the staking page
  driver.get('https://staking.chain.link/')

  # Wait for the page to load
  time.sleep(15)

  # Find all elements matching the XPath expression for the "Next" button
  next_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[3]/div[3]/button[2]')

  # Click
  next_button.click()


  # Wait for the page to load
  time.sleep(15)

  # Get the fully rendered HTML of the page
  html = driver.page_source

  # Parse the HTML of the staking page and extract the trusted answers
  soup = BeautifulSoup(html, 'html.parser')

  answers = {
    'trusted': '',
    'linkpools': ''
  }

  # Find the body element
  body_element = soup.find('body')

  # Check if the body element was found
  if body_element is not None:
    # Find the div element with the data-reactroot attribute
    div_element = body_element.find('div', attrs={'data-reactroot': ''})

    # Check if the div element was found
    if div_element is not None:
      # Find the main element with the stakingLayout_container__WzwO_ class
      main_element = div_element.find('main', class_='stakingLayout_container__WzwO_')

      # Check if the main element was found
      if main_element is not None:
        # Find the div element with the homeView_container__8zV5Z class
        home_view_element = main_element.find('div', class_='homeView_container__8zV5Z')

        # Check if the home_view element was found
        if home_view_element is not None:
          # Find the div element with the dataFeed
          data_feed_element = main_element.find('div', class_='dataFeedsSecured_container__SEadr card_container__XeKX6')
          if data_feed_element is not None:
            #Find the div element with feed_data__cGKC_
            feed_data_element = main_element.find('div', class_='feed_data__cGKC_')
            if feed_data_element is not None:
              trusted_answer = feed_data_element.find('h4')
              final_answero = trusted_answer.getText().strip()
              final_answer = final_answero.strip('$')
              answers.update({'trusted': final_answer})

  # Find the body element
  second_body_element = soup.find('body')

  # Check if the body element was found
  if second_body_element is not None:
    # Find the div element with the data-reactroot attribute
    div_element = second_body_element.find('div', attrs={'data-reactroot': ''})

    # Check if the div element was found
    if div_element is not None:
      # Find the main element with the stakingLayout_container__WzwO_ class
      main_element = div_element.find('main', class_='stakingLayout_container__WzwO_')

      # Check if the main element was found
      if main_element is not None:
        # Find the div element with the homeView_container__8zV5Z class
        home_view_element = main_element.find('div', class_='homeView_container__8zV5Z')

        # Check if the home_view_element element was found
        if home_view_element is not None:
          # Find the div element with the dataFeedsSecured_container__SEadr class
          data_feeds_secured_element = home_view_element.find('div', class_='dataFeedsSecured_container__SEadr')

          # Check if the data_feeds_secured_element element was found
          if data_feeds_secured_element is not None:
            # Find the div element with the nodeOperators_container__op_sL class
            node_operators_element = data_feeds_secured_element.find('div', class_='nodeOperators_container__op_sL')

            # Check if the node_operators_element element was found
            if node_operators_element is not None:
              # Find the table element
              table_element = node_operators_element.find('table')

              # Check if the table_element element was found
              if table_element is not None:
                # Extract the table element into a list of dictionaries
                table_data = []

                # Find the thead element
                thead_element = table_element.find('thead')

                # Extract the column names from the th elements
                column_names = [th.get_text().strip() for th in thead_element.find_all('th')]

                # Find the tbody element
                tbody_element = table_element.find('tbody')

                # Iterate over the tr elements
                for tr_element in tbody_element.find_all('tr'):
                  # Extract the data from the td elements
                  data = [td.get_text().strip() for td in tr_element.find_all('td')]

                  # Create a dictionary with the column names as the keys and the data as the values
                  row_data = dict(zip(column_names, data))

                  # Append the dictionary to the list
                  table_data.append(row_data)

                # Print the table data
                linkpool = table_data[4]
                print(linkpool)
                linkpools_answer = linkpool['Latest answer']
                print(linkpools_answer)
                linkpools_time = linkpool['Date']
                print(linkpools_time)
                final_linkpool = linkpools_answer.strip('$')
                print(final_linkpool)
                final_answer = answers['trusted']
                print(final_answer)
                answers.update({'linkpools': final_linkpool})
                global streak
                global highscore
                global trusted
                global total
                global toppers
                global total_bypasser
                global percentage
                global numba_one
                                if answers['trusted'] != answers['linkpools']:
                  streak += 1
                  # Remove the commas from the values
                  trusted_value = float(answers['trusted'].replace(',', ''))
                  linkpools_value = float(answers['linkpools'].replace(',', ''))

                  # Calculate the absolute difference between the two values
                  difference = abs(trusted_value - linkpools_value)
                  formatted_difference = "{:.2f}".format(difference)

                  if total % 10 == 0:
                    if linkpool_in_top_1 == True:
                      if difference > highscore:
                        total += 1
                        toppers += 1
                        numba_one += 1
                        percentage = (toppers / total) * 100
                        percentage = "{:.2f}".format(percentage)
                        total_bypasser = total
                        message = f'The trusted answer for the ETH/USD feed is ${final_answer} and Linkpool provided ${final_linkpool}. \n \nThey were off by ${formatted_difference}. This is a new highscore! Previous: ${highscore}\n \n{numba_one} answers have bene the furthest answer from the truth.'
                        message_two = f'The worst variance has been ${highscore}.\n \nThey have submitted {trusted} trusted answers out of {total} attempts this session. They are submitting faulty answers at a rate of {percentage}%.\n \nThey have submitted {streak} variant answers consecutively.'
                        api.update_status(message)
                        api.update_status(message_two)
                        highscore = difference
                        total = 0
                      if difference < highscore:
                        total += 1
                        toppers += 1
                        numba_one += 1
                        percentage = (toppers / total) * 100
                        percentage = "{:.2f}".format(percentage)
                        total_bypasser = total
                        message = f'The trusted answer for the ETH/USD feed is ${final_answer} and Linkpool provided ${final_linkpool}. \n \nThey were off by ${formatted_difference}.\n \n{numba_one} answers have been the furthest answer from the truth.'
                        message_two = f'The worst variance has been ${highscore}.\n \nThey have submitted {trusted} trusted answers out of {total} attempts this session. They are submitting faulty answers at a rate of {percentage}%.\n \nThey have submitted {streak} variant answers consecutively.'
                        api.update_status(message)
                        api.update_status(message_two)
                        total = 0
                    elif linkpool_in_top_5 == True:
                      if difference > highscore:
                        total += 1
                        toppers += 1
                        percentage = (toppers / total) * 100
                        percentage = "{:.2f}".format(percentage)
                        total_bypasser = total
                        message = f'The trusted answer for the ETH/USD feed is ${final_answer} and Linkpool provided ${final_linkpool}. \n \nThey were off by ${formatted_difference}. This is a new highscore! Previous: ${highscore}\n \nThey were among the top 5 most variant Oracles for this update.'
                        message_two = f'The worst variance has been ${highscore}.\n \nThey have submitted {trusted} trusted answers out of {total} attempts this session. They are submitting faulty answers at a rate of {percentage}%.\n \nThey have submitted {streak} variant answers consecutively.'
                        api.update_status(message)
                        api.update_status(message_two)
                        highscore = difference
                        total = 0
                      if difference < highscore:
                        total += 1
                        toppers += 1
                        percentage = (toppers / total) * 100
                        percentage = "{:.2f}".format(percentage)
                        total_bypasser = total
                        message = f'The trusted answer for the ETH/USD feed is ${final_answer} and Linkpool provided ${final_linkpool}. \n \nThey were off by ${formatted_difference}.\n \nThey were among the top 5 most variant Oracles for this update.'
                        message_two = f'The worst variance has been ${highscore}.\n \nThey have submitted {trusted} trusted answers out of {total} attempts this session. They are submitting faulty answers at a rate of {percentage}%.\n \nThey have submitted {streak} variant answers consecutively.'
                        api.update_status(message)
                        api.update_status(message_two)
                        total = 0
                    elif answers['trusted'] == answers['linkpools']:
                      streak = 0
                      trusted += 1
                      total += 1
                      total_bypasser = total
                      print(f'we have had a rare occurence at {linkpools_time}')
                    else:
                      if difference > highscore:
                        total += 1
                        percentage = (toppers / total) * 100
                        percentage = "{:.2f}".format(percentage)
                        total_bypasser = total
                        message = f'The trusted answer for the ETH/USD feed is ${final_answer} and Linkpool provided ${final_linkpool}. \n \nThey were off by ${formatted_difference}. This is a new highscore! Previous: ${highscore}.\n \nThey were not among the top 5 most variant Oracles for this update.'
                        message_two = f'The worst variance has been ${highscore}.\n \nThey have submitted {trusted} trusted answers out of {total} attempts this session. They are submitting faulty answers at a rate of {percentage}%.\n \nThey have submitted {streak} variant answers consecutively.'
                        api.update_status(message)
                        api.update_status(message_two)
                        highscore = difference
                        total = 0
                      if difference < highscore:
                        total += 1
                        percentage = (toppers / total) * 100
                        percentage = "{:.2f}".format(percentage)
                        total_bypasser = total
                        message = f'The trusted answer for the ETH/USD feed is ${final_answer} and Linkpool provided ${final_linkpool}. \nThey were off by ${formatted_difference}.\nThey were not among the top 5 most variant Oracles for this update.'
                        message_two = f'The worst variance has been ${highscore}.\n \nThey have submitted {trusted} trusted answers out of {total} attempts this session. They are submitting faulty answers at a rate of {percentage}%.\n \nThey have submitted {streak} variant answers consecutively.'
                        api.update_status(message)
                        api.update_status(message_two)
                        total = 0
                  if total % 10 != 0:
                    if linkpool_in_top_1 == True:
                      if difference > highscore:
                        total += 1
                        toppers += 1
                        numba_one += 1
                        total_bypasser = total
                        message = f'The trusted answer for the ETH/USD feed is ${final_answer} and Linkpool provided ${final_linkpool}. \n \nThey were off by ${formatted_difference}. This is a new highscore! Previous: ${highscore}\n \nThis was the furthest answer from the truth.'
                        api.update_status(message)
                        highscore = difference
                      if difference < highscore:
                        total += 1
                        toppers += 1
                        numba_one += 1
                        total_bypasser = total
                        message = f'The trusted answer for the ETH/USD feed is ${final_answer} and Linkpool provided ${final_linkpool}. \n \nThey were off by ${formatted_difference}.\n \nThey have submitted {streak} variant answers consecutively.\n \nThis was the furthest answer from the truth.'
                        api.update_status(message)
                    elif linkpool_in_top_5 == True:
                      if difference > highscore:
                        total += 1
                        toppers += 1
                        total_bypasser = total
                        message = f'The trusted answer for the ETH/USD feed is ${final_answer} and Linkpool provided ${final_linkpool}. \n \nThey were off by ${formatted_difference}. This is a new highscore! Previous: ${highscore}\n \nThey were among the top 5 most variant Oracles for this update.'
                        api.update_status(message)
                        highscore = difference
                      if difference < highscore:
                        total += 1
                        toppers += 1
                        total_bypasser = total
                        message = f'The trusted answer for the ETH/USD feed is ${final_answer} and Linkpool provided ${final_linkpool}. \n \nThey were off by ${formatted_difference}.\n \nThey have submitted {streak} variant answers consecutively.\n \nThey were among the top 5 most variant Oracles for this update.'
                        api.update_status(message)
                    elif answers['trusted'] == answers['linkpools']:
                      streak = 0
                      trusted += 1
                      total += 1
                      total_bypasser = total
                      print(f'we have had a rare occurence at {linkpools_time}')
                    else:
                      if difference > highscore:
                        total += 1
                        total_bypasser = total
                        message = f'The trusted answer for the ETH/USD feed is ${final_answer} and Linkpool provided ${final_linkpool}. \n \nThey were off by ${formatted_difference}. This is a new highscore! Previous: ${highscore}.\n \nThey were not among the top 5 most variant Oracles for this update.'
                        api.update_status(message)
                        highscore = difference
                      if difference < highscore:
                        total += 1
                        total_bypasser = total
                        message = f'The trusted answer for the ETH/USD feed is ${final_answer} and Linkpool provided ${final_linkpool}. \n \nThey were off by ${formatted_difference}.  \n \nThey were not among the top 5 most variant Oracles for this update.'
                        api.update_status(message)

def create_df(data, data_two, data_three, data_four):
  global running_df
  # Create a dataframe from the first list
  df1 = pd.DataFrame(data)

  # Create a dataframe from the second list
  df2 = pd.DataFrame(data_two)

  # Create a dataframe from the third list
  df3 = pd.DataFrame(data_three)

  # Create a dataframe from the fourth list
  df4 = pd.DataFrame(data_four)

  # Combine the dataframes using the concat function
  df = pd.concat([df1, df2, df3, df4])

  running_df = df.dropna(how='all')

# Function to send tweets out just need to input tweet as message variable in call to function
def send_tweet(message):
  consumer_key = "..."
  consumer_secret = "..."
  access_token = "..."
  access_token_secret = "..."

  # Set up the OAuth1 authentication
  auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  # Create the API client
  api = tweepy.API(auth)
  api.update_status(message)


# Function to send direct message to list of users
def send_dm(message):
  consumer_key = "..."
  consumer_secret = "..."
  access_token = "..."
  access_token_secret = "..."

  # Set up the OAuth1 authentication
  auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  # Create the API client
  api = tweepy.API(auth)

  # A list of user screen names to send the message to
  users = ['user1', 'user2', 'user3']

  # Send the message to each user
  for user in users:
    api.send_direct_message(user, message)


jango = True

streak = 0
highscore = 11.42
trusted = 0
toppers = 0
total = 0
total_bypasser = 0
percentage = 0
numba_one = 0

while jango == True:
  running_df = []
  data = []
  data_two = []
  data_three = []
  data_four = []
  print(running_df)
  get_trusted()
  page_one()
  page_two()
  page_three()
  page_four()

  create_df(data,data_two,data_three,data_four)



  # Define a function that takes a row of the DataFrame and returns the variance
  # between the value in column 2 and the trusted value
  def calculate_variance(row, trusted_value):
    value = row[1]
    # Remove the "$" and "," characters from the value string
    value = re.sub(r'[$,]', '', value)
    trusted_value = re.sub(r'[$,]', '', trusted_value)
    # Convert the value string to a float
    value = float(value)
    trusted_value = float(trusted_value)
    # Calculate the absolute difference between the trusted value and the value
    variance = abs(trusted_value - value)
    # Return the variance as a float
    return variance


  # Add a new column to the DataFrame called "Variance" and fill it with the
  # variance values calculated by the calculate_variance function
  running_df.rename(columns={0: 'Oracle Name'}, inplace=True)
  running_df['Variance'] = running_df.apply(lambda row: calculate_variance(row, final_answer), axis=1)

  # Sort the DataFrame by the Variance column in descending order
  running_df.sort_values(by='Variance', ascending=False, inplace=True)

  # Get the top 5 rows of the DataFrame
  top_5 = running_df.head(5)
  top_10 = running_df.head(10)
  top_1 = running_df.head(1)
  print(top_10)
  # Print the Oracle Name and Variance for each of the top 5 rows
  for index, row in top_5.iterrows():
    print(row['Oracle Name'], row['Variance'])

  # Check if Linkpool is in the top 5
  linkpool_in_top_5 = 'LinkPool' in top_5['Oracle Name'].values
  linkpool_in_top_1 = 'LinkPool' in top_1['Oracle Name'].values
  print(f'top 5 = {linkpool_in_top_5}')
  print(f'top 1 = {linkpool_in_top_1}')

  # Rename column 3 to "Response"
  running_df.rename(columns={3: "Response"}, inplace=True)

  # Check if any rows in the "Response" column do not contain "Responded"
  non_responding_oracles = running_df[running_df['Response'] != 'Responded']

  # Print the result
  if non_responding_oracles.empty:
    print('All oracles responded')
  else:
    print(f'The following oracles did not respond: {non_responding_oracles["Oracle Name"].tolist()}')

  total = total_bypasser
  main()
  running_df = []
  time.sleep(3600)
else:
  print('failed')

