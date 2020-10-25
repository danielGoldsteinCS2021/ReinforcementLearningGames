import random
from numpy.random import choice
import numpy as np
from matplotlib import pyplot as plt
random.seed(1337)


def gameAlgorithm(rewardMatrices, policies, episodes, alpha, num_moves):
    p1_policies = np.empty([episodes, num_moves])
    p2_policies = np.empty([episodes, num_moves])
    for k in range(episodes):
        p1_policies[k] = policies[0]
        p2_policies[k] = policies[1]
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
        for o in range(len(policies[1])):
            if o != p2_action:
                policies[1][o] = p2_old[o] - alpha * \
                    p2_reward * p2_old[o]
    return policies, [p1_policies, p2_policies]


def generateAction(player, policies):
    # Generate a random action for player from probability vector
    action = choice(range(len(policies[player])),
                    p=policies[player])
    return action


if __name__ == "__main__":
    '''PRISONER'S'''
    player1, player2 = [[5, 0], [10, 1]], [[5, 10], [0, 1]]
    p = [[0.5, 0.5], [0.5, 0.5]]
    rewardMatrices = [player1, player2]
    # Run algorithm
    results = gameAlgorithm(rewardMatrices, p, 50000, 0.001, 2)
    # Organize results
    policies = results[0]
    p1_policies = results[1][0]
    p2_policies = results[1][1]
    # Generate player 1 figure
    p1_move1 = [i[0] for i in p1_policies]
    p1_move2 = [i[1] for i in p1_policies]
    plt.plot(p1_move1, label="Cooperate")
    plt.plot(p1_move2, label="Defect")
    plt.xlabel('Episode')
    plt.ylabel('Probability')
    plt.legend()
    plt.show()
    # Generate player 2 figure
    p2_move1 = [i[0] for i in p2_policies]
    p2_move2 = [i[1] for i in p2_policies]
    plt.plot(p2_move1, label="Cooperate")
    plt.plot(p2_move2, label="Defect")
    plt.xlabel('Episode')
    plt.ylabel('Probability')
    plt.legend()
    plt.show()

    '''PENNIES'''
    player1, player2 = [[1, -1], [-1, 1]], [[-1, 1], [1, -1]]
    p = [[0.2, 0.8], [0.8, 0.2]]
    rewardMatrices = [player1, player2]
    # Run algorithm
    results = gameAlgorithm(rewardMatrices, p, 50000, 0.001, 2)
    # Organize results
    policies = results[0]
    p1_policies = results[1][0]
    p2_policies = results[1][1]
    # Generate player 1 figure
    p1_move1 = [i[0] for i in p1_policies]
    p1_move2 = [i[1] for i in p1_policies]
    plt.plot(p1_move1, label="Head")
    plt.plot(p1_move2, label="Tail")
    plt.xlabel('Episode')
    plt.ylabel('Probability')
    plt.legend()
    plt.show()
    # Generate player 2 figure
    p2_move1 = [i[0] for i in p2_policies]
    p2_move2 = [i[1] for i in p2_policies]
    plt.plot(p2_move1, label="Head")
    plt.plot(p2_move2, label="Tail")
    plt.xlabel('Episode')
    plt.ylabel('Probability')
    plt.legend()
    plt.show()

    '''Rock Paper Scissors'''
    player1, player2 = [[0, -1, 1], [1, 0, -1],
                        [-1, 1, 0]], [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
    p = [[0.6, 0.2, 0.2], [0.2, 0.2, 0.6]]
    rewardMatrices = [player1, player2]
    # Run algorithm
    results = gameAlgorithm(rewardMatrices, p, 50000, 0.001, 3)
    # Organize results
    policies = results[0]
    p1_policies = results[1][0]
    p2_policies = results[1][1]
    # Generate player 1 figure
    p1_move1 = [i[0] for i in p1_policies]
    p1_move2 = [i[1] for i in p1_policies]
    p1_move3 = [i[2] for i in p1_policies]
    plt.plot(p1_move1, label="Rock")
    plt.plot(p1_move2, label="Paper")
    plt.plot(p1_move3, label="Scissors")
    plt.xlabel('Episode')
    plt.ylabel('Probability')
    plt.legend()
    plt.show()
    # Generate player 2 figure
    p2_move1 = [i[0] for i in p2_policies]
    p2_move2 = [i[1] for i in p2_policies]
    p2_move3 = [i[2] for i in p2_policies]
    plt.plot(p2_move1, label="Rock")
    plt.plot(p2_move2, label="Paper")
    plt.plot(p2_move3, label="Scissors")
    plt.xlabel('Episode')
    plt.ylabel('Probability')
    plt.legend()
    plt.show()

    print(policies)
