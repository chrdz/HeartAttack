import argparse
import yaml

parser=argparse.ArgumentParser()
parser.add_argument('--EPI',help='Epicardial parameters (default)',action="store_true")
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

with open('config.yml','r') as stream:
    try:
        param=yaml.load(stream)
    except yaml.YAMLError as err:
        print(err)

uo=param[var_type]['uo']
uu=param[var_type]['uu']
thetav=param[var_type]['thetav']
thetaw=param[var_type]['thetaw']
thetamv=param[var_type]['thetamv']
thetao=param[var_type]['thetao']
taumv1=param[var_type]['taumv1']
taumv2=param[var_type]['taumv2']
taupv=param[var_type]['taupv']
taumw1=param[var_type]['taumw1']
taumw2=param[var_type]['taumw2']
kmw=param[var_type]['kmw']
umw=param[var_type]['umw']
taupw=param[var_type]['taupw']
taufi=param[var_type]['taufi']
tauo1=param[var_type]['tauo1']
tauo2=param[var_type]['tauo2']
tauso1=param[var_type]['tauso1']
tauso2=param[var_type]['tauso2']
kso=param[var_type]['kso']
uso=param[var_type]['uso']
taus1=param[var_type]['taus1']
taus2=param[var_type]['taus2']
ks=param[var_type]['ks']
us=param[var_type]['us']
tausi=param[var_type]['tausi']
tauwinf=param[var_type]['tauwinf']
wainf=param[var_type]['wainf']
