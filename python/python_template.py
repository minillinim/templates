#!/usr/bin/env python

__script_name__ = "NAME ME"
__version__ = "0.0.1"
__maintainer__ = "Michael Imelfort"
__email__ = "mike@mikeimelfort.com"
__status__ = "Development"

import argparse
import sys

#from multiprocessing import Pool
#from subprocess import Popen, PIPE

#import os
#import errno

#import numpy as np
#np.seterr(all='raise')

#import matplotlib as mpl
#import matplotlib.pyplot as plt

def run_command(cmd):
    """Run a command and take care of stdout

    expects 'cmd' to be a string like "foo -b ar"

    returns (stdout, stderr)
    """
    p = Popen(cmd.split(' '), stdout=PIPE)
    return p.communicate()

def do_work( args ):
    """ Main wrapper"""

    """
    # run something external using a thread pool
    pool = Pool(6)
    cmds = ['ls -l', 'ls -alh', 'ps -ef']
    print pool.map(run_command, cmds)
    """

    """
    # parse a file
    try:
        with open(args.filename, "r") as fh:
            for line in fh:
                print line
    except:
        print "Error opening file:\"", args.filename, "\", sys.exc_info()[0]
        raise
    """

    """
    fig = plt.figure()

    #-----
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

    #-----
    # make a 2d plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(points[:,0],
            points[:,1],
            '*g')

    #-----
    # show figure
    plt.show()
    # or save figure
    plt.savefig(filename,dpi=300,format='png')

    #-----
    # clean up!
    plt.close(fig)
    del fig
    """

    return 0

###############################################################################

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help="Input file to parse")
    #parser.add_argument('positional_arg', help="Required")
    #parser.add_argument('positional_arg2', type=int, help="Integer argument")
    #parser.add_argument('positional_arg3', nargs='+', help="Multiple values")
    #parser.add_argument('-X', '--optional_X', action="store_true", default=False, help="flag")

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
        print "%s: version: %s" % (__script_name__, __version__)
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
            cProfile.run('do_work(args)', 'prof')
            ##########################################
            ##########################################
            # Use this in python console!
            #import pstats
            #p = pstats.Stats('prof')
            #p.sort_stats('cumulative').print_stats(10)
            #p.sort_stats('time').print_stats(10)
            ##########################################
            ##########################################
        else:
            do_work(args)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

