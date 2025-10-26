#!/usr/bin/env python3
import argparse
import sys
from trans import trans, vhdl

def error(i):
    print(i)

def splitting(text, spliter):
    if len(spliter)>0:
        text=text.split(spliter[0])
        if len(spliter)>1:
            for i in spliter[1:]:
                text=[j.split(i) for j in text]
    return text

def getdefinition(line,index):
    level=0
    for i in line:
        if i==' ':level+=0.25
        elif i=='\t': level+=1
        else: break 
    if level!=int(level):error(f'###############################################invalid definition level at line {index}')
    return int(level)

def split_blocks(text, verbose=False):
    i=-1
    lines=[]
    text=text.split('\n')
    if verbose:
        print('lines num',len(text))
    running = True
    while running:
        line_type=None
        i+=1
        defined=False
        line_defin=getdefinition(text[i],i)
        next_defin=getdefinition(text[i+1],i+1) if i+1<len(text) else -1
        def_keys={'if':'condition' , 'for':'for_loop', 'while':'while_loop','entity':'entity' ,'process':'process','func':'func'}#item with definition block
        keys={'=':'equation','import':'loading','return':'end','beark':'bearking'}
        if i!=0:
            if line_defin>=prev_defin+2:
                error(f'invalid definition level at line {i}')
        if ((next_defin>-1) and (next_defin==line_defin+1)) or (text[i].strip().endswith(':')):
            defined = True
            if i==len(text)-1:
                error(f'excpected definition block after line {i}')
            elif line_defin!=getdefinition(text[i+1],i+1)-1:
                error(f'excpected definition block after line {i}')
            for key in def_keys:
                if key in text[i]:
                    line_type=def_keys[key]
                    break
        for key in keys:
            if key in text[i]:
                line_type=keys[key]
                if line_type=="loading":text[i]=text[i]+'.all'
                break
        prev_defin=line_defin
        lines.append({'level':line_defin,'index':i,'text':text[i],'type':line_type, 'defined':defined})
        if i+1==len(text):
            break
        if verbose:
            print('spliting')
    return lines

def blockize(lines, verbose=False):
    def_keys_count= {'condition': 0, 'for_loop': 0, 'while_loop': 0,
                                      'entity': 0, 'process': 0,'func':0}
    blocks= {'condition': {}, 'for_loop': {}, 'while_loop': {}, 'entity': {}, 'process':{},'func':{}}
    for i in range(len(lines)-1):
        if verbose:
            print('blockizing,working with : ',lines[i]['text'])
        if lines[i]['defined']:
            if 'name' not in lines[i].keys():
                lines[i]['name']=lines[i]['type']+str(def_keys_count[lines[i]['type']])
                def_keys_count[lines[i]['type']]+=1
            inside = True
            lines[i]['childs']=[]
            index=lines[i]['index']
            while inside:
                if verbose:
                    print('text:',lines[i]['text'],'/index is:',index)
                index+=1
                if verbose:
                    print(f'i:{i},index:{index}')
                
                if lines[index]['level']==lines[i]['level']+1:
                    if not lines[index]['defined']:lines[i]['childs'].append(index)
                    else:
                        if 'name' not in lines[index].keys():
                            lines[index]['name']=lines[index]['type']+str(def_keys_count[lines[index]['type']])
                            def_keys_count[lines[index]['type']]+=1
                            lines[i]['childs'].append(index)
                if lines[index]['level']<=lines[i]['level']: 
                    break
                if index>=len(lines)-2:
                    break
    return lines

def main():
    parser = argparse.ArgumentParser(description='PYHDL - Python to VHDL converter')
    parser.add_argument('input', help='Input file', type=str)
    parser.add_argument('output', help='Output file', type=str, default='out.vhd', nargs='?')
    parser.add_argument('package', help='Package file', type=bool, default=False, nargs='?')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    args = parser.parse_args()
    
    fname = args.input
    output = args.output
    verbose = args.verbose
    package = args.package
    
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            code = f.read()
        
        result = vhdl(trans(blockize(split_blocks(code, verbose), verbose), verbose), verbose)
        
        with open(output, 'w', encoding='utf-8') as f:
            f.write(result)
        
        print(f'Successfully converted {fname} to {output}')
        
    except FileNotFoundError:
        print(f'Error: File {fname} not found')
        sys.exit(1)
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()
