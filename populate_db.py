import json
import sqlite3

conn = sqlite3.connect("The_Messier_Dualis_Database.db")
curr = conn.cursor()

f = open('messier.json', 'r')
data = json.loads(f.read())
for obj in data['data'].values():
    # obj is the object
    curr.execute(f'''INSERT INTO The_Messier_Objects_Catalogue (Messier_Number, Name, Distance, Object_Type, Constellation, Apparent_Magnitude, Image_File) VALUES (
                 \"M{obj['messierNumber']}\", \"{obj['name']}\", {obj['distance']}, \"{obj['type']}\", \"{obj['constellation']}\", {obj['magnitude']}, \"Messier_{obj['messierNumber']}.jpg\"
    )''')

conn.commit()
conn.close()