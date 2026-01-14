from dataclasses import dataclass

from model.hub import Hub


@dataclass
class Tratta:
    h1: Hub
    h2: Hub
    valore_totale: float
    numero_spedizioni: int