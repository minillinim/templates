#!/usr/bin/env python

#=======================================================================
# Author:
#
# Unit tests.
#
# Copyright
#
# This is free software: you can redistribute it and/or modify
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
import subprocess
import tempfile
import os.path


class Tests(unittest.TestCase):
  def testSomething(self):
    bamOutputFile = '/tmp/a'+'.bam'
    subprocess.check_call(path_to_script+' -1 data/reads.1.fq.gz -2 data/reads.2.fq.gz -d data/ref.fna -b '+bamOutputFile, shell=True)

    samOutput = subprocess.check_output('samtools view '+bamOutputFile, shell=True)

    expectedSamOutput = 'FCC0WM1ACXX:2:2106:7087:17037#TATCCAGA	89	E1D_contig_2582764	1477	37	100M	=	1477	0	GCAGTCACTGCACCGCAAGGAAGCACAGAACCTGCAATGATATTTCACATCGTGGGACTTAAATATCTTTTGGCATTGTTCACACTTGGGCTTTTCCTTC	cccccbbccccaccdddeeeeeeggfgggchiihiiihihfhffihgiihihhgghhhfiiihiiiiiihiihfiiihiihgihiiigggggeeeeebbb	XT:A:U	NM:i:0	SM:i:37	AM:i:0	X0:i:1	X1:i:0	XM:i:0	XO:i:0	XG:i:0	MD:Z:100'+"\n"
    expectedSamOutput += 'FCC0WM1ACXX:2:2308:9246:128896#TATCCAGA	89	E1D_contig_3	23	37	100M	=	23	0	AATACAACGGAATCCGCTTTCTCCCGCTGAAGCTGGGACGCTGGCTTAACGACTTCGACGAATCTCAAAAACGCAACGTCGTCGTTCTCGGCGATGAGAT	ccccccccdccccccccb^Ta__accb_cbbabcaccacc_bbbbaccccb^cccccdeeeeeggeiihg`hiihgggaihhhiiihgfgggeeeeebbb	XT:A:U	NM:i:0	SM:i:37	AM:i:0	X0:i:1	X1:i:0	XM:i:0	XO:i:0	XG:i:0	MD:Z:100'+"\n"

    self.assertEqual(expectedSamOutput, samOutput)

    # Check the index exists also
    self.assertEqual(True, os.path.isfile(bamOutputFile+'.bai'))


if __name__ == "__main__":
	unittest.main()
