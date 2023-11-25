def calculate_safe_sequence(available, alloc, max_req, n_processes, n_resources):
    safe_sequence = []
    finished = [False] * n_processes
    while True:
        all_finished = True
        for i in range(n_processes):
            if not finished[i]:
                all_finished = False
                break
        if all_finished:
            break

        work = [False] * n_resources
        for i in range(n_resources):
            if available[i] >= max_req[i][i]:
                work[i] = True
        if all(value is False for value in work):
            return "No Solution"

        for i in range(n_processes):
            if not finished[i]:
                if all(available[j] >= alloc[i][j] for j in range(n_resources)):
                    safe_sequence.append(i)
                    available = [available[j] + alloc[i][j] for j in range(n_resources)]
                    finished[i] = True
                break
    return safe_sequence

if type(safe_sequence) == str:
    print(safe_sequence)
else:
    print("Safe sequence is: ", safe_sequence)
