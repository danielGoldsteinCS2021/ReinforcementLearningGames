"""
CISC474 A2
Group 15
Part 2 - two player matrix games
"""


def gameAlgorithm(rewardMatrices, policies, episodes, alpha):
    for _ in range(episodes):
        for i in range(2):  # i switches between our 2 players
            # ith index refers to player, the 0th index of each policy is the first probability, the 1st is the second
            # rewardMatrices[i][0][0] is both players choose cooperate, [i][0][1] is if one chooses to defect
            # [i][1][0] is if p1 chooses to defect, p2 chooses to cooperate
            # [i][1][1] both defect

            # policy value 1
            policies[i][0] = policies[i][0] + alpha * (rewardMatrices[i][0][0] + rewardMatrices[i][0][1]) * (1 - policies[i][0])
            policies[i][0] = policies[i][0] - alpha * (rewardMatrices[i][1][0] + rewardMatrices[i][1][1]) * policies[i][0]

            # policy value 2
            policies[i][1] = policies[i][1] + alpha * (rewardMatrices[i][1][0] + rewardMatrices[i][1][1]) * (1 - policies[i][1])
            policies[i][1] = policies[i][1] - alpha * (rewardMatrices[i][0][1] + rewardMatrices[i][0][0]) * policies[i][1]
    return policies


if __name__ == "__main__":
    player1, player2 = [[5, 0], [10, 1]], [[5, 10], [0, 1]]
    rewardMatricies = [player1, player2]
    p = [[0.5, 0.5], [0.5, 0.5]]
    e = 50000
    print(gameAlgorithm(rewardMatricies, p, e, 0.001))
