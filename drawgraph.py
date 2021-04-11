import sys
from graphviz import Digraph

from bamscript import BAMCompile

def generate_graph(machine, name):
    dot = Digraph(comment='State Machine')
    for state, rules in machine.items():
        for rule, value in rules.items():
            dot.edge(str(state), str(value), label=rule)
    #display(Image(data=dot.pipe(format="png")))
    dot.render(name, format='png')

with open(sys.argv[1]) as fp:
    program = fp.read()

end_machine_code, main_machine_code = BAMCompile(program)
generate_graph(main_machine_code, "private")
generate_graph(end_machine_code, "general")
