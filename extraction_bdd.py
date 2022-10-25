import sqlite3
# Connect the bdd
conn = sqlite3.connect('banque.db')
# We need to create the cursor

# Print the name of colums
cursor = conn.cursor()
data=cursor.execute("SELECT * FROM 'client'")
print(data.description)

# #get table names
res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in res.fetchall():
    print(name[0])
    
    # Print the name of colums
cursor = conn.cursor()
data=cursor.execute("SELECT * FROM 'client'")
print(data.description)

# Print the name of colums
cursor = conn.cursor()
data=cursor.execute("SELECT * FROM 'compte'")
print(data.description)

# Print the name of colums
cursor = conn.cursor()
data=cursor.execute("SELECT * FROM 'operation'")
print(data.description)


#Donner le nom et le prénom de tous les clients:
print("\n1) Voici tous les clients :")
cursor.execute("SELECT nom, prenom FROM client")
for x in cursor.fetchall():
    print(x)