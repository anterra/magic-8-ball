# Prompt: Arrays are great for storing possible responses from a program. If you combine that
#   with a random number generator, you can pick a random entry from this list, which works
#   great for games. Create a Magic 8 Ball game that prompts for a question and then displays
#   either "Yes", "No", "Maybe", or "Ask again later". Example Output: "What's your questions?
#   (Will I be rich and famous?) Ask again later." Constraint: The value should be chosen
#   randomly using a pseudo random number generator. Store the possible choices in a list and
#   select one at random.
# From "Exercises for Programmers: 57 Challenges to Develop Your Coding Skills" by Brian P. Hogan

# random module utilizes Mersenne Twister as core generator. one of the most extensively tested random number
#   generators in existence. it is however completely deterministic, not approved for security


import random


responses = ["Yes", "No", "Maybe", "Ask again later"]


def magic_8_ball_response():
    question = input("What's your questions? --> ")
    if question:
        print(responses[random.randrange(0, 4)])  # indexes 0 through 3 inclusive


magic_8_ball_response()


