[ P a r a m e t e r s ]
icntl    =           0     # (D=0) 3:ECH 5:NOR 6:SRC 7,8:GSH 11:DSH 12:DUMP
itall    =           1     # (D=0) 0:no tally at batch, 1:same, 2:different
maxcas   =       50000     # (D=10) number of particles per one batch
maxbch   =       10000    # (D=10) number of batches
dmax(2)  =  20.0000000     # (D=emin(2)) data max. energy of neutron (MeV)
emin(2)  = 1.000000000     # (D=1.0) cut-off energy of neutron (MeV)
file(6)  = phits.out       # (D=phits.out) general output file name
#
# set correct path for nuclear and photon data files !!!
#
# file(7)  = /PATH/TO/PHITS/phits/data/xsdir.jnd # (D=xdirs) nuclear data input file name
# file(14) = /PATH/TO/PHITS/phits/data/trxcrd.dat # (D=trxcrd.dat) photon data input file name
inclg    =           2     # (D=1) 0:no, 1:INCL for p,n,pi,d,t,3He,alpha, 2:p,n,pi only
icrhi    =           0     # (D=1) 0: Shen, 1: NASA, 2: KUROTAMA
icxsni   =           0     # (D=0) 0: Pearlstein-Niita, 1: KUROTAMA, 2: Sato
ismm     =           0     # (D=0) 0: no, 1: Activate statistical multi-fragmentation
e-mode   =           1     # event generator activated
