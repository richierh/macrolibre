#!/usr/bin/python
import os
import sqlite3


def create_connection(db_file):  # db_file):
    try:
        # db_file="db.db"
        conn = sqlite3.connect(db_file)            
        print ("conneffct")
        return conn

    except Exception as e:
        print ("dd")
        print(e)
 
    return None

 
def close(conn):
    conn.close()
    print ("Great udah diputus")


def create_table(conn, create_table_sql):
    c = conn.cursor()
    c.execute(create_table_sql)

    
def main(db):
    database = db
    sql_create_projects_table = """ 
    CREATE TABLE IF NOT EXISTS `personft` (
    `idpersonft`    int,
    `nama`    text,
    `tgl_tes`    date,
    `jenis_kelamin`    text,
    `tgl_lahir`    date,
    `asal_sekolah`    text,
    `jurusan`    text,
    `kota`    text,
    `hobi`    text,
    `prestasi_akademik`    text,
    `prestasi_non`    akademik text,
    `eksul`    text,
    PRIMARY KEY(`idpersonft`)
);"""

    sql_create_table2 = """
CREATE TABLE IF NOT EXISTS `personfs` (
    `idpersonfs`    int,
    `no_tes`    int,
    `tgl_tes`    date,
    `nama_kandidat`    text,
    `jenis_kelamin`    text,
    `tgl_lahir`    date,
    `pendidikan_terakhir`    text,
    `jurusan`    text,
    `kota`    text,
    `perusahaanorinstansi`    text,
    `posisiorjabatan`    text,
    PRIMARY KEY(`idpersonfs`)
);"""
    sql_create_table3 = """CREATE TABLE IF NOT EXISTS `kuncijawaban`(
                            `idkuncijawaban`    int,
                            `personfsid`    int,
                            `personftid`    int,
                            FOREIGN KEY(`personftid`) REFERENCES `personft`(`idpersonft`),
                            PRIMARY KEY(`idkuncijawaban`),
                            FOREIGN KEY(`personfsid`) REFERENCES `personfs`(`idpersonfs`)
                                ); """
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
        # create tasks table
       
        create_table(conn, sql_create_table2)
        
        create_table(conn, sql_create_table3)
    else:
        print("Error! cannot create the database connection.")
    
    conn.close()
    print ("sudah ditutup")

    
def createdatabasename():
    namadatabase = "riasec"
    print (os.getcwd())
    db_file = "db.db"
    create_connection(db_file)
    main(namadatabase)

# createdatabasename()

    
class dataprocess():
    
    def __init___(self):
        
        pass
    
    def __method__(self):
        pass


class CreateDatabaseName():
    
    def __init__(self):
        self.database = []
        self.listfile = os.listdir(os.getcwd())
        print (self.listfile)
    
    def inputnamedatabase(self, adding):
        self.adding = adding
#         self.database.append(adding)
        for listf in self.listfile:
            print (listf)
            if listf != self.adding:
                print ("tidak sama")
                self.database.append(listf)
#                 return self.database.append(adding)
            else :
                print ("data sudah ada")
                
                break
        return self.database.append(self.adding)


k = CreateDatabaseName()
k.inputnamedatabase("db.db")
    
print (k.database)
    
