#!/usr/bin/env python
#-*- coding: utf-8 -*-

###########################################################################
##                                                                       ##
## Copyrights Frédéric Rodrigo 2014                                      ##
##                                                                       ##
## This program is free software: you can redistribute it and/or modify  ##
## it under the terms of the GNU General Public License as published by  ##
## the Free Software Foundation, either version 3 of the License, or     ##
## (at your option) any later version.                                   ##
##                                                                       ##
## This program is distributed in the hope that it will be useful,       ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of        ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ##
## GNU General Public License for more details.                          ##
##                                                                       ##
## You should have received a copy of the GNU General Public License     ##
## along with this program.  If not, see <http://www.gnu.org/licenses/>. ##
##                                                                       ##
###########################################################################

from Analyser_Merge import Analyser_Merge


class Analyser_Merge_Bicycle_Rental_FR_CAPP(Analyser_Merge):
    def __init__(self, config, logger = None):
        self.missing_official = {"item":"8160", "class": 11, "level": 3, "tag": ["merge", "public equipment", "cycle"], "desc": T_(u"CAPP bicycle rental not integrated") }
        Analyser_Merge.__init__(self, config, logger)
        self.officialURL = "http://opendata.agglo-pau.fr/index.php/fiche?idQ=14"
        self.officialName = u"Stations Idécycle du réseau Idelis sur la CAPP"
        self.csv_file = "bicycle_rental_FR_capp.csv.bz2"
        self.osmTags = {
            "amenity": "bicycle_rental",
        }
        self.osmTypes = ["nodes"]
        self.sourceTable = "capp_bicycle_rental"
        self.sourceX = "X"
        self.sourceXfunction = self.float_comma
        self.sourceY = "Y"
        self.sourceYfunction = self.float_comma
        self.sourceSRID = "4326"
        self.defaultTag = {
            "source": u"Communauté d'Agglomération Pau-Pyrénées - 01/2013",
            "amenity": "bicycle_rental",
            "operator": "IDEcycle",
        }
        self.defaultTagMapping = {
            "name": "NOM",
            "capacity": "Nb_velo",
            "vending_machine": lambda res: "yes" if res["Borne_pai"] == "Oui" else None,
        }
        self.conflationDistance = 100
