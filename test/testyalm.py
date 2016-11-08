#!/usr/bin/env python3

import yaml
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--EPI',help='Epicardial parameters',action="store_true")
parser.add_argument('--ENDO',help='Endocardial parameters',action="store_true")
parser.add_argument('--M',help='Midmyocardial parameters',action="store_true")
parser.add_argument('--PB',help='Priebe and Beuckelmann parameters',action="store_true")
parser.add_argument('--TNNP',help='Tusscher-Noble-Noble-Panfilov parameters',action="store_true")
args=parser.parse_args()

if args.ENDO:
    var_type='ENDO'
elif args.M:
    var_type='M'
elif args.PB:
    var_type='PB'
elif args.TNNP:
    var_type='TNNP'
else:
    var_type='EPI'

var=yaml.load(open('config.yml','r'))

print(var[var_type]['thetamw'])
