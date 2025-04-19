import heapq

h = [5, 3, 1, 4, 2]
heapq.heapify(h)
print(h)

heapq.heappush(h, 9)
print(h)

heapq.heappop(h)
print(h)

heapq.heappushpop(h, 8)
print(h)

heapq.heapreplace(h, 10)
print(h)