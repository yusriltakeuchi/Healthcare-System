import pymysql.cursors

class DataDiseases:
    def initDB(self):
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='healthcare',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        return connection

    def getDiseasesAll(self):
        self.connection = self.initDB()
        cursor = self.connection.cursor()

        sql = "SELECT * FROM diseases"
        cursor.execute(sql)
        rows = cursor.fetchall()

        return rows

    def getDiseases(self, name):
        self.connection = self.initDB()
        cursor = self.connection.cursor()

        sql = "SELECT * FROM diseases WHERE name='{}'".format(name)
        cursor.execute(sql)
        rows = cursor.fetchone()
        return rows

    def diseasesExists(self, name):
        self.connection = self.initDB()
        cursor = self.connection.cursor()

        sql = "SELECT * from diseases WHERE name = %s"
        cursor.execute(sql, (name))
        exists = cursor.fetchone()

        if exists == None:
            return False
        else:
            return True

    def getDiseasesID(self, name):
        self.connection = self.initDB()
        cursor = self.connection.cursor()

        sql = "SELECT * from diseases WHERE name = %s"
        cursor.execute(sql, (name))
        rows = cursor.fetchone()

        return rows['id']

    def InsertDiseases(self, title, description):
        
        try:
            #check if diseases exists
            if self.diseasesExists(title) == False:
                self.connection = self.initDB()
                sql = "INSERT INTO diseases (name, description) VALUES(%s, %s)"
                cursor = self.connection.cursor()

                cursor.execute(sql, (title, description))
                self.connection.commit()

                print("     [+] Diseaseas {} successfully inserted".format(title))
            else:
                print("     [*] Diseaseas {} already exists".format(title))
        except Exception as e:
            print("     [ERROR] " + e)
        finally:
            self.connection.close()

    def symptompsExists(self, symptoms):
        self.connection = self.initDB()
        cursor = self.connection.cursor()

        sql = "SELECT * from symptoms WHERE symptoms = %s"
        cursor.execute(sql, (symptoms))
        exists = cursor.fetchone()

        if exists == None:
            return False
        else:
            return True

    def getSymptomsID(self, symptoms):
        self.connection = self.initDB()
        cursor = self.connection.cursor()

        sql = "SELECT * from symptoms WHERE symptoms = %s"
        cursor.execute(sql, (symptoms))
        rows = cursor.fetchone()

        return rows['id']

    def insertSymptoms(self, symptoms):
        try:
            if self.symptompsExists(symptoms) == False:
                self.connection = self.initDB()
                sql = "INSERT INTO symptoms (symptoms) VALUES(%s)"
                cursor = self.connection.cursor()

                cursor.execute(sql, (symptoms))
                self.connection.commit()
                print("     [+] Symptoms {} successfully inserted".format(symptoms))
            else:
                print("     [*] Symptoms {} already exists".format(symptoms))
        except Exception as e:
            print("     [ERROR] " + e)
        finally:
            self.connection.close()

    def getSymptoms(self, diseases):
        self.connection = self.initDB()
        cursor = self.connection.cursor()

        sql = "SELECT s.symptoms FROM diseases_symptoms ds INNER JOIN diseases d ON ds.diseases_id = d.id INNER JOIN symptoms s ON ds.symptoms_id = s.id WHERE d.name = '{}'".format(diseases)
        cursor.execute(sql)
        rows = cursor.fetchall()

        return rows

    def refreshDiseasesSymptoms(self):
        self.connection = self.initDB()
        sql = "DELETE FROM diseases_symptoms"
        cursor = self.connection.cursor()

        cursor.execute(sql)
        self.connection.commit()

    def insertDiseasesSymptoms(self, diseases_id, symptoms_id):
        try:
            self.connection = self.initDB()
            sql = "INSERT INTO diseases_symptoms (diseases_id, symptoms_id) VALUES(%s, %s)"
            cursor = self.connection.cursor()

            cursor.execute(sql, (diseases_id, symptoms_id))
            self.connection.commit()
        except Exception as e:
            print("     [ERROR] " + e)
        finally:
            self.connection.close()

