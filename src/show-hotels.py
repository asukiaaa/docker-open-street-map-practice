#!/usr/bin/env python

from OSMPythonTools.data import Data
from typing import Any

import osmium

class HotelHandler(osmium.SimpleHandler):
    hodels: list[Any] = []

    def __init__(self):
        osmium.SimpleHandler.__init__(self)
        self.hotels = []

    def node(self, o):
        if o.tags.get('tourism') == 'hotel' and 'name' in o.tags:
            print(o.tags['name'])
            self.hotels.append(o.tags['name']) # 値を保持する


h = HotelHandler()
h.apply_file("./kanto-latest.osm.pbf")

print(sorted(h.hotels))
