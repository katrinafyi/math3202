from gurobipy import * 

from collections import namedtuple

TableSpec = namedtuple('TableSpec', 'title header format generator')

r = lambda i: round(i, 4)
row_generator = {
    'constraints': TableSpec(
        'Constraint Analysis', 
        ('constr', '', 'rhs', 'slack', 'pi', 'rhs low', 'rhs high'),
        '  {:>1} {:>5} | {:>6} {:>6} | {:>7} {:>7}', 
        lambda n, c: (n, c.sense, r(c.rhs), r(c.slack), r(c.pi), r(c.SARHSLow), r(c.SARHSUp))
    ),
    'variables': TableSpec(
        'Variable Analysis', 
        ('variable', 'x', 'coeff', 'rc', 'obj low', 'obj high'),
        '  = {:>5} * {:>6} | {:>6} | {:>7} {:>7}', 
        lambda n, c: (c.varName, r(c.x), r(c.obj), r(c.rc), r(c.SAObjLow), r(c.SAObjUp))),
}

def _dict_to_rows(constrs_list, generator, prefix=''):
    if not isinstance(constrs_list, dict):
        return [generator(prefix, constrs_list)]
    if prefix:
        p = prefix + ' '
    else:
        p = ''
    out = []
    for k, v in constrs_list.items():
        rows = _dict_to_rows(v, generator, p+str(k))
        out.extend(rows)
    return out

def _print_analysis(constr_dict, mode):
    rows = _dict_to_rows(constr_dict, row_generator[mode].generator)
    max_lens = []
    for i in range(len(rows[0])):
        this_max_len = max(map(lambda a: len(str(a)), (r[i] for r in rows)))
        if i > 0:
            this_max_len = min(this_max_len, 10)
        max_lens.append(this_max_len)
    
    # f_str_list = list(map(lambda l: f'{{:>{l}}}', max_lens))
    # f_str_list[0] = f'{{:>{max_lens[0]}}}'
    # f_str_list[1] = '{:2}'
    
    f_str = f'{{:>{max_lens[0]}}}' + row_generator[mode].format

    print(row_generator[mode].title)
    print(f_str.format(*row_generator[mode].header))
    for r in rows:
        # print(f_str)
        # print(r)
        print(f_str.format(*r))
    
def print_constr_analysis(constrs):
    return _print_analysis(constrs, 'constraints')

def print_variable_analysis(variables): 
    return _print_analysis(variables, 'variables')

if __name__ == "__main__":
    m = Model()
    x = m.addVar()
    c = m.addConstr(x*4 >= x, name='1')
    m.setObjective(x/2, GRB.MINIMIZE)
    m.optimize()
    print(m.getRow(c))

    print_constr_analysis({'a aaaaaaaaaaaaa': {'b': c}, 'x': c})
    print_variable_analysis({'a aaaaaaaaaaaaa': {'b': x}, 'x': x})