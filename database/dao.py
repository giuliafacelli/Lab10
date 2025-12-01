from database.DB_connect import DBConnect
from model.hub import Hub

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    @staticmethod
    def get_all_hubs():
    #Tutti gli hub del database
        conn = DBConnect.get_connection()
        result = []
        if conn is None:
            return result

        query = 'SELECT * FROM hub'
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            for row in cursor:
                hub = Hub (row['id'], row['codice'], row['nome'], row['citta'],
                          row['stato'], row['latitudine'], row['longitudine'])
                result.append(hub)
            cursor.close()
            return result
        except Exception as e:
            print(f'Errore nella query get_all_hubs: {e}')
            return result
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_tratte_aggregate():
        conn = DBConnect.get_connection()
        result = []
        if conn is None:
            return result

        query = '''
                SELECT 
                    LEAST(id_hub_origine, id_hub_destinazione) AS hub1,
                    GREATEST(id_hub_origine, id_hub_destinazione) AS hub2,
                    SUM(valore_merce) AS somma_valore_merce,
                    COUNT(*) AS conteggio_spedizioni
                FROM spedizione
                WHERE id_hub_origine <> id_hub_destinazione
                GROUP BY hub1, hub2
                '''
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(f'Errore nella query get_tratte_aggregate: {e}')
            return result
        finally:
            if conn:
                conn.close()




