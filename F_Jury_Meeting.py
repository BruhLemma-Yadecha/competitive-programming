n, m, k = map(int, input().split())
flights = []
for _ in range(m):
    flights.append(tuple(map(int, input().split())))
cost = 0
# max the earliest arrivals and min the departures
arrivals = [x for x in flights if x[2] == 0]
departures = [x for x in flights if x[1] == 0]
last_arrival = max([x[0] for x in arrivals])
earliest_departure = min([x[0] for x in departures])
