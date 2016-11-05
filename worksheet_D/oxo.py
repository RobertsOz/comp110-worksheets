class OxoBoard:
    def __init__(self):
        """
        For nxn I would have to choose a different
        naming scheme something like ZeroZero,OneZero representing x and y
        """

            # I use the dictionary so I can have names next to my values for ease of changing them
        self.fields = {"Top Left": 0, "Top Middle": 0, "Top Right": 0,
                       "Middle Left": 0, "Middle Middle": 0, "Middle Right": 0,
                       "Bottom Left": 0, "Bottom Middle": 0, "Bottom Right": 0}

    def get_square(self, x, y):
        """
        For nxn I would just have to add the extra squares
        """
            # Here I'm returning the current value of the current position

            # Top line
        if x == 0 and y == 0:
            return board.fields["Top Left"]
        elif x == 1 and y == 0:
            return board.fields["Top Middle"]
        elif x == 2 and y == 0:
            return board.fields["Top Right"]

            # Middle line
        elif x == 0 and y == 1:
            return board.fields["Middle Left"]
        elif x == 1 and y == 1:
            return board.fields["Middle Middle"]
        elif x == 2 and y == 1:
            return board.fields["Middle Right"]

            # Bottom line
        elif x == 0 and y == 2:
            return board.fields["Bottom Left"]
        elif x == 1 and y == 2:
            return board.fields["Bottom Middle"]
        elif x == 2 and y == 2:
            return board.fields["Bottom Right"]

    def set_square(self, x, y, mark):
        """
        For nxn I would again have to add extra squares
        """

            # Top line
        if x == 0 and y == 0 and board.fields["Top Left"] == 0:
                # Change the field value to mark
            board.fields["Top Left"] = mark
            return True
        elif x == 0 and y == 0 and board.fields["Top Left"] > 0:
                # if the field is anything other than 0 return False
            return False
        if x == 1 and y == 0 and board.fields["Top Middle"] == 0:
            board.fields["Top Middle"] = mark
            return True
        elif x == 1 and y == 0 and board.fields["Top Middle"] > 0:
            return False
        if x == 2 and y == 0 and board.fields["Top Right"] == 0:
            board.fields["Top Right"] = mark
            return True
        elif x == 2 and y == 0 and board.fields["Top Right"] > 0:
            return False

            # Middle line
        if x == 0 and y == 1 and board.fields["Middle Left"] == 0:
            board.fields["Middle Left"] = mark
            return True
        elif x == 0 and y == 1 and board.fields["Middle Left"] > 0:
            return False
        if x == 1 and y == 1 and board.fields["Middle Middle"] == 0:
            board.fields["Middle Middle"] = mark
            return True
        elif x == 1 and y == 1 and board.fields["Middle Middle"] > 0:
            return False
        if x == 2 and y == 1 and board.fields["Middle Right"] == 0:
            board.fields["Middle Right"] = mark
            return True
        elif x == 2 and y == 1 and board.fields["Middle Right"] > 0:
            return False

            # Bottom line
        if x == 0 and y == 2 and board.fields["Bottom Left"] == 0:
            board.fields["Bottom Left"] = mark
            return True
        elif x == 0 and y == 2 and board.fields["Bottom Left"] > 0:
            return False
        if x == 1 and y == 2 and board.fields["Bottom Middle"] == 0:
            board.fields["Bottom Middle"] = mark
            return True
        elif x == 1 and y == 2 and board.fields["Bottom Middle"] > 0:
            return False
        if x == 2 and y == 2 and board.fields["Bottom Right"] == 0:
            board.fields["Bottom Right"] = mark
            return True
        elif x == 2 and y == 2 and board.fields["Bottom Right"] > 0:
            return False

    def is_board_full(self):
        """
        Nothing would change for nxn
        """

            # Loop through the dictionary and if any of the values is 0 return False
        for field_name, value in board.fields.iteritems():
            if value == 0:
                return False
            # When the loop ends that means there are no empty squares so return True
        return True

    def get_winner(self):
        """
        For nxn I would have to add the extra win conditions, although if its a 100x100 board this could get hectic
        You would have to change how squares are checked for the win condition and just have a know the current square
        and check the squares around it in the n radius of the win condition.
        """

            # Horizonal outcomes
            # Check a win condition if the 3 squares match and they are NOT 0
        if board.fields["Top Left"] == board.fields["Top Middle"] == board.fields["Top Right"] and board.fields[
                "Top Left"] != 0:
                # Return one of the squares doesn't matter which one because this can only happen if they are all equal
            return board.fields["Top Left"]

        elif board.fields["Bottom Left"] == board.fields["Bottom Middle"] == board.fields["Bottom Right"] and \
                board.fields["Bottom Left"] != 0:
            return board.fields["Bottom Left"]

        elif board.fields["Middle Left"] == board.fields["Middle Middle"] == board.fields["Middle Right"] and \
                board.fields["Middle Left"] != 0:
            return board.fields["Middle Left"]

            # Vertical outcomes
        elif board.fields["Top Left"] == board.fields["Middle Left"] == board.fields["Bottom Left"] and board.fields[
                "Bottom Left"] != 0:
            return board.fields["Bottom Left"]

        elif board.fields["Top Middle"] == board.fields["Middle Middle"] == board.fields["Bottom Middle"] and \
                board.fields["Bottom Middle"] != 0:
            return board.fields["Bottom Middle"]

        elif board.fields["Top Right"] == board.fields["Middle Right"] == board.fields["Bottom Right"] and board.fields[
                "Bottom Right"] != 0:
            return board.fields["Bottom Right"]

            # Diognal outcomes
        elif board.fields["Top Left"] == board.fields["Middle Middle"] == board.fields["Bottom Right"] and board.fields[
                "Bottom Right"] != 0:
            return board.fields["Bottom Right"]
        elif board.fields["Bottom Left"] == board.fields["Middle Middle"] == board.fields["Top Right"] and board.fields[
                "Top Right"] != 0:
            return board.fields["Top Right"]
            # Return 0 if there is no victor
        else:
            return 0

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in xrange(3):
            if y > 0:
                print "--+---+--"
            for x in xrange(3):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print


def input_square():
    """ Prompt the player to enter a square. You should not need to edit this. """
    while True:
        input = raw_input("Enter x,y where x=0,1,2, y=0,1,2: ")
        if input.count(',') != 1:
            print "Input must contain exactly one comma!"
            continue

        x, y = input.split(',')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print "Input must be two numbers separated by a comma!"
            continue

        if x < 0 or x > 2 or y < 0 or y > 2:
            print "Input is out of bounds!"
            continue

        return x, y


# The main game. You should not need to edit this.
if __name__ == '__main__':
    board = OxoBoard()
    current_player = 1
    while True:
        board.show()
        print "Choose a square, Player", current_player
        x, y = input_square()

        if board.set_square(x, y, current_player):
            # Move was played successfully, so check for a winner
            winner = board.get_winner()
            if winner != 0:
                print "Player", winner, "wins!"
                break  # End the game
            elif board.is_board_full():
                print "It's a draw!"
                break  # End the game
            else:
                # Switch players
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
        else:
            # Move was not played successfully
            print "That square is already filled!"
