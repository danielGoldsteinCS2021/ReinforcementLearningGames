import random
from numpy.random import choice
import numpy as np
random.seed(1337)


def gameAlgorithm(rewardMatrices, policies, episodes, alpha):
    for k in range(episodes):
        # Generate actions for each player
        p1_action = generateAction(0, policies)
        p2_action = generateAction(1, policies)

        # Determine rewards for each player action
        p1_reward = rewardMatrices[0][p1_action][p2_action]
        p2_reward = rewardMatrices[1][p1_action][p2_action]

        p1_old = policies[0]
        p2_old = policies[1]
        # Player 1
        # If chosen action is taken
        policies[0][p1_action] = p1_old[p1_action] + \
            alpha * p1_reward * (1-p1_old[p1_action])
        # For all other actions o =/= p1_action
        for o in range(len(policies[0])):
            if o != p1_action:
                policies[0][o] = p1_old[o] - alpha * \
                    p1_reward * p1_old[o]

        # Player 2
        # If chosen action is taken
        policies[1][p2_action] = p2_old[p2_action] + \
            alpha * p2_reward * (1-p2_old[p2_action])
        # For all other actions o =/= p2_action
        for i in range(len(policies[1])):
            if i != p2_action:
                policies[1][i] = p2_old[i] - alpha * \
                    p2_reward * p2_old[i]

    return policies


def generateAction(player, policies):
    # Generate a random action for player from probability vector
    action = choice(range(len(policies[player])),
                    p=policies[player])
    return action


if __name__ == "__main__":
    # Prisoner's
    player1, player2 = [[5, 0], [10, 1]], [[5, 10], [0, 1]]
    p = [[0.5, 0.5], [0.5, 0.5]]
    # Pennies
    player1, player2 = [[1, -1], [-1, 1]], [[-1, 1], [1, -1]]
    p = [[0.2, 0.8], [0.8, 0.2]]
    # RPS
    player1, player2 = [[0, -1, 1], [1, 0, -1],
                        [-1, 1, 0]], [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
    p = [[0.6, 0.2, 0.2], [0.2, 0.2, 0.6]]

    rewardMatricies = [player1, player2]
    e = 50000
    policies = gameAlgorithm(rewardMatricies, p, e, 0.001)
    print(policies)
