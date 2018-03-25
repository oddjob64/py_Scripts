import sqlite3 as lite

def create_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if EXISTS words")
        ddl = "CREATE TABLE words (word TEXT PRIMARY KEY NOT NULL,usage_count INT DEFAULT 1 NOT NULL);"
        cur.execute(ddl)
        ddl = "CREATE UNIQUE INDEX words_word_uindex ON words (word)"
        cur.execute(ddl)
    conn.close()



def save_words_to_database(database_path:str, words_list: list):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        for word in words_list:
            # check to see if the word is in there
            sql = "select count(word) from words WHERE word='" + word +"'"
            cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count = usage_count + 1 WHERE word = '" + word + "'"
            else:
                sql = "insert into words(word) VALUES ('" + word + "')"
            cur.execute(sql)
            print("Database save complete!")

