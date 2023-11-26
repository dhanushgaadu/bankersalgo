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
k=int(input("enter number of processes :"))
print("Your selected processes are :")
for e in range(0,k):
        print("P"+str(e))
allc=[]
maxi=[]
avl=[]
abc=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n=int(input("\nEnter number of resources :"))
print("\n\nEnter allocations\n\n")
for i in range(k):
    m=[]
    o=0
    for k in range(n):
        a=int(input("\nEnter value of "+abc[o]+" :"))
        o+=1
        m.append(a)
    allc.append(m)
    print("\n\nallocations:"+str(allc))
print('\n\nenter maximum\n\n')
for i in range(k):
    m=[]
    o=0
    for k in range(n):
        a=int(input("\nEnter value of "+abc[o]+" :"))
        o+=1
        m.append(a)
    maxi.append(m)
    print("\n\nmaximum resources are :"+str(maxi))
print("\n\nEnter available\n\n")
o=0
for k in range(n):
        a=int(input("\nEnter value of "+abc[o]+" :"))
        o+=1
        avl.append(a)
print("\n\navailable resouces are :"+str(avl))
safe_sequence = calculate_safe_sequence(avl, allc, maxi, k, n)

if type(safe_sequence) == str:
    print(safe_sequence)
else:
    print("Safe sequence is: ", safe_sequence)
