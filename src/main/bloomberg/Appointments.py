appts = [(1000, 1100), (1015, 1130), (1145, 1200), (1200, 1230)]


def find_the_min_required_room():
    """Find the minimal required rooms to fulfil all of the appointments, e.g. in this case, (1000, 1100) and (1145, 1200)
    can happen at one room
    """

    heap = []
    import heapq
    for appt in appts:
        if len(heap) == 0:
            heapq.heappush(heap, (appt[1], appt[0]))
        else:
            first_finish_appt = heap[0]

            if appt[0] >= first_finish_appt[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, (appt[1], appt[0]))
    return len(heap)


print find_the_min_required_room()
