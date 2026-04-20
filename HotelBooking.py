class HotelRoom:
    def __init__(self, room_number, price_per_night, is_booked=False):
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.is_booked = is_booked

    def book_room(self):
        if self.is_booked == False:
            self.is_booked = True
            print("Room booked successfully")
        else:
            print("Room is already booked")

    def checkout(self):
        if self.is_booked == True:
            self.is_booked = False
            print("Checkout successful")
        else:
            print("Room is not booked yet")


room1 = HotelRoom(101, 2500)
room1.book_room()
room1.book_room()

room1.checkout()
room1.checkout()
