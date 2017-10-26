import objgraph

if __name__ == "__main__":
    max_size = 1212345
    objgraph.show_backrefs(
        max_size, 
        filename='sample-backref-graph.png'
    )

