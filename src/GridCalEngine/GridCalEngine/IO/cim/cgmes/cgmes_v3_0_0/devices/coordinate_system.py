# GridCal
# Copyright (C) 2015 - 2023 Santiago Peñate Vera
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
from GridCalEngine.IO.base.units import UnitMultiplier, UnitSymbol
from GridCalEngine.IO.cim.cgmes.cgmes_v3_0_0.devices.identified_object import IdentifiedObject
from GridCalEngine.IO.cim.cgmes.cgmes_enums import cgmesProfile


class CoordinateSystem(IdentifiedObject):
	def __init__(self, rdfid='', tpe='CoordinateSystem'):
		IdentifiedObject.__init__(self, rdfid, tpe)

		self.crsUrn: str = None
		from GridCalEngine.IO.cim.cgmes.cgmes_v3_0_0.devices.location import Location
		self.Locations: Location | None = None

		self.register_property(
			name='crsUrn',
			class_type=str,
			multiplier=UnitMultiplier.none,
			unit=UnitSymbol.none,
			description='''A Uniform Resource Name (URN) for the coordinate reference system (crs) used to define 'Location.PositionPoints'.
An example would be the European Petroleum Survey Group (EPSG) code for a coordinate reference system, defined in URN under the Open Geospatial Consortium (OGC) namespace as: urn:ogc:def:crs:EPSG::XXXX, where XXXX is an EPSG code (a full list of codes can be found at the EPSG Registry web site http://www.epsg-registry.org/). To define the coordinate system as being WGS84 (latitude, longitude) using an EPSG OGC, this attribute would be urn:ogc:def:crs:EPSG::4236.
A profile should limit this code to a set of allowed URNs agreed to by all sending and receiving parties.''',
			profiles=[]
		)
		self.register_property(
			name='Locations',
			class_type=Location,
			multiplier=UnitMultiplier.none,
			unit=UnitSymbol.none,
			description='''All locations described with position points in this coordinate system.''',
			profiles=[]
		)
