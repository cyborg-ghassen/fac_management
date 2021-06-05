import mysql.connector


class database2():
    def conn(self):
        con = mysql.connector.connect(user='root', password='', host='localhost', database='final python pro')
        return con

    def insert_data(self, id, m1, m2, m3):
        c = self.conn()
        cur = c.cursor()
        s = m1 + m2 + m3
        sql = "insert into degree values('%d', '%d', '%d', '%d', '%d')" % (id, m1, m2, m3, s)
        try:
            cur.execute(sql)
            c.commit()
            print('Inserted rows')
        except Exception as ee:
            print(ee)
            c.rollback()
        c.close()

    def get_degree(self, id):
        c = self.conn()
        cur = c.cursor()
        sql = "select * from degree where id='%d'" % id
        try:
            cur.execute(sql)
            list_data = cur.fetchall()
            return list_data
        except Exception as e:
            print(e)
            return None
        c.close()

    def update_data(self, id, m1, m2, m3):
        c = self.conn()
        cur = c.cursor()
        sum = m1 + m2 + m3
        sql = "update degree set m1='%d', m2='%d', m3='%d', sum='%d' where id='%d'" % (m1, m2, m3, sum, id)
        try:
            cur.execute(sql)
            c.commit()
            print("Updated row")
        except Exception as e:
            c.rollback()
            print(e)
        c.close()

    def get_degrees(self):
        c = self.conn()
        cur = c.cursor()
        sql = "select user_information.id, fullname, department, degree.m1, degree.m2, degree.m3, degree.sum from user_information, degree where user_information.id=degree.id"
        try:
            cur.execute(sql)
            list_data = cur.fetchall()
            return list_data
        except Exception as ee:
            print(ee)
            return None
