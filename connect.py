# Connect to DB
# Make all CSV's data persistant in DB
import pyodbc
import csv

# Creating Connection Class

class Conct_MS_SQL_IMDB:
    #when intialize we make the connection
    def __init__(self, listoffilms, server = 'localhost,1433', database='IMDB',username='SA',password='Passw0rd2018'):
        self.listoffilms = listoffilms
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.dockr_conct = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.cursor = self.dockr_conct.cursor()

    def sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def insert(self):
        for row in self.listoffilms:
            self.sql_query(f"INSERT INTO [Titles] VALUES "
                           f"('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}')")
            self.dockr_conct.commit()



# def transform_imdb_details(csv_full_name):  # opening imdbtitle and transforming ans then createing new csv
#     newimdb_data = []
#
#     with open(csv_full_name, newline='') as csv_file:
#         title_details_csv = csv.reader(csv_file, delimiter=',')
#         iterable = iter(title_details_csv)
#         next(iterable)
#
#         for rowlist in iterable:
#             transformed_row = []
#             transformed_row.append(rowlist[0].capitalize())         # titleType
#             transformed_row.append(rowlist[1].replace("'", "''"))   # primaryTitle
#             transformed_row.append(rowlist[2].replace("'", "''"))   # originalTitle
#             transformed_row.append(rowlist[4])                      # startYear
#             if str.isdigit(rowlist[6]):
#                 transformed_row.append(rowlist[6])                  # runtimeMinutes
#             else:
#                 transformed_row.append("")
#             transformed_row.append(rowlist[7].capitalize())         # genres
#             newimdb_data.append(transformed_row)
#         return newimdb_data
#
#print(new_trans_data)
#
# Let create a function to write our transformed data
#   write to csv
#
# def create_new_csv_imdb_data(transformed_data, new_imdb_file_name):
#     # have transformed data
#     # open new file
#     new_file = open(new_imdb_file_name, 'w', newline='')
#
#     #write to that file
#     with new_file:
#         csv_writer = csv.writer(new_file)
#         csv_writer.writerows(transformed_data)
#
#
# #
#
# # creating DB
# imdb_db = Conct_MS_SQL_IMDB()
#
# imdb_db.sql_query("CREATE TABLE [Titles] ([titleType] VARCHAR(30),"
#                   "[primaryTitle] VARCHAR(70),"
#                   "[originalTitle] VARCHAR(70),"
#                   "[startYear] DATE,"
#                   "[runtimeMinutes] SMALLINT,"
#                   "[genres] VARCHAR(70))")
#
# # Putting csv into the DB
#
#
#
# with open('transformed_imdb_csv.csv', newline='') as csv_file:
#     csvreader = csv.reader(csv_file, delimiter=',')
#     #iterable = iter(csvreader)
#     #print(iterable)
#     #next(iterable)
#     for row in csvreader:
#         print(row)
#         imdb_db.sql_query(f"INSERT INTO [Titles] VALUES "
#                           f"('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}')")
#         imdb_db.dockr_conct.commit()