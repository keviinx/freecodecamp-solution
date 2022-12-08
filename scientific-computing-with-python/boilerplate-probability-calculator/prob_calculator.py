import copy
import random
# Consider using the modules imported above.

class Hat:

    # init function
    def __init__(self, **kwargs):
        # init content as 
        self.contents = []
        # loop to fill up the content
        for color, number_of_balls in kwargs.items():
            self.contents += [color] * number_of_balls

    # draw method that accepts an argument indicating the number of balls to draw from the hat.
    def draw(self, number_of_balls_to_draw):
        # If the number of balls to draw exceeds the available quantity,
        if number_of_balls_to_draw > len(self.contents):
            # set all the balls to draw
            balls_to_draw = self.contents
            # clear self.contents
            self.contents = []
            # return all the balls.
            return balls_to_draw

        # get the list of random balls to draw
        balls_to_draw = random.sample(self.contents, number_of_balls_to_draw)

        # go thru the loop and remove the balls
        for ball_to_draw in balls_to_draw:
            self.contents.remove(ball_to_draw)

        # return the list
        return balls_to_draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # we perform N experiments
    N = num_experiments
    # count how many times M we get
    M = 0

    # go thru the experiments
    for experiment in range(num_experiments):
        # make a copy of hat
        hat_copy = copy.deepcopy(hat)
        # draw the balls from hat copy
        balls_drawn = hat_copy.draw(num_balls_drawn)
        # set success to True
        success = True
        # get the probability
        for expected_color, expected_number in expected_balls.items():
            # count the number of colors drawn
            color_number = balls_drawn.count(expected_color)
            # success stays true if number of colors drawn is equal or more than the expected number
            success = success and (color_number >= expected_number)

        # increase M if success
        if success:
            M += 1

    # return M/N
    return M/N