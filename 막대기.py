import heapq
x = int(input())
stick = [64]
heapq.heapify(stick)
while sum(stick) > x:
    s = heapq.heappop(stick)
    s //= 2
    heapq.heappush(stick, s)
    if not sum(stick) >= x:
        heapq.heappush(stick, s)
print(len(stick))