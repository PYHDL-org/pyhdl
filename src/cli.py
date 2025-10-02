import argparse
args=argparse.ArgumentParser()
args.add_argument("input",help="Input file",type=str)
args.add_argument("output",help="Output file",type=str,default="out.vhd")
args.add_argument("package",help="Package file",type=bool,default=False)
args.add_argument("--verbose",action="store_true",help="Enable verbose output")
args=args.parse_args()
fname=args.input
code=open(fname,'r',encoding='utf-8').read()
V=args.verbose
package=args.package
outname=args.output
