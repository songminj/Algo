def solution(weights):
    answer = 0
    
    weight_counts = {}
    for w in weights:
        weight_counts[w] = weight_counts.get(w, 0) +1 

    unique_weights = list(weight_counts.keys())

    for w in unique_weights:
        count = weight_counts[w]
        
        if count > 1:
            answer += count * (count - 1) // 2
        
        if (w * 3) % 2 == 0:
            target = (w * 3) // 2
            if target in weight_counts:
                answer += count * weight_counts[target]
        
        target = w * 2
        if target in weight_counts:
            answer += count * weight_counts[target]
            
        if (w * 4) % 3 == 0:
            target = (w * 4) // 3
            if target in weight_counts:
                answer += count * weight_counts[target]
                
    return answer