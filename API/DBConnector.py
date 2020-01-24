import mysql.connector
from mysql.connector import errorcode

class DataBaseController():
    user = None
    password = None
    host = None
    database = None

    def __init__(self, user='root', password='root', host='localhost', database='scp'):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def create(self, name, description, price, amount):
        try:
            cnx = mysql.connector.connect(user= self.user, password= self.password,
                                          host= self.host, database= self.database)
            cursor = cnx.cursor()

            if len(self.search_by_name(name)) == 0:
                command = "INSERT INTO PRODUCTS (NAME, DESCRIPTION, PRICE, AMOUNT) VALUES (%s ,%s ,%s ,%s)"
                cursor.execute(command, (name, description, price, amount))

                cnx.commit()

                cursor.close()
                cnx.close()

            else:
                return False

            return True

        except mysql.connector.Error as err:
            return False
    
    def delete(self, id):
        try:
            cnx = mysql.connector.connect(user= self.user, password= self.password,
                                          host= self.host, database= self.database)
            cursor = cnx.cursor()

            command = "DELETE FROM PRODUCTS WHERE ID = " + str(id)
            cursor.execute(command)

            cnx.commit()

            cursor.close()
            cnx.close()
            return True

        except mysql.connector.Error:
            return False

    def update(self, id, name, description, price, amount):
        try:
            cnx = mysql.connector.connect(user= self.user, password= self.password,
                                          host= self.host, database= self.database)
            cursor = cnx.cursor()

            command = "UPDATE PRODUCTS SET NAME = %s, DESCRIPTION = %s, PRICE = %s, AMOUNT = %s WHERE ID = %s"
            cursor.execute(command, (name, description, price, amount, id))

            cnx.commit()

            cursor.close()
            cnx.close()
            return True

        except mysql.connector.Error:
            return False
    
    def search_by_name(self, name):
        try:
            cnx = mysql.connector.connect(user= self.user, password= self.password,
                                          host= self.host, database= self.database)
            cursor = cnx.cursor(buffered=True)

            name = '%' + name + '%'
            command = "SELECT * FROM PRODUCTS WHERE NAME LIKE '" + name + "'"
            cursor.execute(command)
            result = cursor.fetchall()

            cnx.commit()

            cursor.close()
            cnx.close()
            return result

        except mysql.connector.Error:
            return False

    def search_by_id(self, id):
        try:
            cnx = mysql.connector.connect(user= self.user, password= self.password,
                                          host= self.host, database= self.database)
            cursor = cnx.cursor()

            command = "SELECT * FROM PRODUCTS WHERE ID = " + str(id)
            cursor.execute(command)
            result = cursor.fetchall()

            cnx.commit()

            cursor.close()
            cnx.close()
            return result

        except mysql.connector.Error:
            return False
    
    def get_products(self):
        try:
            cnx = mysql.connector.connect(user= self.user, password= self.password,
                                          host= self.host, database= self.database)
            cursor = cnx.cursor()

            command = "SELECT * FROM PRODUCTS"
            cursor.execute(command)
            products = cursor.fetchall()

            cnx.commit()

            cursor.close()
            cnx.close()
            return products

        except mysql.connector.Error:
            return False
