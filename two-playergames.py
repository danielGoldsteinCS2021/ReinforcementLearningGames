"""
CISC474 A2
Group 15
Part 2 - two player matrix games
"""


def gameAlgorithm(rewardMatrices, policies, episodes, alpha):
    numOfPlayers, numOfRows, numOfCols = len(policies), len(rewardMatricies[0]), len(rewardMatricies[1])  # each player has their own policy
    for _ in range(episodes):
        # p1
        policies[0][0] = policies[0][0] + alpha * rewardMatricies[0][0][0] * (1 - policies[0][0])
        policies[0][0] = policies[0][0] - alpha * rewardMatricies[1][0][0] * policies[0][0]

        policies[0][0] = policies[0][0] + alpha * rewardMatricies[0][0][1] * (1 - policies[0][0])
        policies[0][0] = policies[0][0] - alpha * rewardMatricies[1][0][1] * policies[0][0]

        policies[0][1] = policies[0][1] + alpha * rewardMatricies[0][1][0] * (1 - policies[0][1])
        policies[0][1] = policies[0][1] - alpha * rewardMatricies[1][1][0] * policies[0][1]

        policies[0][1] = policies[0][1] + alpha * rewardMatricies[0][1][1] * (1 - policies[0][1])
        policies[0][1] = policies[0][1] - alpha * rewardMatricies[1][1][1] * policies[0][1]

        # p2
        policies[1][0] = policies[1][0] + alpha * rewardMatricies[1][0][0] * (1 - policies[1][0])
        policies[1][0] = policies[1][0] - alpha * rewardMatricies[0][0][0] * policies[1][0]

        policies[1][0] = policies[1][0] + alpha * rewardMatricies[1][0][1] * (1 - policies[1][0])
        policies[1][0] = policies[1][0] - alpha * rewardMatricies[0][0][1] * policies[1][0]

        policies[1][1] = policies[1][1] + alpha * rewardMatricies[1][1][0] * (1 - policies[1][1])
        policies[1][1] = policies[1][1] - alpha * rewardMatricies[0][1][0] * policies[1][1]

        policies[1][1] = policies[1][1] + alpha * rewardMatricies[1][1][1] * (1 - policies[1][1])
        policies[1][1] = policies[1][1] - alpha * rewardMatricies[0][1][1] * policies[1][1]

    return policies


if __name__ == "__main__":
    player1, player2 = [[5, 0], [10, 1]], [[5, 10], [0, 1]]
    rewardMatricies = [player1, player2]
    policies = [[0.5, 0.5], [0.5, 0.5]]
    episodes = 50000
    print(gameAlgorithm(rewardMatricies, policies, episodes, 0.001))
