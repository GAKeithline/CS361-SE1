#Name: Gilbert Keithline
#OSU Email: keithlig@oregonstate.edu
#Assignment: CS361 Assignment 5- Main Program Implementation
#Date: 05/05/2024

class Game:
    """A game item living in the library"""
    def __init__(self):
        self._title = input('Enter name: ')
        self._maker = input('Enter maker: ')
        self._keywords = []
        self._description = input('Enter a game description: ')
        keyword = None
        print('Enter keywords one at a time, type "done" when you are done entering keywords.')
        while keyword != 'done':

            keyword = input('Keyword: ')
            if keyword != 'done':
                self._keywords.append(keyword)

    def get_name(self):
        """returns title of game"""
        return self._title

    def get_maker(self):
        """returns maker of game"""
        return self._maker

    def get_keywords(self):
        """returns list of keywords associated with the game"""
        return self._keywords

    def get_description(self):
        """returns a description of the game"""
        return self._description

class GameLib:
    """A library holding the games the user enters"""
    def __init__(self):
        self._library = {}
        self._size = 0

    def get_keys(self):
        """returns the keys (titles) from lib dictionary"""
        keys = self._library.keys()
        key_list = []
        for key in keys:
            key_list.append(key)
        return key_list

    def get_library(self):
        """returns the actual dictionary from self._library"""
        return self._library

    def add_game(self):
        """adds a new game to the library with keywords"""
        new_game = Game()
        print('Are you sure you want to add', new_game.get_name(), 'to the library?')
        x = input("Enter 'y' to add game, enter any other key to abort: ")
        if x.lower() == 'y':
            self._library[new_game.get_name()] = new_game
            print(new_game.get_name(), "has been added to the library!")
            self._size += 1
        else:
            print("You have chosen not to add", new_game.get_name(), 'to the library.')

    def remove_game(self, title):
        """deletes a game from the library"""
        if title in self._library:
            print('Are you sure you want to delete ', title.upper(), ' from the library?')
            x = input("Press 'y' to delete, press any other key to abort: ")
            if x.lower() == 'y':
                del self._library[title]
                print(title, ' has been deleted from the library')
                self._size -= 1
            else:
                print('You have chosen not to delete ', title)
        else:
            print('There is no game by that title in the library. \n')

close_command = 'None'
games = GameLib()
print('Welcome to GamePro!')
print('GamePro lets you save all your favorite games in one convenient location and is free to use!')
while close_command.lower() != 'close':
    print("\n---------"), print("Home Page"), print("---------")
    instruct = input("Enter 'y' to see instructions. Otherwise, simply hit 'enter': ")
    if instruct.lower() == 'y':
        print("Type 'add game' to add a new game to the library.")
        print("Type 'library' to view, edit, and delete existing games.")
        print("Enter any command other than 'add game' or 'library' to exit. \n")
    print("What would you like to do?")
    x = input("Add game, visit library, or exit?: ")
    if x.lower() == "add game":
        print("\n---------"), print("Add Game"), print("---------")
        print('Enter "y" to continue adding a game.')
        y = input("Enter any other value to return to the home screen: ")
        if y == 'y' or 'Y':
            games.add_game()
    if x.lower() == "library":
        print("\n---------"), print("Library"), print("---------")
        lib = games.get_keys()
        if lib == []:
            print('The library is currently empty')
            action = input("Hit 'enter' to return to the home page: ")
        else:
            print('Current titles: ', lib)
            action = input("Type 'delete' to delete a game or 'view' to see a game's details. Enter any other key to return to the home page: ")
        if action.lower() == 'delete':
            title = input("Type the name of the game you wish to delete: ")
            games.remove_game(title)
            print(games.get_keys())
        if action.lower() == 'view':
            title = input("Please type the name of the game you wish to view and press 'enter': ")
            print('Title: ', games.get_library()[title].get_name()), print('Maker: ', games.get_library()[title].get_maker())
            print('Description: ', games.get_library()[title].get_description()), print('Keywords: ', games.get_library()[title].get_keywords())


    print('\nWould you like to continue?')
    close_command = input("Press any key to return to the Home Page or type 'close' to close the program: ")