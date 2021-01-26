#!/usr/bin/env python3
"""Generate random sets of Sobol sequence numbers (or uniform). Graham L Giller"""
from sys import stderr,stdout,version_info
from sobol_seq import i4_sobol as sobol
from random import uniform

def main():
    # arguments
    from argparse import ArgumentParser;
    args=ArgumentParser();
    args.add_argument("-u","--uniform",action='store_true',help="Set to generate uniform random numbers not Sobol sequence.")
    args.add_argument("-d","--dimension",type=int,default=2,help="Dimensionality.")
    args.add_argument("-n","--number",type=int,default=100,help="Sample size.")
    args=args.parse_args();

    # basic loop
    n,seed=args.number,1
    
    while n>0:
        if args.uniform:
            vector=[uniform(0,1) for i in range(args.dimension)]

        else:
            vector,seed=sobol(args.dimension,seed)
            
        print(",".join(map(str,vector)))
        n-=1

# bootstrap
if __name__ == "__main__":
    assert(version_info.major>=3)
    main()
