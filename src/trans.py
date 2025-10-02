from cli import V

class entity:
    def __init__(self, line, name, ins, outs, architecture):
        self.name = name
        self.line = line
        self.ins = ins
        self.outs = outs
        self.architecture = architecture

    def pins(self):
        # Expect ins/outs as list of tuples: (name, type)
        ins_ports = [f"{name}: in {typ};" for name, typ in self.ins]
        out_ports = [f"{name}: out {typ};" for name, typ in self.outs]
        return ('\n' + ' ' * 4).join(ins_ports + out_ports)[:-1]

    def pre(self):
        return f"entity {self.name} is\n    port(\n    {self.pins()}\n    );\nend entity {self.name};\n"

    def __str__(self):
        return f"architecture {self.name}Arch of {self.name} is\n    begin\n" + \
               '\n'.join([str(i['processed']) for i in self.architecture]) + \
               f"\nend architecture {self.name}Arch;\n"

class cond:
    def __init__(self, line, child):
        self.line = line
        self.child = child

    def __str__(self):
        # Replace ':' with 'then' for VHDL if statements
        return self.line['text'].replace(':', ' then') + '\n' + \
               '\n'.join([str(i['processed']) for i in self.child]) + \
               '\n' + ' ' * 4 * int(self.line['level']) + 'end if;'

class while_loop:
    def __init__(self, line, child):
        self.line = line
        self.child = child

    def __str__(self):
        return self.line['text'] + '\n' + \
               '\n'.join([str(i['processed']) for i in self.child]) + \
               '\n' + ' ' * 4 * int(self.line['level']) + 'end loop;'

class func:
    def __init__(self, Name, returned_type, child, ins):
        self.name = Name
        self.returned_type = returned_type
        self.child = child
        self.ins = ins

    def upper(self):
        return f"function {self.name}({self.ins}) return {self.returned_type} is\n    begin\n"

    def lower(self):
        text = ''
        for i in self.child:
            text += i['processed'] + '\n'
        return text

    def __str__(self):
        return self.upper() + self.lower() + "end function;\n"

class for_loop:
    def __init__(self, name, level, iter_var_name, iterable, children):
        self.name = name
        self.iter_var_name = iter_var_name
        self.iterable = iterable
        self.children = children
        self.level = level

    def __str__(self):
        indent = ' ' * 4 * int(self.level)
        string = indent + f"{self.name}: for {self.iter_var_name} in {self.iterable} loop\n"
        for i in self.children:
            string += i['processed'] + '\n'
        string += indent + "end loop;\n"
        return string

class process:
    def __init__(self, line, child):
        self.line = line
        self.child = child

    def __str__(self):
        return self.line['text'].replace(':', '') + '\n' + \
               ('\n' + ' ' * 4 * (self.line['level'] + 1)).join([str(i['processed']) for i in self.child]) + \
               '\n' + ' ' * 4 * int(self.line['level']) + 'end process;\n'

def trans(lines):
    replaces = [
        {'key': 'equation', 'old': '=', 'new': '<='},
        {'key': 'loading', 'old': 'import ', 'new': 'use work.'}
    ]
    for i in range(len(lines)):
        if not lines[i]['defined']:
            if V: print('processing')
            lineType = lines[i]['type']
            for j in replaces:
                if lineType == j['key']:
                    if V: print('replacing')
                    lines[i]['processed'] = lines[i]['text'].replace(j['old'], j['new']) + ';'
            if 'processed' not in lines[i].keys():
                lines[i]['processed'] = lines[i]['text'] + ';'
        else:
            if lines[i]['type'] == 'condition':
                lines[i]['processed'] = trans_condition(lines[i], [lines[j] for j in lines[i]['childs']])
            elif lines[i]['type'] == 'func':
                lines[i]['processed'] = trans_fanc(lines[i], [lines[j] for j in lines[i]['childs']])
            elif lines[i]['type'] == 'for_loop':
                lines[i]['processed'] = trans_for_loop(lines[i], lines[i]['level'], [lines[j] for j in lines[i]['childs']])
            elif lines[i]['type'] == 'while_loop':
                lines[i]['processed'] = trans_while_loop(lines[i], [lines[j] for j in lines[i]['childs']])
            elif lines[i]['type'] == 'entity':
                lines[i]['processed'] = trans_entity(lines[i], [lines[j] for j in lines[i]['childs']])
            elif lines[i]['type'] == 'process':
                lines[i]['processed'] = trans_process(lines[i], [lines[j] for j in lines[i]['childs']])
    return lines

def vhdl(lines):
    vhdlCode = ''
    for i in lines:
        if V: print("working with element:", i)
        if i['level'] == 0:
            vhdlCode += str(i['processed']) + '\n'
        if i['type'] == 'entity':
            vhdlCode = i['processed'].pre() + vhdlCode
    return vhdlCode

def trans_for_loop(line, level, child):
    text = line['text'].split()
    loop_var = text[text.index('for') + 1]
    iterable = text[text.index('in') + 1]
    if V: print(f'for line {line["text"]}: iterable={iterable}, loop_var={loop_var}')
    return for_loop(line['name'], level, loop_var, iterable, child)

def trans_condition(line, child):
    return cond(line, child)

def trans_process(line, child):
    return process(line, child)

def trans_fanc(line, child):
    Name = line['name']
    text = line['text']
    ins = text[text.index('(') + 1:text.index(')')]
    returned_type = text.split()[-2]
    print('\n' * 2, 'Names:', Name, ',ins: ', ins, ', return :', returned_type, '\n' * 2)
    return func(Name, returned_type, child, ins)

def trans_while_loop(line, child):
    return while_loop(line, child)

def trans_entity(line, child):
    text = line['text']
    name = text.split()[1]
    # Expect ins/outs as list of tuples: (name, type)
    ins = [tuple(pin.split(':')) for pin in text[text.index('(') + 1:text.index(')')].split(',')]
    out = [tuple(pin.split(':')) for pin in text.split()[-2].split(',')]
    return entity(line, name, ins, out, child)
