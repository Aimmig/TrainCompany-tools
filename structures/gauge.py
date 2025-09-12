from __future__ import annotations
from typing import Dict
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Gauge:
    idstring: str
    name: str

gauges: Dict[str, Gauge] = {gauge.idstring: gauge for gauge in (
    Gauge(idstring="750mm", name="Schmalspur (750mm)"),
    Gauge(idstring="760mm", name="Bosnaspur"),
    Gauge(idstring="891mm", name="Schwedische Schmalspur"),
    Gauge(idstring="1000mm", name="Meterspur"),
    Gauge(idstring="1067mm", name="Kapspur"),
    Gauge(idstring="1435mm", name="Normalspur"),
    Gauge(idstring="1520mm", name="Russische Breitspur"),
    Gauge(idstring="1600mm", name="Irische Breitspur"),
    Gauge(idstring="1668mm", name="Iberische Breitspur"),
    Gauge(idstring="1676mm", name="Indische Breitspur"),
)}
