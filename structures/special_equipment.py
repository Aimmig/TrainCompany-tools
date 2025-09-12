from __future__ import annotations
from typing import Dict
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Equipment:
    idstring: str
    name: str

equipments: Dict[str, Equipment] = {equipment.idstring: equipment for equipment in (
    Equipment(idstring="ETCS", name="ETCS"),
    Equipment(idstring="KRM", name="KRM"),
    Equipment(idstring="TVM", name="TVM"),
    Equipment(idstring="bostrab", name="BOStrab"),
    Equipment(idstring="Eurotunnel", name="Eurotunnel"),
    Equipment(idstring="SP-SEETAL", name="Sonderprofil Seetal"),
)}
