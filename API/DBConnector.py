import mysql.connector
from mysql.connector import errorcode

class DataBaseController():
    def __init__(self, user='root', password='root', host='localhost', database='scp'):
        self._user = user
        self._password = password
        self._host = host
        self._database = database
        self._cursor = None
        self._cnx = None

    def _start_conn(self):
        try:
            self._cnx = mysql.connector.connect(user= self._user, password= self._password,
                                                host= self._host, database= self._database)
            self._cursor = self._cnx.cursor()
        
        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

    def _end_conn(self):
        try:
            self._cursor.close()
            self._cnx.close()

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

    def create(self, name, description, price, amount):
        try:
            if len(self.search_by_specific_name(name)) == 0:
                self._start_conn()
                
                command = "INSERT INTO PRODUCTS (NAME, DESCRIPTION, PRICE, AMOUNT) VALUES (%s ,%s ,%s ,%s)"
                self._cursor.execute(command, (name, description, price, amount))
                self._cnx.commit()

                self._end_conn()
            else:
                print("Não foi possivel criar, ja possui outro com mesmo nome")

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))
    
    def delete(self, id):
        try:
            self._start_conn()

            command = "DELETE FROM PRODUCTS WHERE ID = " + str(id)
            self._cursor.execute(command)
            self._cnx.commit()

            self._end_conn()

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

    def update(self, id, name, description, price, amount):
        try:
            self._start_conn()

            command = "UPDATE PRODUCTS SET NAME = %s, DESCRIPTION = %s, PRICE = %s, AMOUNT = %s WHERE ID = %s"
            self._cursor.execute(command, (name, description, price, amount, id))
            self._cnx.commit()

            self._end_conn()

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))
    
    def search_by_name(self, name):
        try:
            self._start_conn()

            name = '%' + name + '%'
            command = "SELECT * FROM PRODUCTS WHERE NAME LIKE '" + name + "'"
            self._cursor.execute(command)
            result = self._cursor.fetchall()
            self._cnx.commit()

            self._end_conn()
            return result

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

    def search_by_specific_name(self, name):
        try:
            self._start_conn()

            command = "SELECT * FROM PRODUCTS WHERE NAME LIKE '" + name + "'"
            self._cursor.execute(command)
            result = self._cursor.fetchall()
            self._cnx.commit()

            self._end_conn()
            return result

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

    def search_by_id(self, id):
        try:
            self._start_conn()

            command = "SELECT * FROM PRODUCTS WHERE ID = " + str(id)
            self._cursor.execute(command)
            result = self._cursor.fetchall()
            self._cnx.commit()

            self._end_conn()
            return result

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))
    
    def get_products(self):
        try:
            self._start_conn()

            command = "SELECT * FROM PRODUCTS"
            self._cursor.execute(command)
            products = self._cursor.fetchall()
            self._cnx.commit()
            
            self._end_conn()
            return products

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))