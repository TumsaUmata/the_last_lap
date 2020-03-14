# def solution(A):
#     booked_items = dict()
#     for booking in A:
#         if booking[1::] not in booked_items:
#             if booking[0] == "+":
#                 booked_items[booking[1::]] = 1
#             else:
#                 booked_items[booking[1::]] = 0
#         else:
#             if booking[0] == "+":
#                 booked_items[booking[1::]] += 1
#
#     booked_count = 0
#     most_booked_room = ""
#     for booked_item in booked_items:
#         if booked_items[booked_item] == booked_count:
#             if not most_booked_room:
#                 booked_count = booked_items[booked_item]
#                 most_booked_room = booked_item
#             if booked_item < most_booked_room:
#                 booked_count = booked_items[booked_item]
#                 most_booked_room = booked_item
#         elif booked_items[booked_item] > booked_count:
#             booked_count = booked_items[booked_item]
#             most_booked_room = booked_item
#     return most_booked_room


def max_booking(booking):
    booked_items = {}
    for room in booking:
        if room[0] == '+':
            booked_items[room[1:]] = booked_items.get(room[1:], 0) + 1

    most_booked = sorted(booked_items.items(), key=lambda booked_item: (-booked_item[1], booked_item[0]))

    return most_booked[0][0]


if __name__ == '__main__':
    booking_1 = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]
    booking_2 = ["+1A", "+3E", "-1A", "+4F", "-1A", "-3E", "+4F"]
    booking_3 = ["+1A", "+3E", "-1A", "+4F", "-1A", "-3E", "+3E"]
    booking_4 = ["+1A", "+3E", "-1A", "+4F", "-1A", "-3E", "+3E", "+4F"]

    print(max_booking(booking_1))
    print(max_booking(booking_2))
    print(max_booking(booking_3))
    print(max_booking(booking_4))

    booking5 = ["+1A", "+3F", "+8X", "-1A", "-3F", "-8X"]
    print(max_booking(booking5))
