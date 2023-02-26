def find_furthest_orbit(list_of_orbit):
    orbits_sq = [3.14*list_of_orbit[i][0]*list_of_orbit[i][1]
                 for i in range(len(list_of_orbit)) if list_of_orbit[i][0] != list_of_orbit[i][1]]
    return list(filter(lambda x: x[0]*x[1]*3.14 == max(orbits_sq), list_of_orbit))


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_furthest_orbit(orbits))
