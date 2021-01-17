import requests
from bs4 import BeautifulSoup
import json
from datetime import date

# Function to check the version within the Discord Bot. 
# Getting the version info with BeautifulSoup from the Starcraft wiki 
def get_version():
    # Load the Starcraft wiki page that contains the info and parsing it with lxml
    source = requests.get('https://starcraft.fandom.com/wiki/StarCraft_II').text
    soup = BeautifulSoup(source,'lxml')
    # Finding the version info within a table (infobox) in the page
    info_table = soup.find('aside', class_='portable-infobox')
    version = info_table.find('a', href='/wiki/StarCraft_II_version_history').text

    # Save the version info within a dict to compare it to the previous saved info
    new_version_info = {
        'version': version,
        'date': str(date.today())
    }

    try:
        # Get the info from the previous check from a json file
        ith open('sc2_version_data.json', 'r') as json_file:
            data = json.load(json_file)
            old_version_info = data['new_version_info']
            # Save the new info within the file
            with open('sc2_version_data.json', 'w') as json_file:
                data = {'old_version_info':old_version_info, 'new_version_info':new_version_info}
                json.dump(data, json_file)
    # In case there is no such file it should be created for the first time
    except Exception as e:
        data = {}
        data['new_version_info'] = new_version_info
        data['old_version_info'] = new_version_info
        with open('sc2_version_data.json', 'w') as json_file:
                json.dump(data, json_file)

    # Return the created dictionary 
    return(data)