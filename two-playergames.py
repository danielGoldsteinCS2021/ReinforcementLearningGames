"""
CISC474 A2
Group 15
Part 2 - two player matrix games
"""


def gameAlgorithm(rewardMatrices, policies, episodes, alpha):
    numOfPlayers, numOfRows, numOfCols = len(policies), len(rewardMatricies[0]), len(rewardMatricies[1])  # each player has their own policy
    for _ in range(episodes):
        for rowNum in range(numOfRows):  # each row corresponds to the player taking an action
            for rewardIdx in range(numOfCols):
                for player in range(numOfPlayers):
                    rewardMatrix = rewardMatrices[player]  # get reward matrix for current player
                    reward = rewardMatrix[rowNum][rewardIdx]
                    policyForAction = policies[player][rowNum]
                    policyForAction = policyForAction + alpha * reward * (1 - policyForAction)
                    for rewardIdx2, reward2 in enumerate(rewardMatrix[rowNum]):  # for all other actions
                        if rewardIdx2 == rewardIdx:  # action is the same as our current action
                            continue
                        policyForAction = policyForAction - alpha * reward2 * policyForAction
                    policies[player][rowNum] = policyForAction
    return policies


if __name__ == "__main__":
    player1, player2 = [[5, 0], [10, 1]], [[5, 10], [0, 1]]
    rewardMatricies = [player1, player2]
    policies = [[0.5, 0.5], [0.5, 0.5]]
    episodes = 500000
    print(gameAlgorithm(rewardMatricies, policies, episodes, 0.001))
