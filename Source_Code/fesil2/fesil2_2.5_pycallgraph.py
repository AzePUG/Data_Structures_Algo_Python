from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

def print_func(n):
    if n == 0: # funksiyanı bitirən əsas hal.
        return 0
    elif n > 0:
        print(n)
        return print_func(n - 1) # rekursiv çağırış


if __name__ == "__main__":
    graphviz = GraphvizOutput()
    graphviz.output_file = 'fesil2_2.5.png'

    with PyCallGraph(output=graphviz):    
        print_func(4)
