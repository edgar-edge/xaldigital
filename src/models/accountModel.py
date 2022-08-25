from database.db import get_connection
from .entities.accounts import Account

class AccountModel():
    @classmethod
    def get_account(self):
        try:
            connection=get_connection()
            clients=[]
            sql = '''select * from accounts 
                     group by user_id
                     order by user_id
                     limit 25'''

            with connection.cursor() as cur:
                cur.execute(sql)
                result = cur.fetchall()

                for row in result:
                    client = Account(row[0], row[1], row[2], \
                        row[3], row[4], row[5], row[6],row[7],\
                        row[8],row[9], row[10], row[11])
                    clients.append(client.to_JSON())
            connection.close()
            return clients
        except Exception as ex:
            raise Exception(ex)
