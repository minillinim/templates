#!/usr/bin/env sh
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

# get opts
# 
# params with values are followed by a value "i:o:h" -> -i IN -o OUT or just -h
#
usage="Usage: $0 -<<add here>> [-h]"
no_opts=1
while getopts "<<add here>>h" o; do       
    case "$o" in
        h)  echo $usage; exit 1;;
        #i) infile=$OPTARG;;
    esac
done
if [ "$no_opts" -eq "1" ]
then
    echo $usage; exit 1
fi
# echo $infile
