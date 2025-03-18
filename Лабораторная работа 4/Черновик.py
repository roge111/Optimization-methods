def select_candidates(candidate_strings):
    result = []
    hash_data = {}
    for candidate in candidate_strings:
        candidate_data = candidate.split(',')
        mark = 0
        

        for i in range(1, len(candidate_data)):
            mark += int(candidate_data[i])
        mark = mark/(len(candidate_data) - 1)


        if mark >= 5: 
            if mark not in hash_data:
                hash_data[mark] = [candidate_data[0]]
            else:
                hash_data[mark].append(candidate_data[0])

    mark_sort = sorted(hash_data)[::-1]

    for mark in mark_sort:
        data = hash_data.sort()
        for people in data:
            result.append(f"{people},{mark}")
    return result




lines = []
while True:
   try:
      line = input()
      if line == "":
         break
   except EOFError:
      break
   lines.append(line)


for candidate in select_candidates(lines):
   print(candidate)
