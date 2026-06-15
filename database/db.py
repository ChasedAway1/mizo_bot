import sqlite3
import os

class Database:
    def __init__(self, db_file="database/bot.db"):
        self.db_file = db_file
        os.makedirs(os.path.dirname(db_file), exist_ok=True)
        self.init_db()
    
    def get_connection(self):
        return sqlite3.connect(self.db_file)
    
    def init_db(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS svo_measures (
                measure_id INTEGER PRIMARY KEY,
                title TEXT,
                docs TEXT,
                right_text TEXT,
                conditions TEXT,
                howto TEXT,
                law TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS large_family (
                id INTEGER PRIMARY KEY,
                law TEXT,
                conditions TEXT,
                order_text TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS laws_parts (
                part_id INTEGER PRIMARY KEY,
                part_text TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS common (
                id INTEGER PRIMARY KEY,
                text TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def get_svo_title(self, measure_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM svo_measures WHERE measure_id = ?", (measure_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else "Информация временно недоступна"
    
    def get_svo_docs(self, measure_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT docs FROM svo_measures WHERE measure_id = ?", (measure_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else "Информация временно недоступна"
    
    def get_svo_right(self, measure_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT right_text FROM svo_measures WHERE measure_id = ?", (measure_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else "Информация временно недоступна"
    
    def get_svo_conditions(self, measure_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT conditions FROM svo_measures WHERE measure_id = ?", (measure_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else "Информация временно недоступна"
    
    def get_svo_howto(self, measure_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT howto FROM svo_measures WHERE measure_id = ?", (measure_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else "Информация временно недоступна"
    
    def get_svo_law(self, measure_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT law FROM svo_measures WHERE measure_id = ?", (measure_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else "Информация временно недоступна"
    
    def get_large_law(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT law FROM large_family WHERE id = 1")
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else "Информация временно недоступна"
    
    def get_large_conditions(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT conditions FROM large_family WHERE id = 1")
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else "Информация временно недоступна"
    
    def get_large_order(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT order_text FROM large_family WHERE id = 1")
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else "Информация временно недоступна"
    
    def get_laws_part(self, part_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT part_text FROM laws_parts WHERE part_id = ?", (part_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else "Информация временно недоступна"
    
    def get_common_question(self):
        return """Каков порядок приобретения земельного участка для индивидуального жилищного строительства в собственность, аренду или постоянное бессрочное пользование?

В соответствии со ст. 28 Земельного кодекса Российской Федерации предоставление земельных участков, находящихся в государственной или муниципальной собственности, в собственность граждан и юридических лиц осуществляется за плату, на торгах.

Информацию о проведении торгов по продаже земельных участков для индивидуального жилищного строительства Вы можете получить в Комитете по управлению имуществом и землепользованию (г. Улан-Удэ, ул. Бабушкина, 25, тел. 23-18-55), а также в сети Интернет на официальном сайте, по адресу: http://www.ulan-ude-eg.ru/today/zemeln/konkurs/index.php.

Также земельный участок для индивидуального жилищного строительства может быть предоставлен в аренду.

В соответствии со ст. 30.1 Земельного кодекса Российской Федерации предоставление земельного участка для индивидуального жилищного строительства может осуществляться на основании заявления гражданина, заинтересованного в предоставлении земельного участка.

В двухнедельный срок со дня получения заявления гражданина о предоставлении в аренду земельного участка исполнительный орган местного самоуправления может принять решение о проведении аукциона по продаже земельного участка или права на заключение договора аренды такого земельного участка либо опубликовать сообщение о приеме заявлений о предоставлении в аренду такого земельного участка с указанием местоположения земельного участка, его площади, разрешенного использования в периодическом печатном издании, а также разместить сообщение о приеме указанных заявлений на официальном сайте в сети Интернет.

В случае, если по истечении месяца со дня опубликования сообщения о приеме заявлений о предоставлении в аренду земельного участка заявления не поступили, орган местного самоуправления, принимает решение о предоставлении такого земельного участка для жилищного строительства в аренду гражданину.

В случае поступления заявления о предоставлении в аренду такого земельного участка проводится аукцион по продаже права на заключение договора аренды земельного участка.

Для приобретения земельного участка в аренду Вам необходимо обратиться в Комитет по управлению имуществом и землепользованию г. Улан-Удэ (670031, г. Улан-Удэ, ул. Бабушкина, д. 25, тел. 23-18-47) либо в Многофункциональный центр, расположенный по адресу: г. Улан-Удэ ул. Ключевская, 56 а, часы работы: 08.30-17.30, перерыв: 12.00-13.00, выходные: суббота, воскресенье.

Что касается вопроса о приобретении земельного участка в постоянное бессрочное пользование, то в соответствии со ст. 20 Земельного кодекса РФ гражданам земельные участки в постоянное (бессрочное) пользование не предоставляются.

Дополнительно сообщаем, что в настоящее время на территории республики действует Закон Республики Бурятия от 16.10.2002 № 115-III О бесплатном предоставлении в собственность земельных участков, находящихся в государственной и муниципальной собственности, которым предусмотрено бесплатное предоставление земельных участков для индивидуального жилищного строительства льготной категории граждан.

В том случае, если Вы относитесь к льготной категории граждан Вам необходимо обратиться также в Многофункциональный центр."""