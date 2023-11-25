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

# example usage
alloc = [[0, 1, 0],
         [2, 0, 0],
         [3, 0, 2],
         [2, 1, 1],
         [0, 0, 2]]

max_req = [[7, 5, 3],
           [3, 2, 2],
           [9, 0, 2],
           [2, 2, 2],
           [4, 3, 3]]

available = [10, 5, 7]

n_processes = 5
n_resources = 3

safe_sequence = calculate_safe_sequence(available, alloc, max_req, n_processes, n_resources)

if type(safe_sequence) == str:
    print(safe_sequence)
else:
    print("Safe sequence is: ", safe_sequence)
