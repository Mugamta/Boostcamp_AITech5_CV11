import collections

def solution(tickets):
    tickets.sort(key = lambda x:x[1], reverse = True)
    dic = collections.defaultdict(list)
    for i in tickets:
        dic[i[0]].append(i[1])
    answer = []
    path = ["ICN"]
    while path:
        if not dic[path[-1]] or path[-1] not in dic:
            answer.append(path.pop())
        else:
            path.append(dic[path[-1]].pop())
    return answer[::-1]