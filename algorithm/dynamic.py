def dtw_distance(seqA, seqB):
    n, m = len(seqA), len(seqB)
    dtw_matrix = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]
    dtw_matrix[0][0] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = abs(seqA[i-1] - seqB[j-1])
            dtw_matrix[i][j] = cost + min(dtw_matrix[i-1][j], dtw_matrix[i][j-1], dtw_matrix[i-1][j-1])
    return dtw_matrix[n][m]

A = [1, 3, 4, 9]
B = [1, 3, 7, 8]

print("DTW distance between A and B:", dtw_distance(A, B))
