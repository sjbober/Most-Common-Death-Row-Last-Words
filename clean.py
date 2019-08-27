import sqlite3
import pandas as pd
import re
from removecontdupes import removeContractionsDuplicates

#connect to the executions db and create a panda Series from the statement row
conn = sqlite3.connect('executions.sqlite')
statements = pd.read_sql_query('SELECT statement FROM Executions', conn)
statements = statements['statement']

#clean up the data- convert to all lowercase, remove headings like "statement to the media", remove all punctuation EXCEPT apostophres (we will deal with those later by expanding contractions). plus replace the weird ’ and ‘ with regular apostrophes so that we can accurately expand extractions later
statements= statements.str.lower()
statements = statements.str.replace("statement to the media:","")
statements = statements.str.replace('spoken:', "")
statements = statements.str.replace('written statement:', "")
statements = statements.str.replace(r'\.|\!|\?|,|-|\(|\)', "")
statements = statements.str.replace(':', "")
statements = statements.str.replace('"', "")
statements = statements.str.replace(';', "")
statements = statements.str.replace('\n', "")
statements = statements.str.replace('\r', "")
statements = statements.str.replace('\’',"\'")
statements = statements.str.replace('\‘',"\'")

#now we will use the function removeContractionsDuplicates to build a string that has no contraction and no duplicates.
for statement in statements:
    new_state = removeContractionsDuplicates(statement)
    statements = statements.str.replace(statement,new_state)

# #at this point all "'s" that occur in the text should be possessive and can be removed
statements = statements.str.replace("\'s","")
# print(statements)
