#python3

import urllib2
from bs4 import BeautifulSoup
#writing the hashes
import json
#creating the alert
import subprocess
#hasing the pages
from hashlib import md5

#TODO: Make the BS for the media page too and figure out sorting
#maybe just with a third argument 0 = pub, 1 = media
def notifier(url_name, url, site_type):

    if site_type == 0:

        quote_page = url
        page = urllib2.urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')
        page_content = soup.find('div', attrs={'id':'publication-wrapper'})

        #hashes the page
        page_hash = md5(page_content.encode("utf-8")).hexdigest()
        print(page_hash)

    elif site_type == 1:
        quote_page = url
        page = urllib2.urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')
        page_content = soup.find('div', attrs={'class':'view-content'})

        #hashes the page
        page_hash = md5(page_content.encode("utf-8")).hexdigest()
        print(page_hash)

    else:
        print('error in the site_type')

    #loads the json file for reading
    with open('hashes_bs.txt') as json_file:
        hash_json = json.load(json_file)


    #set the old_hash variable based on what's in the json
    old_hash = hash_json[url_name]



    #compares the new has to the old hash
    if page_hash == old_hash:

        print(url_name + " all good")

    else:
        print(url_name + ' change')

        #print a system alert dialog box
        #this only works on mac

        #construct the text to be displayed
        applescript = 'display dialog ' + '"Check' + url_name + '"'

        #display the popup
        subprocess.call("osascript -e '{}'".format(applescript), shell=True)



    #makes the new hash the old hash
    old_hash = page_hash

    #writes the old has to the json

    #opens the json and turns it into a dictionary
    with open('hashes_bs.txt') as json_file:
        json_decoded = json.load(json_file)
    #adds the new pair to the dictionary
    json_decoded[url_name] = old_hash
    #writes the newly expanded json to the file
    with open('hashes_bs.txt', 'w') as json_file:
        json.dump(json_decoded, json_file)

notifier('BartonPubs', 'http://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=30077', 0)
notifier('BartonMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1365', 1)

notifier('RochellePubs', 'http://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=19888', 0)
notifier('RochelleMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1457', 1)

notifier('JeannePubs', 'http://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=27961', 0)
notifier('JeanneMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1406', 1)

notifier('ScottPubs', 'http://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=40904', 0)
notifier('ScottMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1540', 1)

notifier('JasonPubs', 'http://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=36880', 0)
notifier('JasonMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1494', 1)

notifier('ChrisPubs', 'http://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=37891', 0)
notifier('ChrisMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1500', 1)

notifier('KathyPubs', 'https://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=28509', 0)
notifier('KathyMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1418', 1)
