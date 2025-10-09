def solution(record):
    answer = []
    name_match = dict()
    for rec in record:
        parts = rec.split()
        act = parts[0]
        if act in ('Enter', 'Change'):
            id, name = parts[1], parts[2]
            name_match[id] = name_match.get(id, 'name')
            name_match[id] = name
    
    for rec in record:
        parts = rec.split()
        act = parts[0]
        if act == 'Enter':
            id = parts[1]
            answer.append(f'{name_match[id]}님이 들어왔습니다.')
        elif act == 'Leave':
            id = parts[1]
            answer.append(f'{name_match[id]}님이 나갔습니다.')
                
    return answer