import sqlite3

class Database:

    def __init__(self,name='test.sqlite3'):
        self.db = sqlite3.connect(name)

    def run(self,query):
        try:
            result = self.db.execute(query)
            self.db.commit()
            return result
        except Exception as e:
            print(e)

    def add(self,name,email,pwd):
        query = f'''
            insert into detail(name,email,pwd) values(
                '{name}',
                '{email}',
                '{pwd}'
            );
        '''
        return self.run(query)

    def view(self):
        query = '''
            select * from detail
        '''

        data = self.run(query)
        if data:
            return data.fetchall()
        else:
            print("no data found")

