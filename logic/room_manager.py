import operator


class RoomManager:
    def __init__(self, rooms, distances):
        self.rooms = rooms
        self.reachable_rooms = dict()

        # Loop over all distances and store them in both directions
        for room1, room2, distance in distances:
            room1_reachables = self.reachable_rooms.get(room1, [])
            room1_reachables.append((room2, distance))
            self.reachable_rooms[room1] = room1_reachables

            room2_reachables = self.reachable_rooms.get(room2, list())
            room2_reachables.append((room1, distance))
            self.reachable_rooms[room2] = room2_reachables

        # Sort distances ascending
        for room in self.rooms:
            room_reachables = self.reachable_rooms.get(room)
            room_reachables.sort(key=operator.itemgetter(1))

    def get_reachables_for_room(self, room):
        """
        Get a list of all reachable rooms for a given room (together with the distances)

        :param room: name of the room
        :type room: str
        :return: list of reachable rooms with their distances
        :rtype: list[tuple[str, int]]
        """
        return self.reachable_rooms.get(room)
