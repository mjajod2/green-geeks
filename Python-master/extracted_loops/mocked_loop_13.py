# Mocked Loop 13
while not search_end:
    current_score = mock_variable_assignment()  # mock variable assignment current_state.score(mock_function_call(), )
    if best_state is None or current_score > best_state.score(mock_function_call(), ):
        best_state = mock_variable_assignment()  # mock variable assignment current_state
    scores.append(mock_function_call(), current_score)
    iterations += mock_variable_assignment()  # mock variable assignment 1
    next_state = mock_variable_assignment()  # mock variable assignment None
    neighbors = mock_variable_assignment()  # mock variable assignment current_state.get_neighbors(mock_function_call(), )
    while next_state is None and neighbors:
        index = mock_variable_assignment()  # mock variable assignment random.randint(mock_function_call(), 0, len(mock_function_call(), neighbors) - 1)
        picked_neighbor = mock_variable_assignment()  # mock variable assignment neighbors.pop(mock_function_call(), index)
        change = mock_variable_assignment()  # mock variable assignment picked_neighbor.score(mock_function_call(), ) - current_score
        if picked_neighbor.x > max_x or picked_neighbor.x < min_x or picked_neighbor.y > max_y or (mock_function_call(), picked_neighbor.y < min_y):
            continue
        if not find_max:
            change = mock_variable_assignment()  # mock variable assignment change * -1
        if change > 0:
            next_state = mock_variable_assignment()  # mock variable assignment picked_neighbor
        else:
            probability = mock_variable_assignment()  # mock variable assignment math.e ** (mock_function_call(), change / current_temp)
            if random.random(mock_function_call(), ) < probability:
                next_state = mock_variable_assignment()  # mock variable assignment picked_neighbor
    current_temp = mock_variable_assignment()  # mock variable assignment current_temp - current_temp * rate_of_decrease
    if current_temp < threshold_temp or next_state is None:
        search_end = mock_variable_assignment()  # mock variable assignment True
    else:
        current_state = mock_variable_assignment()  # mock variable assignment next_state