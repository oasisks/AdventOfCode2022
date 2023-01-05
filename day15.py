from __future__ import annotations

import re


def day15(file):
    sensors = {}
    max_x = 0
    max_y = 0
    for line in file:
        sensor_x, beacon_x = [int(_.strip("x=")) for _ in re.findall(r'x=[+-]?[0-9]+', line)]
        sensor_y, beacon_y = [int(_.strip("y=")) for _ in re.findall(r'y=[+-]?[0-9]+', line)]

        if sensor_x > max_x:
            max_x = sensor_x
        if sensor_y > max_y:
            max_y = sensor_y
        dx = beacon_x - sensor_x
        dy = beacon_y - sensor_y
        manhattan = abs(dx) + abs(dy)
        sensors[sensor_x, sensor_y] = (beacon_x, beacon_y), manhattan

    def no_beacon_in_row(row, sensors) -> int:
        """
        Calculates the number of positions that cannot contain a beacon given the row
        :param row:
        :return: int
        """
        no_beacon_zone = set()
        for sensor in sensors:
            beacon, manhattan = sensors[sensor]
            dy = abs(sensor[1] - row)

            remaining_manhattan = manhattan - dy  # this is the remaining manhattan distance
            if remaining_manhattan >= 0:
                for _ in range(remaining_manhattan + 1):
                    left = sensor[0] - _, row
                    right = sensor[0] + _, row
                    if left != beacon:
                        no_beacon_zone.add(left)
                    if right != beacon:
                        no_beacon_zone.add(right)

        return len(no_beacon_zone)

    print(max_x, max_y)
    return no_beacon_in_row(2000000, sensors)


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day15(file))
    file.close()
