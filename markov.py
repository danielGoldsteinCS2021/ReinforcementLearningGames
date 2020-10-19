import numpy as np
import matplotlib.pyplot as plt


class gridworld:

    def __init__(self, size, A, A_, B, B_):
        # size of the gridworld (must be square in this implementation)
        self.size = size
        self.A = A  # A cell
        self.A_ = A_  # A' cell
        self.B = B  # B cell
        self.B_ = B_  # B' cell
        # possible actions the agent can take
        self.actions = ["N", "W", "S", "E"]
        # probability of each action taken
        self.action_prob = [0.25, 0.25, 0.25, 0.25]
        self.s = [0, 0]  # initial state
        self.V = 0

    def action(self, action):
        # Check if given action is legal
        if action not in self.actions:
            return "Invalid action"
        # Check special cases (i.e. cell A or B)
        if self.s == self.A:
            self.s = self.A_  # move agent to cell A'
            reward = 10  # receive reward of 10
        elif self.s == self.B:
            self.s = self.B_  # move agent to cell B'
            reward = 5  # receive reward of 5
        # Move north, making sure agent is not in top row
        elif action == "N" and self.s[0] > 0:
            self.s[0] -= 1
            reward = 0
        # Move west, making sure agent is not in leftmost column
        elif action == "W" and self.s[1] > 0:
            self.s[1] -= 1
            reward = 0
        # Move south, making sure agent is not in bottom row
        elif action == "S" and self.s[0] < self.size - 1:
            self.s[0] += 1
            reward = 0
        # Move east, making sure agent is not in rightmost column
        elif action == "E" and self.s[1] < self.size - 1:
            self.s[1] += 1
            reward = 0
        # Bumped into wall and cannot move - reduce reward
        else:
            reward = -1
        return self.s, reward


def state_value_table(grid, discount):
    v = np.zeros((grid.size, grid.size))
    delta = 0.01
    delta_t = 1

    while delta_t > delta:
        v_ = np.zeros((grid.size, grid.size))
        # iterate through each state
        for i in range(grid.size):
            for j in range(grid.size):
                # iterate through each action
                for action in grid.actions:
                    grid.s = [i, j]
                    # determine state and reward of current action
                    s, r = grid.action(action)
                    # determine index of current action
                    action_index = grid.actions.index(action)
                    prob = grid.action_prob[action_index]
                    v_[i, j] += prob * (r + discount * v[s[0], s[1]])
        delta_t = np.sum(np.abs(v - v_))
        v = v_.copy()
    return v


def v_star(grid, discount):
    # Initialize empty q, and delta values
    q = np.zeros((grid.size, grid.size, len(grid.actions)))
    delta = 0.01
    delta_t = 1
    while delta_t > delta:
        q_old = q.copy()
        # iterate through each state
        for i in range(grid.size):
            for j in range(grid.size):
                # iterate through each available action
                for a in grid.actions:
                    grid.s = [i, j]
                    # determine state and reward of current
                    s, r = grid.action(a)
                    # determine index of the current action
                    a_index = grid.actions.index(a)
                    q[i, j, a_index] = r + discount * np.max(q_old[s[0], s[1]])
        delta_t = np.sum(np.abs(q - q_old))
    return q


def optimal_policy(q, grid):
    x = np.linspace(0, grid.size - 1, grid.size) + 0.5
    y = np.linspace(grid.size - 1, 0, grid.size) + 0.5
    X, Y = np.meshgrid(x, y)
    zeros = np.zeros((grid.size, grid.size))
    q_max = np.max(q, axis=2)

    plt.figure(figsize=(4, 4))
    axes = plt.axes()

    for a, action in enumerate(grid.actions):
        q_star = np.zeros((grid.size, grid.size))
        for b in range(grid.size):
            for c in reversed(range(grid.size)):
                if q[b, c, a] == q_max[b, c]:
                    q_star[b, c] = 0.4
        # Plot results
        if action == "N":
            # arrow points north
            plt.quiver(X, Y, zeros, q_star, scale=1, units='xy')
        elif action == "W":
            # arrow points west
            plt.quiver(X, Y, -q_star, zeros, scale=1, units='xy')
        elif action == "S":
            # arrow points south
            plt.quiver(X, Y, zeros, -q_star, scale=1, units='xy')
        elif action == "E":
            # arrow points east
            plt.quiver(X, Y, q_star, zeros, scale=1, units='xy')

    # Set blank axis tick labels
    axes.set_yticklabels([])
    axes.set_xticklabels([])
    # Set the x and y limits for the axis
    plt.xlim([0, grid.size])
    plt.ylim([0, grid.size])
    plt.grid()  # Configure grid lines
    plt.show()  # Display the plot with the optimal policy


""" 5x5 grid problem """
# A(1,2), A'(5,2), B(1,4), B'(3,4)
# Initialize special cells A/B taking into account index starting at 0
A = [0, 1]
A_ = [4, 1]
B = [0, 3]
B_ = [2, 3]

# Discount rate = 0.85
print("5x5 case - Discount rate = 0.85")
grid = gridworld(5, A, A_, B, B_)
v = state_value_table(grid, 0.85)
print(v.round(1))
v = v_star(grid, 0.85)
print(np.max(v, axis=2).round(1))
optimal_policy(v, grid)

# # Discount rate = 0.75
print("\n5x5 case - Discount rate = 0.75")
grid = gridworld(5, A, A_, B, B_)
v = state_value_table(grid, 0.75)
print(v.round(1))
v = v_star(grid, 0.75)
print(np.max(v, axis=2).round(1))
optimal_policy(v, grid)

# """ 7x7 grid problem """
# # A(3,2), A'(7,2), B(1,6), B'(4,6)
# # Initialize special cells A/B taking into account index starting at 0
A = [2, 1]
A_ = [6, 1]
B = [0, 5]
B_ = [3, 5]

# # Discount rate = 0.85
print("\n7x7 case - Discount rate = 0.85")
grid = gridworld(7, A, A_, B, B_)
v = state_value_table(grid, 0.85)
print(v.round(1))
v = v_star(grid, 0.85)
print(np.max(v, axis=2).round(1))
optimal_policy(v, grid)

# # Discount rate = 0.75
print("\n7x7 case - Discount rate = 0.75")
grid = gridworld(7, A, A_, B, B_)
v = state_value_table(grid, 0.75)
print(v.round(1))
v = v_star(grid, 0.75)
print(np.max(v, axis=2).round(1))
optimal_policy(v, grid)
