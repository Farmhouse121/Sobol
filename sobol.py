#!/usr/bin/env python3
"""Generate random pairs of Sobol sequence numbers (or uniform for contrast)."""
from sys import stderr,stdout,version_info
from sobol_seq import i4_sobol as sobol
from random import uniform

def main():
    # arguments
    from argparse import ArgumentParser;
    args=ArgumentParser();
    args.add_argument("mode",type=str,default="sobol",nargs='*',choices=['sobol','uniform'],help="Type of numbers to create.")
    args.add_argument("-d","--dimension",type=int,default=2,help="Dimensionality.")
    args.add_argument("-n","--number",type=int,default=100,help="Sample size.")
    args=args.parse_args();

    # basic loop
    n,seed=args.number,1
    
    while n>0:
        if args.mode=='sobol':
            vector,seed=sobol(args.dimension,seed)
            
        else:
            vector=[uniform(0,1) for i in range(args.dimension)]
            
        print(",".join(map(str,vector)))
        n-=1

# bootstrap
if __name__ == "__main__":
    assert(version_info.major>=3)
    main()