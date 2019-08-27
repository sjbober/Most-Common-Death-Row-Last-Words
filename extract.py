import sqlite3
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#creates a DB called "executions" and connects to it. This is where we will store execution data and the final statement
conn = sqlite3.connect('executions.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Executions
    (id INTEGER PRIMARY KEY UNIQUE, inmate_id INTEGER UNIQUE, date TEXT, county TEXT, statement TEXT)
''')

url = 'https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html' #URL for Texas Department of Criminal Justice death row information
document = urlopen(url, context=ctx) ##opens the Texas DCJ url and connects to it
html = document.read()

#after examining the site's HTML structure using Developer Tools, the best way to extract the information I need is to use BeautifulSoup to parse and extract the table cell tags
soup = BeautifulSoup(html, "html.parser")
tags_td = soup('td')

#goes through td tags and pulls out the execution information and statement link
for i in range(len(tags_td)):
    if str(i).endswith("0"):
        #the iterations that end in 0 are the unique execution numbers
        exnum = tags_td[i].text
    elif str(i).endswith("2"):
        #iterations that end in 2 are the statement link
        #if we can we will try to parse the HTML to get the href link to the statement
        #Sometimes the HTML is formatted badly and there is a space between the end of the first table cell tag and the beginning of the anchor tag. In this case, the space is considered the next element and the anchor tag is considered the next-next element
        try:
            statelink = tags_td[i].contents[0].get('href',None)
        except:
            statelink = tags_td[i].next_element.next_element.get('href',None)

        # the statement links are actually just the ending to the URL. We need to prepend the appropriate link. After studying the link that is extracted and comparing it to the link the user is brought to upon clicking the link in the table, I found two patterns
        if statelink.startswith('dr_info'):
            statelink = "https://www.tdcj.texas.gov/death_row/" + statelink
        else:
            statelink = "https://www.tdcj.texas.gov" + statelink

        #open the link we just extracted and constructed
        document_stat = urlopen(statelink, context=ctx)
        html_stat = document_stat.read()
        #after examining the HTML on the last statement pages, the best way to extract the statement is to parse the paragraph tags
        soup_stat = BeautifulSoup(html_stat, "html.parser")
        tagsstat_p = soup_stat('p')
        statement = ""
        #the first four paragaphs are other data and can be ignored. All the remaining paragraphs are the last statement. We will iterate through the remaining paragraph tags and append each paragraph text to the current string that is called statement
        for i in range(5,len(tagsstat_p)):
            statement += ' ' + str(tagsstat_p[i].text)
    elif str(i).endswith("5"):
        #if the iteration ends in 5, this is the TDCJ (unique inmate id number)
        tdcj = tags_td[i].text
    elif str(i).endswith("7"):
        #if the iteration ends in 7, this is the date of execution
        exdate = tags_td[i].text
    elif str(i).endswith("9"):
        # if the iteration ends in 9, this is the county where crime took place
        county = tags_td[i].text
        # at this point we have cycled through all the table tags for one particular execution and stored those details in variables. Now we will insert this data as a row in our executions table.
        cur.execute('INSERT OR IGNORE INTO Executions (id, inmate_id, date, county, statement) VALUES ( ?, ?, ?, ?, ?)', ( exnum, tdcj, exdate, county, statement) )
        conn.commit()

cur.close()
