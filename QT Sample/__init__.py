import os,sys
import argparse
import logging
loglevel=logging.INFO
#Version
__version__ = 0.01

#Command Line Arguments
parser = argparse.ArgumentParser(description='Filmmmh Image Utilty',epilog='Image Editing Tool')

parser.add_argument('--version','-v',dest='version',action='store_true',
                   help='return the version')
                   
args, unknown = parser.parse_known_args()

if args.version:
    print(__version__)
    exit()

#Logging
logpath='filmmmh.log'
logging.basicConfig(filename=logpath, level=loglevel, format='%(asctime)s\t[%(levelname)s]\t%(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info("Started")