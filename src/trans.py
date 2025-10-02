from cli import V
class entity:
    def __init__(self,line,name,ins,outs, architecture):#architecture
        self.name=name
        self.line=line
        self.ins=ins
        self.outs=outs
        self.architecture=architecture
    def pins(self):
        return ('\n'+' '*4).join([
                i.replace(':',': in ')+';' for i in self.ins
            ]+[
                i.replace(':',': out ')+';' for i in self.outs
            ])[:-1]
    def pre(self):
       return f'Etity {self.name} is \n    port(\n    {self.pins()}\n    );\nend Entity;\n'
    def __str__(self):
       return f'architecture {self.name}Arch of {self.name} is\n    begin\n'+'\n'.join([str(i['processed']) for i in self.architecture])\
               +f'\nend {self.name}Arch;\n'
class cond:
    def __init__(self,line,child):
        self.line=line
        self.child=child
    def __str__(self):
        return self.line['text'].replace(':' ,' then')+'\n'+''.join([str(i['processed']) for i in self.child])+'\n'+' '*4*int(self.line['level'])+'end if;'
class while_loop:
    def __init__(self,line,child):
        self.line=line
        self.child=child
    def __str__(self):
        return self.line['text']+'\n'+''.join([str(i['processed'])+'\n' for i in self.child])+\
          '\n'+' '*4*int(self.line['level'])+'end loop;'
class func:
    def __init__(self,Name,returned_type,child,ins):
        self.name=Name
        self.returned=returned_type
        self.returned_type=returned_type
        self.child=child
        self.ins=ins
    def _returned(self):
        return f'{self.returned_type}'
    def _ins(self):
        return f'{self.ins}'
    def upper(self):
        return f'Function {self.name}({self._ins()}) return {self._returned()} is\n    begin\n'
    def lower(self):
        text=''
        for i in self.child:
            text+=i['text']+'\n'
        return text
    def __str__(self):
        return self.upper()+self.lower()
class for_loop:
    def __init__(self,name,level,iter_var_name,iterable,children):
        self.name:str=name
        self.iter_var_name:str=iter_var_name
        self.iterable:object=iterable
        self.children:list=children
        self.level=level
    def __str__(self):
        string=''
        string+=int(self.level)*4*' '+f'{self.name}: for {" ".join(self.iter_var_name)} in {self.iterable} loop\n'
        for i in self.children:
            string+=i['processed']+'\n'
        string+=f'end loop {self.name}\n'
        return string
class process:
    def __init__(self,line,child):
        self.line=line
        self.child=child
    def __str__(self):
        return self.line['text'].replace(':','')+'\n     '+('\n    '*4*(self.line['level']+1)).join([str(i['processed']) for i in self.child])+'    '*(4*self.line['level'])+'\nend process;'
def trans(lines):
    replaces=[{'key':'equation','old':'=','new' :'<='},{'key':'loading','old':'import','new' :'use'}]
    for i in range(len(lines)):
        if not lines[i]['defined']:
            if V:print('processing')
            lineType=lines[i]['type']
            for j in replaces:
                if lineType==j['key']:
                    if V:print('replacing')
                    lines[i]['processed']=lines[i]['text'].replace(j['old'],j['new'])+';'
            if 'processed' not in lines[i].keys():
                lines[i]['processed']=lines[i]['text']+';'
        else:
            if lines[i]['type']=='condition':lines[i]['processed']=trans_condition(lines[i],[lines[j] for j in lines[i]['childs']])
            elif lines[i]['type']=='func':lines[i]['processed']=trans_fanc(lines[i],[lines[j] for j in lines[i]['childs']])###
            elif lines[i]['type']=='for_loop':lines[i]['processed']=trans_for_loop(lines[i],lines[i]['level'],[lines[j] for j in lines[i]['childs']])
            elif lines[i]['type']=='while_loop':lines[i]['processed']=trans_while_loop(lines[i],[lines[j] for j in lines[i]['childs']])
            elif lines[i]['type']=='entity':lines[i]['processed']=trans_entity(lines[i],[lines[j] for j in lines[i]['childs']])
            elif lines[i]['type']=='process':lines[i]['processed']=trans_process(lines[i],[lines[j] for j in lines[i]['childs']])
    return lines
def vhdl(lines):
    vhdlCode=''
    for i in lines:
        if V:print("working with element:",i)
        if i['level']==0 :vhdlCode +=str(i['processed'])+'\n'
        if i['type']=='entity':
            vhdlCode=i['processed'].pre()+vhdlCode 
    return vhdlCode
def trans_for_loop(line,level,child):
    text=line['text'].split()
    loop_var=text[text.index('for')+1:text.index('in')]
    iterable=line['text'][line['text'].index('in')+2:line['text'].index(':')]
    if V:print(f'for line {line["text"]}:iterable={iterable},,,,,loop_var={loop_var}')
    return for_loop(line['name'],level,loop_var,iterable,child)

def trans_condition(line,child):
    return cond(line,child)

def trans_process(line,child):
    return process(line,child)

def trans_fanc(line,child):
    Name=line['name']
    text=line['text']
    ins=text[text.index('(')+1:text.index(')')]
    returned_type=text.split()[-2]
    print('\n'*10,'Names:',Name,',ins: ',ins,', return :', returned_type,'\n'*5)
    return func(Name, returned_type,child,ins)
def trans_while_loop(line,child):
    return while_loop(line,child)
def trans_entity(line,child):
    text=line['text']
    name=text.split()[1]
    ins=text[text.index('(')+1:text.index(')')].split(',')
    out=text.split()[-2].split(',')
    return entity(line,name,ins,out,child)

