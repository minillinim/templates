#=======================================================================
# Author:
#
# Unit tests for STAMP.
#
# Copyright
#
# STAMP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License.
# If not, see <http://www.gnu.org/licenses/>.
#=======================================================================

import unittest
import sys


class VerifyPostHocTests(unittest.TestCase):
	def testGamesHowell(self):
		"""Verify computation of Games-Howell post-hoc test"""
		from plugins.multiGroups.postHoc.GamesHowell import GamesHowell
		gh = GamesHowell(preferences)

		# ground truth found with SPSS v19. Values are not exact since the critical Q value
		# are interpolated from tables in the STAMP implementation.
		pValues, effectSize, lowerCI, upperCI, labels, note = gh.run([[1,2,3,4,5],[10,20,30,40,50,60],[1,2,3,4,5,6,7]], 0.95, ['1', '2', '3'])
		self.assertEqual(labels[0], '1 : 2')
		self.assertAlmostEqual(effectSize[0], -32)
		self.assertAlmostEqual(lowerCI[0], -56.836534205367272) # SPSS = -56.80902338101632
		self.assertAlmostEqual(upperCI[0],  -7.163465794632728) # SPSS = -7.190976618983683
		self.assertEqual(pValues[0] == '< 0.02', True) # SPSS = 0.019165308600281317

if __name__ == "__main__":
	unittest.main()
