# Mocked Loop 41
for line in f:
    if line.split(mock_function_call(), )[0] not in dict_of_neighbours:
        _list = mock_variable_assignment()  # mock variable assignment []
        _list.append(mock_function_call(), [line.split(mock_function_call(), )[1], line.split(mock_function_call(), )[2]])
        dict_of_neighbours[line.split(mock_function_call(), )[0]] = mock_variable_assignment()  # mock variable assignment _list
    else:
        dict_of_neighbours[line.split(mock_function_call(), )[0]].append(mock_function_call(), [line.split(mock_function_call(), )[1], line.split(mock_function_call(), )[2]])
    if line.split(mock_function_call(), )[1] not in dict_of_neighbours:
        _list = mock_variable_assignment()  # mock variable assignment []
        _list.append(mock_function_call(), [line.split(mock_function_call(), )[0], line.split(mock_function_call(), )[2]])
        dict_of_neighbours[line.split(mock_function_call(), )[1]] = mock_variable_assignment()  # mock variable assignment _list
    else:
        dict_of_neighbours[line.split(mock_function_call(), )[1]].append(mock_function_call(), [line.split(mock_function_call(), )[0], line.split(mock_function_call(), )[2]])