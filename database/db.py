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
        
        # Таблицы
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS svo_measures (
                measure_id INTEGER PRIMARY KEY,
                title TEXT,
                docs TEXT,
                right_text TEXT,
                conditions TEXT,
                howto TEXT,
                law TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS large_family (
                id INTEGER PRIMARY KEY,
                law TEXT,
                conditions TEXT,
                order_text TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS laws_parts (
                part_id INTEGER PRIMARY KEY,
                part_text TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS common (
                id INTEGER PRIMARY KEY,
                text TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Проверка и заполнение
        cursor.execute("SELECT COUNT(*) FROM svo_measures")
        if cursor.fetchone()[0] == 0:
            self.insert_default_data(cursor)
        
        conn.commit()
        conn.close()
    
    def insert_default_data(self, cursor):
        # Здесь ваши INSERT запросы (как в init_db.py)
        pass
    
    def get_svo_title(self, measure_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM svo_measures WHERE measure_id = ?", (measure_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else "Информация временно недоступна"
    
    # Остальные методы get_svo_docs, get_svo_right и т.д. — аналогично
    
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
    
    def get_common_text(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT text FROM common WHERE id = 1")
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else "Информация будет добавлена позже."