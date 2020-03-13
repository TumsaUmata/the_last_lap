def findMostBookedHotelRoom(bookings):
    booked_items = dict()
    for booking in bookings:
        if booking[1::] not in booked_items:
            if booking[0] == "+":
                booked_items[booking[1::]] = 1
            else:
                booked_items[booking[1::]] = 0
        else:
            if booking[0] == "+":
                booked_items[booking[1::]] += 1

    booked_count = 0
    most_booked_room = ""
    for booked_item in booked_items:
        if booked_items[booked_item] > booked_count:
            booked_count = booked_items[booked_item]
            most_booked_room = booked_item
    return most_booked_room


if __name__ == '__main__':
    booking_1 = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]
    booking_2 = ["+1A", "+3E", "-1A", "+4F", "-1A", "-3E", "+4F"]
    booking_3 = ["+1A", "+3E", "-1A", "+4F", "-1A", "-3E", "+3E"]
    booking_4 = ["+1A", "+3E", "-1A", "+4F", "-1A", "-3E", "+3E", "+4F"]

    print(findMostBookedHotelRoom(booking_1))
    print(findMostBookedHotelRoom(booking_2))
    print(findMostBookedHotelRoom(booking_3))
    print(findMostBookedHotelRoom(booking_4))
