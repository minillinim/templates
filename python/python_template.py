#!/usr/bin/env python3

#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__maintainer__ = 'Michael Imelfort'
__script_name__ = 'NAME ME'
__version__ = '0.0.1'
__profiling__ = 'False'

import argparse
import sys

#import numpy as np
#np.seterr(all='raise')

def do_work( args ):

    '''
    # run something external using a thread pool

    from multiprocessing import Pool
    from subprocess import Popen, PIPE

    def run_command(cmd):
        # expects 'cmd' to be a string like 'foo -b ar'
        p = Popen(cmd.split(' '), stdout=PIPE)
        return p.communicate()

    num_threads = __choose__

    pool = Pool(num_threads)
    cmds = ['ls -l', 'ls -alh', 'ps -ef']
    print(pool.map(run_command, cmds))
    '''

    '''
    # parse a file
    try:
        with open(args.filename, 'r') as fh:
            for line in fh:
                print(line)
    except:
        print('Error opening file: %s - %s' % (args.filename, sys.exc_info()[0]))
        raise
    '''

    '''
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    fig = plt.figure()

    points = __somepoints__

    # make a 3d plot
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:,0],
               points[:,1],
               points[:,2],
               #edgecolors='none',
               #c=colors,
               #s=2,
               #marker='.'
               )

    # make a 2d plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(points[:,0],
            points[:,1],
            '*g')

    # show or save figure
    filename = __filename__
    plt.show()
    plt.savefig(filename, dpi=300, format='png')

    # clean up
    plt.close(fig)
    del fig
    '''

    return 0

###############################################################################

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Input file to parse')
    #parser.add_argument('positional_arg', help='Required')
    #parser.add_argument('positional_arg2', type=int, help='Integer argument')
    #parser.add_argument('positional_arg3', nargs='+', help='Multiple values')
    #parser.add_argument('-X', '--optional_X', action='store_true', default=False, help='flag')

    #-------------------------------------------------
    # get and check options
    args = None
    if(len(sys.argv) == 1):
        parser.print_help()
        sys.exit(0)
    elif(sys.argv[1] == '-v' or \
         sys.argv[1] == '--v' or \
         sys.argv[1] == '-version' or \
         sys.argv[1] == '--version'):
        print('%s: version: %s' % (__script_name__, __version__))
        sys.exit(0)
    elif(sys.argv[1] == '-h' or \
         sys.argv[1] == '--h' or \
         sys.argv[1] == '-help' or \
         sys.argv[1] == '--help'):
        parser.print_help()
        sys.exit(0)
    else:
        args = parser.parse_args()

    try:
        if(__profiling__):
            import cProfile
            import pstats
            cProfile.run('do_work(args)', 'prof')
            p = pstats.Stats('prof')
            p.sort_stats('cumulative').print_stats(10)
            p.sort_stats('time').print_stats(10)
        else:
            do_work(args)
    except:
        print('Unexpected error:', sys.exc_info()[0])
        raise
