import sqlite3

conn = sqlite3.connect(r'data.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS locations (name, description, longitude, latitude, hours, category);')

cur.execute('INSERT INTO locations VALUES ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}");'.format(\
    "library1", "this is a library", -127.6476, 53.7267, 'NA', 'Library'))
cur.execute('INSERT INTO locations VALUES ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}");'.format(\
    "library2", "this is a library", -127.6476, 53.7267, 'NA', 'Library'))
cur.execute('INSERT INTO locations VALUES ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}");'.format(\
    "library3", "this is a library", -127.6476, 53.7267, 'NA', 'Library'))
cur.execute('INSERT INTO locations VALUES ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}");'.format(\
    "library4", "this is a library", -127.6476, 53.7267, 'NA', 'Library'))
cur.execute('INSERT INTO locations VALUES ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}");'.format(\
    "library5", "this is a library", -127.6476, 53.7267, 'NA', 'Library'))
cur.execute('INSERT INTO locations VALUES ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}");'.format(\
    "library6", "this is a library", -127.6476, 53.7267, 'NA', 'Library'))
conn.commit()
conn.close()