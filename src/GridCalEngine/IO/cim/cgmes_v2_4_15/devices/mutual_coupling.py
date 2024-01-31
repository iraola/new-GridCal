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
from GridCalEngine.IO.cim.cgmes_v2_4_15.devices.identified_object import IdentifiedObject
from GridCalEngine.IO.cim.cgmes_v2_4_15.devices.terminal import Terminal
from GridCalEngine.IO.cim.cgmes_v2_4_15.devices.terminal import Terminal
from GridCalEngine.IO.cim.cgmes_v2_4_15.cgmes_enums import cgmesProfile


class MutualCoupling(IdentifiedObject):
	def __init__(self, rdfid='', tpe='MutualCoupling'):
		IdentifiedObject.__init__(self, rdfid, tpe)

		self.First_Terminal: Terminal | None = None
		self.Second_Terminal: Terminal | None = None
		self.b0ch: float = 0.0
		self.distance11: float = 0.0
		self.distance12: float = 0.0
		self.distance21: float = 0.0
		self.distance22: float = 0.0
		self.g0ch: float = 0.0
		self.r0: float = 0.0
		self.x0: float = 0.0

		self.register_property(
			name='First_Terminal',
			class_type=Terminal,
			multiplier=UnitMultiplier.none,
			unit=UnitSymbol.none,
			description='''The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.''',
			profiles=[]
		)
		self.register_property(
			name='Second_Terminal',
			class_type=Terminal,
			multiplier=UnitMultiplier.none,
			unit=UnitSymbol.none,
			description='''The starting terminal for the calculation of distances along the second branch of the mutual coupling.''',
			profiles=[]
		)
		self.register_property(
			name='b0ch',
			class_type=float,
			multiplier=UnitMultiplier.none,
			unit=UnitSymbol.S,
			description='''Imaginary part of admittance.''',
			profiles=[]
		)
		self.register_property(
			name='distance11',
			class_type=float,
			multiplier=UnitMultiplier.k,
			unit=UnitSymbol.m,
			description='''Unit of length. Never negative.''',
			profiles=[]
		)
		self.register_property(
			name='distance12',
			class_type=float,
			multiplier=UnitMultiplier.k,
			unit=UnitSymbol.m,
			description='''Unit of length. Never negative.''',
			profiles=[]
		)
		self.register_property(
			name='distance21',
			class_type=float,
			multiplier=UnitMultiplier.k,
			unit=UnitSymbol.m,
			description='''Unit of length. Never negative.''',
			profiles=[]
		)
		self.register_property(
			name='distance22',
			class_type=float,
			multiplier=UnitMultiplier.k,
			unit=UnitSymbol.m,
			description='''Unit of length. Never negative.''',
			profiles=[]
		)
		self.register_property(
			name='g0ch',
			class_type=float,
			multiplier=UnitMultiplier.none,
			unit=UnitSymbol.S,
			description='''Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.''',
			profiles=[]
		)
		self.register_property(
			name='r0',
			class_type=float,
			multiplier=UnitMultiplier.none,
			unit=UnitSymbol.ohm,
			description='''Resistance (real part of impedance).''',
			profiles=[]
		)
		self.register_property(
			name='x0',
			class_type=float,
			multiplier=UnitMultiplier.none,
			unit=UnitSymbol.ohm,
			description='''Reactance (imaginary part of impedance), at rated frequency.''',
			profiles=[]
		)
