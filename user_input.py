

class UserInput:
    def __init__(self, airports_dict):
        # Variables to store OWM connection data:
        self.airports_dict = airports_dict
        #self.itinerary_set = set([])
        self.itinerary_dict = {}
        self.size_loop = True
        self.itinerary_loop = True
        self.input_size = None

    def itinerary_size(self):

        while self.size_loop:
            try:
                self.input_size = int(input("Enter the number of places you would like to visit:"))
                if 1 < self.input_size <= 4:
                    self.size_loop = False
                else:
                    print()
                    print('The size of your itinerary must be four or less!')
                    print()

            except ValueError as e:
                print()
                print('That\'s not an integer:')
                print(e)
                print()

            except Exception as e:
                print(e)

    @staticmethod
    def desc_program():

        print("Please enter up to four destinations.")
        print()
        print("Note:")
        print("- Destinations must be in the format of IATA airport codes")
        print("- IATA codes consist of three alphabetic capital letters")
        print("- This program calculates a round trip. The first code you enter is both your starting point and destination")
        print()
        return 0

    def itinerary_input(self):

        while self.itinerary_loop:
            input_icao = str(input("Input code:"))

            if len(input_icao) == 3 and input_icao.isalpha():

                if (input_icao not in self.itinerary_dict) and (len(self.itinerary_dict) < (self.input_size-1)):
                    if input_icao in self.airports_dict:
                        self.itinerary_dict[input_icao] = None
                        print("Dictionary", self.itinerary_dict, "Size:", len(self.itinerary_dict))
                    else:
                        print("Airport code not in dictionary")
                        # raise ValueError("Airport code not in dictionary")

                elif len(self.itinerary_dict) == (self.input_size-1) and (input_icao not in self.itinerary_dict):

                    if input_icao in self.airports_dict:
                        self.itinerary_dict[input_icao] = None

                        print("Dictionary", self.itinerary_dict, "Size:", len(self.itinerary_dict))
                        print()
                        print("Thank-you, I will now calculate the shortest path (fuel price weighted)")
                        self.itinerary_loop = False

                    else:
                        print("Airport code does not exist")

                else:
                    print("Sorry that one is already in the dictionary")
                    # raise ValueError("Sorry, I don't understand your input")
            else:
                print('Inputted ICAO code is invalid. It must be four alphabetic characters')

'''
        except ValueError as e:
            print(e)
            self.user_input()

        except KeyboardInterrupt:
            print()
            print("Goodbye!!")
            exit()

        except Exception as e:
            print(e)
'''