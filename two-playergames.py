"""
CISC474 A2
Group 15
Part 2 - two player matrix games
"""


def gameAlgorithm(rewardMatrices, policies, episodes, alpha):
    numOfPlayers, numOfRows, numOfCols = len(policies), len(rewardMatricies[0]), len(rewardMatricies[1])  # each player has their own policy
    for _ in range(episodes):
        for i in range(2):
            for j in range(2):
                policies[i][j] = policies[i][j] + alpha * rewardMatricies[i][0][0] * (1 - policies[i][j])
                policies[i][j] = policies[i][j] - alpha * rewardMatricies[i][1][0] * policies[i][j]
                policies[i][j] = policies[i][j] - alpha * rewardMatricies[i][0][1] * policies[i][j]
                policies[i][j] = policies[i][j] - alpha * rewardMatricies[i][1][1] * policies[i][j]

                policies[i][j] = policies[i][j] + alpha * rewardMatricies[i][1][0] * (1 - policies[i][j])
                policies[i][j] = policies[i][j] - alpha * rewardMatricies[i][0][0] * policies[i][j]
                policies[i][j] = policies[i][j] - alpha * rewardMatricies[i][0][1] * policies[i][j]
                policies[i][j] = policies[i][j] - alpha * rewardMatricies[i][1][1] * policies[i][j]

                policies[i][j] = policies[i][j] + alpha * rewardMatricies[i][0][1] * (1 - policies[i][j])
                policies[i][j] = policies[i][j] - alpha * rewardMatricies[i][1][0] * policies[i][j]
                policies[i][j] = policies[i][0] - alpha * rewardMatricies[i][0][0] * policies[i][j]
                policies[i][j] = policies[i][j] - alpha * rewardMatricies[i][1][1] * policies[i][j]

                policies[i][j] = policies[i][j] + alpha * rewardMatricies[i][1][1] * (1 - policies[i][j])
                policies[i][j] = policies[i][j] - alpha * rewardMatricies[i][1][0] * policies[i][j]
                policies[i][j] = policies[i][j] - alpha * rewardMatricies[i][0][1] * policies[i][j]
                policies[i][j] = policies[i][j] - alpha * rewardMatricies[i][0][0] * policies[i][j]
    return policies


if __name__ == "__main__":
    player1, player2 = [[5, 0], [10, 1]], [[5, 10], [0, 1]]
    rewardMatricies = [player1, player2]
    policies = [[0.5, 0.5], [0.5, 0.5]]
    episodes = 50000
    print(gameAlgorithm(rewardMatricies, policies, episodes, 0.001))
