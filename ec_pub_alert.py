#python3

#COMMENT OUT 28 - 49 THE FIRST TIME YOU RUN THIS WITH A NEW PERSON
#IN ORDER TO FILL THE JSON

#downloading the page
import requests
#writing the hashes
import json
#creating the alert
import subprocess
#hasing the pages
from hashlib import md5

def notifier(url_name, url):
    #gets the website
    r = requests.get(url)
    #pulls the text
    page_content = r.text

    #hashes the page
    page_hash = md5(page_content.encode("utf-8")).hexdigest()

    #loads the json file for reading
    with open('hashes.txt') as json_file:
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
    with open('hashes.txt') as json_file:
        json_decoded = json.load(json_file)
    #adds the new pair to the dictionary
    json_decoded[url_name] = old_hash
    #writes the newly expanded json to the file
    with open('hashes.txt', 'w') as json_file:
        json.dump(json_decoded, json_file)

notifier('BartonPubs', 'http://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=30077')
notifier('BartonMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1365')

notifier('RochellePubs', 'http://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=19888')
notifier('RochelleMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1457')

notifier('JeannePubs', 'http://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=27961')
notifier('JeanneMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1406')

notifier('ScottPubs', 'http://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=40904')
notifier('ScottMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1540')

notifier('JasonPubs', 'http://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=36880')
notifier('JasonMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1494')

notifier('ChrisPubs', 'http://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=37891')
notifier('ChrisMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1500')

notifier('KathyPubs', 'https://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=28509')
notifier('KathyMedia', 'https://www.law.nyu.edu/presshighlights?field_fulltime_faculty_target_id=1418')
