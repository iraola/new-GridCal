# GridCal
# Copyright (C) 2015 - 2024 Santiago Peñate Vera
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
import numpy as np
import scipy.sparse as sp
import GridCalEngine.Topology.topology as tp
from GridCalEngine.basic_structures import Vec, CxVec, IntVec, StrVec


class ShuntData:
    """
    ShuntData
    """

    def __init__(self, nelm: int, nbus: int):
        """
        Shunt data arrays
        :param nelm: number of shunts
        :param nbus: number of buses
        """
        self.nelm: int = nelm
        self.nbus: int = nbus

        self.names: StrVec = np.empty(nelm, dtype=object)
        self.idtag: StrVec = np.empty(nelm, dtype=object)

        self.active: IntVec = np.zeros(nelm, dtype=bool)
        self.admittance: CxVec = np.zeros(nelm, dtype=complex)

        # reliabilty
        self.mttf: Vec = np.zeros(nelm, dtype=float)
        self.mttr: Vec = np.zeros(nelm, dtype=float)

        self.C_bus_elm: sp.lil_matrix = sp.lil_matrix((nbus, nelm), dtype=int)

        self.original_idx: IntVec = np.zeros(nelm, dtype=int)

    def size(self) -> int:
        """
        Get size of the structure
        :return:
        """

        return self.nelm

    def slice(self, elm_idx: IntVec, bus_idx: IntVec) -> "ShuntData":
        """
        Slice shunt data by given indices
        :param elm_idx: array of branch indices
        :param bus_idx: array of bus indices
        :return: new ShuntData instance
        """

        data = ShuntData(nelm=len(elm_idx), nbus=len(bus_idx))

        data.names = self.names[elm_idx]
        data.idtag = self.idtag[elm_idx]

        data.active = self.active[elm_idx]
        data.admittance = self.admittance[elm_idx]

        data.mttf = self.mttf[elm_idx]
        data.mttr = self.mttr[elm_idx]

        data.C_bus_elm = self.C_bus_elm[np.ix_(bus_idx, elm_idx)]

        data.original_idx = elm_idx

        return data

    def copy(self) -> "ShuntData":
        """
        Get deep copy of this structure
        :return: new ShuntData instance
        """

        data = ShuntData(nelm=self.nelm, nbus=self.nbus)

        data.names = self.names.copy()
        data.idtag = self.idtag.copy()
        data.active = self.active.copy()
        data.admittance = self.admittance.copy()

        data.mttf = self.mttf.copy()
        data.mttr = self.mttr.copy()

        data.C_bus_elm = self.C_bus_elm.copy()

        data.original_idx = self.original_idx.copy()

        return data

    def get_island(self, bus_idx: IntVec):
        """
        Get the array of shunt indices that belong to the islands given by the bus indices
        :param bus_idx: array of bus indices
        :return: array of island branch indices
        """
        if self.nelm:
            return tp.get_elements_of_the_island(
                C_element_bus=self.C_bus_elm.T,
                island=bus_idx,
                active=self.active,
            )
        else:
            return np.zeros(0, dtype=int)

    def get_array_per_bus(self, arr: Vec) -> Vec:
        """
        Get generator array per bus
        :param arr:
        :return:
        """
        assert len(arr) == self.nelm
        return self.C_bus_elm @ arr

    def get_injections_per_bus(self) -> CxVec:
        """
        Get Injections per bus
        :return:
        """
        return self.C_bus_elm * (self.admittance * self.active)

    def __len__(self) -> int:
        return self.nelm

    def get_bus_indices(self) -> IntVec:
        """
        Get the bus indices
        :return: array with the bus indices
        """
        return tp.get_csr_bus_indices(self.C_bus_elm.tocsr())
