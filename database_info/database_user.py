import mysql.connector


class database1():
    def conn(self):
        con = mysql.connector.connect(user='root', password='', host='localhost', database='final python pro')
        return con

    def get_user(self):
        c = self.conn()
        cur = c.cursor()
        sql = 'select * from user_information'
        try:
            cur.execute(sql)
            list_data = cur.fetchall()
            return list_data
        except Exception as e:
            print(e)
            return None

    def check_user(self, user, passWord):
        data = self.get_user()
        username = []
        password = []
        for i in data:
            username.append(i[1])
            password.append(i[2])
        j = 0
        while j < len(username):
            if username[j] == user:
                if password[j] == passWord:
                    return 1
                else:
                    return 2
            else:
                j += 1
                continue
                return 3

    def get_status(self, s1):
        c = self.conn()
        cur = c.cursor()
        sql = "select type from user_information where filiere='%s'" % s1
        try:
            cur.execute(sql)
            data = cur.fetchall()
            return data[0][0]
        except Exception as ee:
            print(ee)
            return None

    def insert_data(self, f, p, u, t, d):
        c = self.conn()
        cur = c.cursor()
        sql = "insert into user_information (fullname,password,filiere,type,department) values ('%s', '%s', '%s', '%s', '%s')" % (f, p, u, t, d)
        try:
            cur.execute(sql)
            c.commit()
            print('Inserted rows')
        except Exception as ee:
            c.rollback()
            print(ee)
        c.close()

    def get_student(self):
        c = self.conn()
        cur = c.cursor()
        sql = "select * from user_information where type='student'"
        try:
            cur.execute(sql)
            list_data = cur.fetchall()
            return list_data
        except Exception as e:
            print(e)
            return None

    def delete_user(self, id):
        c = self.conn()
        cur = c.cursor()
        sql = "delete from user_information where id='%d'" % id
        sql1 = "delete from degree where id='%d'" % id
        try:
            cur.execute(sql)
            cur.execute(sql1)
            c.commit()
        except Exception as e:
            print(e)
