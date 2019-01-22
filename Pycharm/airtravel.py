from pprint import pprint as pp
class Flight:
    def __init__(self,number,aircraft):
        if not number[:2].isalpha() or not number[:2].isupper():
            raise ValueError("No Airline code or Not valid airline code {}".format(number))
        if not number[2:].isdigit() and not number[2:] <= 9999:
            raise ValueError("Invalid route number {} in".format(number))
        self._number=number
        self._aircraft=aircraft
        rows, seats = self._aircraft.seating_plan()
#        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]
        self._seating = [None] + [{str(num)+letter: None for letter in seats} for num in rows]

    def number(self):
        return(self._number)

    def airline(self):
        return(self._number[:2])

    def aircraft_model(self):
        return(self._aircraft.model())

    def _parse_seat(self,seat):
        rows_numbers, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)

        except ValueError:
            raise ValueError("Invalid seat row {}", format(row_text))

        if row not in rows_numbers:
            raise ValueError("Invalid row number {}".format(row))

        return(row)


    def allocate_seat(self,seat,passenger):

        row = self._parse_seat(seat)
        if self._seating[row][seat] is not None:
            raise ValueError("Seat {} is already occupied".format(seat))

        self._seating[row][seat] = passenger

    def relocate_seat(self,from_seat, to_seat):
        from_row = self._parse_seat(from_seat)

        if self._seating[from_row][from_seat] is None:
            raise ValueError("No Passenger on seat {} ".format(from_seat))

        to_row = self._parse_seat(to_seat)

        if self._seating[to_row][to_seat] is not None:
            raise ValueError("seat {} already occupied".format(to_seat))

        self._seating[to_row][to_seat] = self._seating[from_row][from_seat]
        self._seating[from_row][from_seat] = None


    def print_seating(self):
        pp(self._seating)


class Aircraft:
    def __init__(self,registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_rows = num_seats_per_row

    def registration(self):
        return(self._registration)

    def model(self):
        return(self._model)

    def seating_plan(self):
        return(range(1,self._num_rows + 1),"ABCDEFGHJK"[:self._num_seats_per_rows])

def make_flight():
    f=Flight("AN4404", Aircraft("EU-756","Airbus319", 22, 6))
    f.allocate_seat("1F", "Sunil")
    f.allocate_seat("10B", "Anil")
    f.allocate_seat("13A", "Shreeya")
    f.allocate_seat("16C", "Anvee")
    f.allocate_seat("21F", "Gaurav")
    f.print_seating()
