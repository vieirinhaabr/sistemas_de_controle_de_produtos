import mysql.connector


class DataBaseController:
    def __init__(self, user='root', password='root', host='localhost', database='scp'):
        self.__user = user
        self.__password = password
        self.__host = host
        self.__database = database
        self.__cursor = None
        self.__cnx = None

    def __enter__(self):
        self.__cnx = mysql.connector.connect(user=self.__user, password=self.__password,
                                             host=self.__host, database=self.__database)
        self.__cursor = self.__cnx.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cnx.close()

    def create(self, name: str, description: str, price: float, amount: int):
        try:
            if len(self.__search_by_specific_name(name)) == 0:
                command = "INSERT INTO PRODUCTS (NAME, DESCRIPTION, PRICE, AMOUNT) VALUES (%s ,%s ,%s ,%s)"
                self.__cursor.execute(command, (name, description, price, amount))
                self.__cnx.commit()

            else:
                print("Não foi possivel criar, ja possui outro com mesmo nome")

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

        finally:
            self.__cursor.close()

    def delete(self, id: int):
        try:
            command = "DELETE FROM PRODUCTS WHERE ID = " + str(id)
            self.__cursor.execute(command)
            self.__cnx.commit()

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

        finally:
            self.__cursor.close()

    def update(self, id: int, name: str, description: str, price: float, amount: int):
        try:
            command = "UPDATE PRODUCTS SET NAME = %s, DESCRIPTION = %s, PRICE = %s, AMOUNT = %s WHERE ID = %s"
            self.__cursor.execute(command, (name, description, price, amount, id))
            self.__cnx.commit()

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

        finally:
            self.__cursor.close()

    def search_by_name(self, name: str):
        try:
            name = '%' + name + '%'
            command = "SELECT * FROM PRODUCTS WHERE NAME LIKE '" + name + "'"
            self.__cursor.execute(command)
            result = self.__cursor.fetchall()
            self.__cnx.commit()

            return result

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

        finally:
            self.__cursor.close()

    def __search_by_specific_name(self, name: str):
        try:
            command = "SELECT * FROM PRODUCTS WHERE NAME LIKE '" + name + "'"
            self.__cursor.execute(command)
            result = self.__cursor.fetchall()
            self.__cnx.commit()

            return result

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

    def search_by_id(self, id: int):
        try:
            command = "SELECT * FROM PRODUCTS WHERE ID = " + str(id)
            self.__cursor.execute(command)
            result = self.__cursor.fetchall()
            self.__cnx.commit()

            return result

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

        finally:
            self.__cursor.close()

    def get_products(self):
        try:
            command = "SELECT * FROM PRODUCTS"
            self.__cursor.execute(command)
            products = self.__cursor.fetchall()
            self.__cnx.commit()

            return products

        except Exception as e:
            print("Ocorreu o seguinte erro --------> {}".format(e))

        finally:
            self.__cursor.close()
