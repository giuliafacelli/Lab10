from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        self.G.clear()
        self._nodes = []
        self._edges = []
        self._id_map = {}

        all_hubs = DAO.get_all_hubs()
        self._nodes = all_hubs
        for hub in all_hubs:
            self._id_map[hub.id] = hub

        self.G.add_nodes_from(self._id_map.keys())

        tratte = DAO.get_tratte_aggregate()

        for tratta in tratte:
            peso = tratta['somma_valore_merce'] / tratta['conteggio_spedizioni']
            if peso >= threshold:
                self.G.add_edge(tratta['hub1'], tratta['hub2'], weight=peso)

        self._edges = list(self.G.edges(data=True))

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        numero_tratte = self.G.number_of_edges()
        return numero_tratte

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        numero_nodi = self.G.number_of_nodes()
        return numero_nodi

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        return self._edges

    def get_hub_from_id(self, hub_id):
        #per stampare il nome della città al posto del numero

        return self._id_map.get(hub_id)

