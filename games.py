import random
from numpy.random import choice
import numpy as np
from matplotlib import pyplot as plt
'''
Givigi says first, unmodified algorithm does  NOT converge
    this is because actions are changing over time
    algo doesn't work for non-stationary distribution

Modified algo
    Hint: calculate new term the same way we did before
    New Est. <- Current-est + Learning Rate [Target - Current-Est]
    E[p(k+1)] = E[p(k)]  + alpha * ("average itself" - current state)
    or calculate "mean value" using "statistics"

    Q(z, r) = Q(z, r) + alpha(g(z') + delta * min Q(z', r')
    summation of prob
'''


def modifiedAlgorithm(rewardMatrices, policies, episodes, alpha, num_moves):
    p1_policies = np.empty([episodes, num_moves])
    p2_policies = np.empty([episodes, num_moves])
    for k in range(episodes):

        # Store policies from previous episode
        p1_old = policies[0].copy()
        p2_old = policies[1].copy()

        # Keep track of policy at current episode for matplotlib figures
        p1_policies[k] = policies[0].copy()
        p2_policies[k] = policies[1].copy()

        # Generate actions for each player
        p1_action = generateAction(0, policies)
        p2_action = generateAction(1, policies)

        # Determine rewards for each player action
        p1_reward = rewardMatrices[0][p1_action][p2_action]
        p2_reward = rewardMatrices[1][p1_action][p2_action]

        # Expected values
        p1_expected[p1_action] = p1_expected[p1_action] + \
            alpha * p1_reward * (1-p1_old[p1_action])
        for o in range(len(policies[0])):
            if o != p1_action:
                p1_expected[o] = p1_expected[o] - alpha * \
                    p1_reward * p1_old[o]
        p2_expected[p2_action] = p2_expected[p2_action] + \
            alpha * p2_reward * (1-p2_old[p2_action])
        # For all other actions o =/= p2_action
        for o in range(len(policies[1])):
            if o != p2_action:
                p2_expected[o] = p2_expected[o] - alpha * \
                    p2_reward * p2_old[o]

        # Player 1
        # If chosen action is taken
        policies[0][p1_action] = p1_old[p1_action] + \
            alpha * p1_reward * \
            (1-p1_old[p1_action]) + alpha * \
            (p1_expected[p1_action] - p1_old[p1_action])
        # For all other actions o =/= p1_action
        for o in range(len(policies[0])):
            if o != p1_action:
                policies[0][o] = p1_old[o] - alpha * \
                    p1_reward * p1_old[o] + alpha * \
                    (p1_expected[o] - p1_old[o])

        # Player 2
        # If chosen action is taken
        policies[1][p2_action] = p2_old[p2_action] + \
            alpha * p2_reward * \
            (1-p2_old[p2_action]) + alpha * \
            (p2_expected[p2_action] - p2_old[p2_action])
        # For all other actions o =/= p2_action
        for o in range(len(policies[1])):
            if o != p2_action:
                policies[1][o] = p2_old[o] - alpha * \
                    p2_reward * p2_old[o] + alpha * \
                    (p2_expected[o] - p2_old[p2_action])

        # Normalize policies
        policies = normalize(policies)
    return policies, [p1_policies, p2_policies]


def gameAlgorithm(rewardMatrices, policies, episodes, alpha, num_moves):
    p1_policies = np.empty([episodes, num_moves])
    p2_policies = np.empty([episodes, num_moves])
    for k in range(episodes):
        # Store policies from previous episode
        p1_old = policies[0].copy()
        p2_old = policies[1].copy()

        # Keep track of policy at current episode for matplotlib figures
        p1_policies[k] = policies[0].copy()
        p2_policies[k] = policies[1].copy()

        # Generate actions for each player
        p1_action = generateAction(0, policies)
        p2_action = generateAction(1, policies)

        # Determine rewards for each player action
        p1_reward = rewardMatrices[0][p1_action][p2_action]
        p2_reward = rewardMatrices[1][p1_action][p2_action]

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

        # Normalize policies
        policies = normalize(policies)
    return policies, [p1_policies, p2_policies]


def generateAction(player, policies):
    # Generate a random action for player from probability vector
    action = choice(range(len(policies[player])),
                    p=policies[player])
    return action


def normalize(policies):
    p1 = policies[0].copy()
    p2 = policies[1].copy()
    p1_sum = sum(p1)
    p2_sum = sum(p2)
    for i in range(len(p1)):
        p1[i] = p1[i] / p1_sum
        p2[i] = p2[i] / p2_sum
    return [p1, p2]


def getExpectedValues(policies):
    # (Not being used right now)
    # Initialize expected values
    p1_expected = []
    p2_expected = []
    for i in range(len(policies[0])):
        p1_expected_sum = 0
        p2_expected_sum = 0
        for j in range(len(policies[0])):
            p1_expected_sum += policies[1][j] * rewardMatrices[0][i][j]
            p2_expected_sum += policies[0][j] * rewardMatrices[1][i][j]
        p1_expected.append(p1_expected_sum)
        p2_expected.append(p2_expected_sum)
    return [p1_expected, p2_expected]


if __name__ == "__main__":
    # '''PRISONER'S'''
    # player1, player2 = [[5, 0], [10, 1]], [[5, 10], [0, 1]]
    # p = [[0.5, 0.5], [0.5, 0.5]]
    # rewardMatrices = [player1, player2]
    # # Run algorithm
    # results = gameAlgorithm(rewardMatrices, p, 50000, 0.001, 2)
    # # Organize results
    # policies = results[0]
    # p1_policies = results[1][0]
    # p2_policies = results[1][1]
    # # Generate player 1 figure
    # p1_move1 = [i[0] for i in p1_policies]
    # p1_move2 = [i[1] for i in p1_policies]
    # plt.plot(p1_move1, label="Cooperate")
    # plt.plot(p1_move2, label="Defect")
    # plt.xlabel('Episode')
    # plt.ylabel('Probability')
    # plt.legend()
    # plt.show()
    # # Generate player 2 figure
    # p2_move1 = [i[0] for i in p2_policies]
    # p2_move2 = [i[1] for i in p2_policies]
    # plt.plot(p2_move1, label="Cooperate")
    # plt.plot(p2_move2, label="Defect")
    # plt.xlabel('Episode')
    # plt.ylabel('Probability')
    # plt.legend()
    # plt.show()

    # '''PENNIES'''
    # player1, player2 = [[1, -1], [-1, 1]], [[-1, 1], [1, -1]]
    # p = [[0.2, 0.8], [0.8, 0.2]]
    # rewardMatrices = [player1, player2]
    # # Run algorithm
    # results = gameAlgorithm(rewardMatrices, p, 50000, 0.001, 2)
    # # Organize results
    # policies = results[0]
    # p1_policies = results[1][0]
    # p2_policies = results[1][1]
    # # Generate player 1 figure
    # p1_move1 = [i[0] for i in p1_policies]
    # p1_move2 = [i[1] for i in p1_policies]
    # plt.plot(p1_move1, label="Head")
    # plt.plot(p1_move2, label="Tail")
    # plt.xlabel('Episode')
    # plt.ylabel('Probability')
    # plt.legend()
    # plt.show()
    # # Generate player 2 figure
    # p2_move1 = [i[0] for i in p2_policies]
    # p2_move2 = [i[1] for i in p2_policies]
    # plt.plot(p2_move1, label="Head")
    # plt.plot(p2_move2, label="Tail")
    # plt.xlabel('Episode')
    # plt.ylabel('Probability')
    # plt.legend()
    # plt.show()
    # print(policies)

    '''Rock Paper Scissors'''
    player1, player2 = [[0, -1, 1], [1, 0, -1],
                        [-1, 1, 0]], [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
    p = [[0.6, 0.2, 0.2], [0.6, 0.2, 0.2]]
    # p = [[0.33, 0.33, 0.34], [0.33, 0.33, 0.34]]

    rewardMatrices = [player1, player2]
    # Run algorithm
    # results = gameAlgorithm(rewardMatrices, p, 50000, 0.001, 3)
    results = modifiedAlgorithm(rewardMatrices, p, 50000, 0.001, 3)
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
