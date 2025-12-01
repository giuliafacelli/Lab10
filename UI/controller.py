import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        self._view.lista_visualizzazione.controls.clear()

        threshold_input = self._view.guadagno_medio_minimo.value
        if not threshold_input:
            self._view.show_alert('Attenzione! Inserire un valore soglia.')
            self._view.update()
            return

        try:
            threshold = float(threshold_input)
            if threshold < 0:
                self._view.show_alert('Attenzione! La soglia deve essere un valore non negativo.')
                self._view.update()
                return
        except ValueError:
            self._view.show_alert('Attenzione! La soglia deve essere un numero valido.')
            self._view.update()
            return

            # Costruisce il grafo nel Model
        self._model.costruisci_grafo(threshold)

        num_nodi = self._model.get_num_nodes()
        num_archi = self._model.get_num_edges()
        all_edges = self._model.get_all_edges()

        self._view.lista_visualizzazione.controls.append(
            ft.Text(f'Analisi Tratte con Soglia >= {threshold:.2f} €', weight=ft.FontWeight.BOLD)
        )
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f'Numero totale di Hub (Nodi): {num_nodi}', color='blue')
        )
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f'Numero di Tratte valide (Archi): {num_archi}', color='blue')
        )

        self._view.lista_visualizzazione.controls.append(ft.Divider())

        if num_archi > 0:
            self._view.lista_visualizzazione.controls.append(
                ft.Text('Elenco delle Tratte e Guadagno Medio per Spedizione:', weight=ft.FontWeight.BOLD)
            )

            # Ordina gli archi dal guadagno più alto al più basso
            sorted_edges = sorted(all_edges, key=lambda x: x[2]['weight'], reverse=True)

            for u, v, data in sorted_edges:
                hub_u = self._model.get_hub_from_id(u)
                hub_v = self._model.get_hub_from_id(v)
                weight = data['weight']

                nome_u = hub_u.nome if hub_u else f'Hub ID {u}'
                nome_v = hub_v.nome if hub_v else f'Hub ID {v}'
                tratta_text = f'**{nome_u}** - **{nome_v}**: {weight:.2f} €/spedizione'
                self._view.lista_visualizzazione.controls.append(
                    ft.Text(tratta_text)
                )
            else:
                self._view.lista_visualizzazione.controls.append(
                    ft.Text('Nessuna Tratta commerciale supera la soglia specificata.',
                            color='red', weight=ft.FontWeight.BOLD)
                )

        self._view.update()