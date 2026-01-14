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
        # TODO
        self.G.clear()

        self._nodes = DAO.get_all_hubs()
        self._edges = DAO.get_all_tratte()

        self.G.add_nodes_from(self._nodes.values())

        for tratta in self._edges:
            valore_medio = tratta.valore_totale/tratta.numero_spedizioni
            h1_oggetto = self._nodes[tratta.h1]
            h2_oggetto = self._nodes[tratta.h2]
            if valore_medio >= threshold:
                self.G.add_edge(h1_oggetto, h2_oggetto, weight=valore_medio)
                print('Tratta aggiunta', tratta)


    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO

        return self.G.edges(data=True)


