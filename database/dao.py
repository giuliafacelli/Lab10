from database.DB_connect import DBConnect
from model.hub import Hub
from model.spedizione import Spedizione
from model.compagnia import Compagnia
from model.tratta import Tratta

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO

    @staticmethod
    def get_all_hubs():
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM hub
                """
        try:
            cursor.execute(query)
            for row in cursor:
                result[row['id']] = Hub(**row)
            cursor.close()
            conn.close()
            return result

        except Exception:
            print("Errore nell'esecuzione della query.")


    @staticmethod
    def get_all_spedizioni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM spedizione
                """
        try:
            cursor.execute(query)
            for row in cursor:
                spedizione = Spedizione(**row)
                result.append(spedizione)
            cursor.close()
            conn.close()
            return result

        except Exception:
            print("Errore nell'esecuzione della query.")




    @staticmethod
    def get_all_compagnie():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM compagnie
                """
        try:
            cursor.execute(query)
            for row in cursor:
                compagnia = Compagnia(**row)
                result.append(compagnia)
            cursor.close()
            conn.close()
            return result

        except Exception:
            print("Errore nell'esecuzione della query.")


    @staticmethod
    def get_all_tratte():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT
                        LEAST(id_hub_origine, id_hub_destinazione) AS h1,
                        GREATEST(id_hub_origine, id_hub_destinazione) AS h2,
                FROM spedizione
                SUM(valore_merce) AS valore_totale
                COUNT(*) AS numero_spedizioni
                GROUP BY h1, h2
                """
        try:
            cursor.execute(query)
            for row in cursor:
                tratta = Tratta(**row)
                result.append(tratta)
            cursor.close()
            conn.close()
            return result

        except Exception:
            print("Errore nell'esecuzione della query.")







