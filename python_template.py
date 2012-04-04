#!/usr/bin/env python
###############################################################################
#
#    __Script__Name__
#    
#    <one line to give the program's name and a brief idea of what it does.>
#
#    Copyright (C) 2012 Michael Imelfort
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from optparse import OptionParser
import sys
from pprint import pprint

###############################################################################
# CODE HERE
###############################################################################

def doWork( options ):
    return 0

###############################################################################
# TEMPLATE SUBS
###############################################################################
#
# Entry point, parse command line args and call out to doWork
#
if __name__ == '__main__':
    # intialise the options parser
    parser = OptionParser("\n\n %prog [options]")
    
    # add options here:
    #parser.add_option("-f", "--frog", action="store_true", dest="frog", default=False, help="Is this a frog? [default: false]")
    #parser.add_option("-c", "--cat", dest="cat", default=16, help="The cat's age? [default: 16")
    
    # get and check options
    (opts, args) = parser.parse_args()
    
    #
    # compulsory opts
    #
    #if (opts.frog is None ):
    #    print ("**ERROR: %prog : No frog!")
    #    parser.print_help()
    #    sys.exit(1)
    
    # 
    # do what we came here to do
    #
    doWork(opts)