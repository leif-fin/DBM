def manhattan_distance(p, q):
    return sum(abs(p_i - q_i) for p_i, q_i in zip(p, q))

def euclidean_distance(p, q):
    return sum((p_i - q_i) ** 2 for p_i, q_i in zip(p, q)) ** 0.5

# Assume that there are two points P(3,5) and Q(1,1)
P = (3, 5)
Q = (1, 1)

print("Manhattan distance:", manhattan_distance(P, Q))
print("Euclidean distance:", euclidean_distance(P, Q))
