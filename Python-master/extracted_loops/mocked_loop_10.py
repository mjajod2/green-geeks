# Mocked Loop 10
while breadth_first_search(mock_function_call(), graph, source, sink, parent):
    path_flow = mock_variable_assignment()  # mock variable assignment int(mock_function_call(), 1000000000.0)
    s = mock_variable_assignment()  # mock variable assignment sink
    while s != mock_variable_assignment()  # mock variable assignment source:
        path_flow = mock_variable_assignment()  # mock variable assignment min(mock_function_call(), path_flow, graph[parent[s]][s])
        s = mock_variable_assignment()  # mock variable assignment parent[s]
    max_flow += mock_variable_assignment()  # mock variable assignment path_flow
    v = mock_variable_assignment()  # mock variable assignment sink
    while v != mock_variable_assignment()  # mock variable assignment source:
        u = mock_variable_assignment()  # mock variable assignment parent[v]
        graph[u][v] -= mock_variable_assignment()  # mock variable assignment path_flow
        graph[v][u] += mock_variable_assignment()  # mock variable assignment path_flow
        v = mock_variable_assignment()  # mock variable assignment parent[v]