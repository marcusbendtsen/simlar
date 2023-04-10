import sqlite3

query = "".join(open("sql/search.sql", "r").readlines())
insert(query, ())
query = "".join(open("sql/report.sql", "r").readlines())
insert(query, ())

##
## Search
##
def search_create(database):
    query = "insert into search (database) values (?)"
    id = insert(query, (database,))
    return id

##
## Report
##
def report_create(search_id, title):
    query = "insert into report (search, title) values (?,?)"
    id = insert(query, (search_id, title))
    return id

##
## Select, insert, connect
##
def select(query):
    con = connect()
    try:
        cur = con.cursor()
        res = cur.execute(query)
        res = res.fetchall()
        con.commit()
        con.close()
        return res
    except Exception as e:
        print(e)
        con.close()


def insert(query, data):
    con = connect()
    try:
        cur = con.cursor()
        cur.execute(query, data)
        id = cur.lastrowid
        con.commit()
        con.close()
        return id
    except Exception as e:
        print(e)
        con.close()


def connect(db="database.db"):
    con = sqlite3.connect(db)
    con.execute("PRAGMA foreign_keys = 1")
    return con
        

select("select * from search")
select("select * from report")


search_create("pubmed")
report_create(1, "Testing title")

