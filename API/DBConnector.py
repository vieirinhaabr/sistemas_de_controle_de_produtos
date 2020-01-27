import mysql.connector
from mysql.connector import errorcode

class DataBaseController():
    def __init__(self, user='root', password='root', host='localhost', database='scp'):
        self.__user = user
        self.__password = password
        self.__host = host
        self.__database = database
        self.__cursor = None
        self.__cnx = None

    def __start_conn(self):
        try:
            self.__cnx = mysql.connector.connect(user= self.__user, password= self.__password,
                                                host= self.__host, database= self.__database)
            self.__cursor = self.__cnx.cursor()
        
        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

    def __end_conn(self):
        try:
            self.__cursor.close()
            self.__cnx.close()

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

    def create(self, name, description, price, amount):
        try:
            if len(self.search_by_specific_name(name)) == 0:
                self.__start_conn()
                
                command = "INSERT INTO PRODUCTS (NAME, DESCRIPTION, PRICE, AMOUNT) VALUES (%s ,%s ,%s ,%s)"
                self.__cursor.execute(command, (name, description, price, amount))
                self.__cnx.commit()

                self.__end_conn()
            else:
                print("Não foi possivel criar, ja possui outro com mesmo nome")

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))
    
    def delete(self, id):
        try:
            self.__start_conn()

            command = "DELETE FROM PRODUCTS WHERE ID = " + str(id)
            self.__cursor.execute(command)
            self.__cnx.commit()

            self.__end_conn()

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

    def update(self, id, name, description, price, amount):
        try:
            self.__start_conn()

            command = "UPDATE PRODUCTS SET NAME = %s, DESCRIPTION = %s, PRICE = %s, AMOUNT = %s WHERE ID = %s"
            self.__cursor.execute(command, (name, description, price, amount, id))
            self.__cnx.commit()

            self.__end_conn()

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))
    
    def search_by_name(self, name):
        try:
            self.__start_conn()

            name = '%' + name + '%'
            command = "SELECT * FROM PRODUCTS WHERE NAME LIKE '" + name + "'"
            self.__cursor.execute(command)
            result = self.__cursor.fetchall()
            self.__cnx.commit()

            self.__end_conn()
            return result

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

    def search_by_specific_name(self, name):
        try:
            self.__start_conn()

            command = "SELECT * FROM PRODUCTS WHERE NAME LIKE '" + name + "'"
            self.__cursor.execute(command)
            result = self.__cursor.fetchall()
            self.__cnx.commit()

            self.__end_conn()
            return result

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

    def search_by_id(self, id):
        try:
            self.__start_conn()

            command = "SELECT * FROM PRODUCTS WHERE ID = " + str(id)
            self.__cursor.execute(command)
            result = self.__cursor.fetchall()
            self.__cnx.commit()

            self.__end_conn()
            return result

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))
    
    def get_products(self):
        try:
            self.__start_conn()

            command = "SELECT * FROM PRODUCTS"
            self.__cursor.execute(command)
            products = self.__cursor.fetchall()
            self.__cnx.commit()
            
            self.__end_conn()
            return products

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))