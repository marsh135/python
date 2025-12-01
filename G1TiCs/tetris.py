import numpy as np
import random
from collections import deque
# import tensorflow as tf  # Removed as it is not used
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95  # Discount factor
        self.epsilon = 1.0  # Exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, activation='relu', input_shape=(self.state_size,)))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state, verbose=0)
        return np.argmax(act_values[0])

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state, verbose=0)[0])
            target_f = self.model.predict(state, verbose=0)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)

# Example usage with a Tetris environment
if __name__ == "__main__":
    # Replace `state_size` and `action_size` with the actual values for your Tetris environment
    state_size = 4  # Example state size
    action_size = 2  # Example action size
    agent = DQNAgent(state_size, action_size)
    episodes = 1000

    # Placeholder for Tetris environment
    class TetrisEnv:
        def reset(self):
            return np.zeros(state_size)  # Replace with actual reset logic

        def step(self, action):
            next_state = np.zeros(state_size)  # Replace with actual next state logic
            reward = 0  # Replace with actual reward logic
            done = False  # Replace with actual done condition
            return next_state, reward, done, {}

    env = TetrisEnv()

    for e in range(episodes):
        state = np.reshape(env.reset(), [1, state_size])
        for time in range(500):
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            next_state = np.reshape(next_state, [1, state_size])
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if done:
                print(f"Episode: {e}/{episodes}, Score: {time}")
                break
        if len(agent.memory) > 32:
            agent.replay(32)