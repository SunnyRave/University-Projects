# -*- coding: utf-8 -*-
# Name: Sunit Ravi
# Zid: z5436640

# SARSA - EG

import numpy as np
import matplotlib.pyplot as plt

class World(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.R = np.zeros(self.x*self.y)
        self.agentPos = 0
    
    def idx2xy(self,idx):
        x = int(idx / self.y)
        y = idx % self.y
        return x, y

    def xy2idx(self,x,y):
        return x*self.y + y

    def resetAgent(self, pos):
        self.agentPos = int(pos)

    def setReward(self, x, y, r):
        goalState = self.xy2idx(x, y)
        self.R[goalState] = r

    def getState(self):
        return self.agentPos

    def getReward(self):
        return self.R[self.agentPos]

    def getNumOfStates(self):
        return self.x*self.y
 
    def getNumOfActions(self):
        return 4

    def move(self,id):
        x_, y_ = self.idx2xy(self.agentPos)
        tmpX = x_
        tmpY = y_
        if id == 0: # move DOWN
            tmpX += 1
        elif id == 1: # move UP
            tmpX -= 1
        elif id == 2: # move RIGHT
            tmpY += 1
        elif id == 3: # move LEFT
            tmpY -= 1
        else:
            print("ERROR: Unknown action")

        if self.validMove(tmpX, tmpY):
            self.agentPos = self.xy2idx(tmpX,tmpY)

    def validMove(self,x,y):
        valid = True
        if x < 0 or x >= self.x:
            valid = False
        if y < 0 or y >= self.y:
            valid = False
        return valid

class Agent(object):
    def __init__(self, world):
        self.world = world
        self.numOfActions = self.world.getNumOfActions()
        self.numOfStates = self.world.getNumOfStates()
        self.Q = np.loadtxt('initial_Q_values.txt')
        self.rand_number = np.loadtxt('random_numbers.txt')
        self.rand1 = iter(self.rand_number)
        self.alpha = 0.7
        self.gamma = 0.4
        self.epsilon = 0.25
        self.temp=0.1

    # epsilon-greedy action selection
    def actionSelection(self, state):
        rand2 = next(self.rand1)
        if (rand2 <= self.epsilon):
            rand2 = next(self.rand1)
            if(rand2 <= self.epsilon): 
                action = 0
            elif(rand2 > self.epsilon and rand2 <= 0.5): 
                action = 1 
            elif(rand2 > 0.5 and rand2 <= 0.75): 
                action = 2 
            elif(rand2 > 0.75 and rand2 <= 1): 
                action = 3
        else:
            action = np.argmax(self.Q[state,:])
        return action
 
    def train(self, iter1):
        self.world.resetAgent(0)
        self.reward1=[]
        
        
        self.steps1=[]
        for itr in range(iter1):
            self.steps=0
            self.reward2=0

            state = 0
            self.world.resetAgent(state)

            # choose action
            a = self.actionSelection(state)
            expisode = True
          
            while expisode:
                # perform action
                self.world.move(a)
                self.steps=self.steps+1
                # look for reward
                reward = self.world.getReward()
                self.reward2 = self.reward2 + reward
                state_new = int(self.world.getState())

                # new action
                a_new = self.actionSelection(state_new)

                # update Q-values
                self.Q[state,a] += self.alpha*(reward +
                                    self.gamma*self.Q[state_new,a_new]-
                                    self.Q[state,a])
        
                state = state_new
                a = a_new
                
                if reward == 1.0:
                    self.Q[state_new,:] = 0
                    expisode = False
            self.steps1.append(self.steps)
            self.reward1.append(int(self.reward2))
                
        
        print(self.Q)
        
        
        

    def plotQValues(self):
        plt.rcParams.update({'font.size': 11})
        plt.imshow(self.Q, cmap='Oranges', interpolation='nearest', aspect='auto')
        plt.colorbar()
        plt.title("Q-values")
        plt.xlabel("Actions")
        plt.ylabel("States")
        plt.xticks(np.arange(4), ('Down', 'Up', 'Right', 'Left'))
        plt.yticks(np.arange(self.numOfStates), np.arange(self.numOfStates))
        plt.show()
        
        plt.figure()
        plt.plot(range(len(self.steps1)), self.steps1)
        plt.xlabel('Episodes')
        plt.ylabel('Steps')
        plt.title('Steps per episode')
        plt.show()
        
        plt.figure()
        plt.plot(range(len(self.reward1)), self.reward1)
        plt.xlabel('Episodes')
        plt.ylabel('Reward')
        plt.title('Accumulated Reward')
        plt.show()
    
        
if __name__ == "__main__":
    world = World(3,4)
    world.setReward(2, 3, 1.0) #Goal state
    world.setReward(1, 1, -1.0) #Fear region
    
  
    learner = Agent(world)
    learner.train(1000)
    
    learner.plotQValues()
    
# Q-Learning EG


import numpy as np
import matplotlib.pyplot as plt

class World(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.R = np.zeros(self.x*self.y)
        self.agentPos = 0
    
    def idx2xy(self,idx):
        x = int(idx / self.y)
        y = idx % self.y
        return x, y

    def xy2idx(self,x,y):
        return x*self.y + y

    def resetAgent(self, pos):
        self.agentPos = int(pos)

    def setReward(self, x, y, r):
        goalState = self.xy2idx(x, y)
        self.R[goalState] = r

    def getState(self):
        return self.agentPos

    def getReward(self):
        return self.R[self.agentPos]

    def getNumOfStates(self):
        return self.x*self.y
 
    def getNumOfActions(self):
        return 4

    def move(self,id):
        x_, y_ = self.idx2xy(self.agentPos)
        tmpX = x_
        tmpY = y_
        if id == 0: # move DOWN
            tmpX += 1
        elif id == 1: # move UP
            tmpX -= 1
        elif id == 2: # move RIGHT
            tmpY += 1
        elif id == 3: # move LEFT
            tmpY -= 1
        else:
            print("ERROR: Unknown action")

        if self.validMove(tmpX, tmpY):
            self.agentPos = self.xy2idx(tmpX,tmpY)

    def validMove(self,x,y):
        valid = True
        if x < 0 or x >= self.x:
            valid = False
        if y < 0 or y >= self.y:
            valid = False
        return valid

class Agent(object):
    def __init__(self, world):
        self.world = world
        self.numOfActions = self.world.getNumOfActions()
        self.numOfStates = self.world.getNumOfStates()
        self.Q = np.loadtxt('initial_Q_values.txt')
        self.rand_number = np.loadtxt('random_numbers.txt')
        self.rand1 = iter(self.rand_number)
        self.alpha = 0.7
        self.gamma = 0.4
        self.epsilon = 0.25
        self.temp=0.1

    # epsilon-greedy action selection
    def actionSelection(self, state):
        rand2 = next(self.rand1)
        if (rand2 <= self.epsilon):
            rand2 = next(self.rand1)
            if(rand2 <= self.epsilon): 
                action = 0
            elif(rand2 > self.epsilon and rand2 <= 0.5): 
                action = 1 
            elif(rand2 > 0.5 and rand2 <= 0.75): 
                action = 2 
            elif(rand2 > 0.75 and rand2 <= 1): 
                action = 3
        else:
            action = np.argmax(self.Q[state,:])
        return action
 
    def train(self, iter1):
        self.world.resetAgent(0)
        self.reward1=[]
        
        self.steps1=[]
        for itr in range(iter1):
            self.steps=0
            self.reward2=0
            

            state = 0
            self.world.resetAgent(state)

            
            
            expisode = True
          
            while expisode:
                a = self.actionSelection(state)
                # perform action
                self.world.move(a)
                self.steps=self.steps+1
                # look for reward
                reward = self.world.getReward()
                self.reward2 = self.reward2 + reward
                
                state_new = int(self.world.getState())

                
                
                
                

                # update Q-values
                self.Q[state,a] += self.alpha*(reward +
                                    self.gamma*np.max(self.Q[state_new,:])-
                                    self.Q[state,a])
        
                state = state_new
                
                
                if reward == 1.0:
                    self.Q[state_new,:] = 0
                    expisode = False
            self.steps1.append(self.steps)
            self.reward1.append(int(self.reward2))
                
        
        print(self.Q)
        
        
        

    def plotQValues(self):
        plt.rcParams.update({'font.size': 11})
        plt.imshow(self.Q, cmap='Oranges', interpolation='nearest', aspect='auto')
        plt.colorbar()
        plt.title("Q-values")
        plt.xlabel("Actions")
        plt.ylabel("States")
        plt.xticks(np.arange(4), ('Down', 'Up', 'Right', 'Left'))
        plt.yticks(np.arange(self.numOfStates), np.arange(self.numOfStates))
        plt.show()
        
        plt.figure()
        plt.plot(range(len(self.steps1)), self.steps1)
        plt.xlabel('Episodes')
        plt.ylabel('Steps')
        plt.title('Steps per episode')
        plt.show()
        
        plt.figure()
        plt.plot(range(len(self.reward1)), self.reward1)
        plt.xlabel('Episodes')
        plt.ylabel('Reward')
        plt.title('Accumulated Reward')
        plt.show()
    
        
if __name__ == "__main__":
    world = World(3,4)
    world.setReward(2, 3, 1.0) #Goal state
    world.setReward(1, 1, -1.0) #Fear region
    
  
    learner = Agent(world)
    learner.train(1000)
    
    learner.plotQValues()

# SARSA - Softmax

import numpy as np
import matplotlib.pyplot as plt

class World(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.R = np.zeros(self.x*self.y)
        self.agentPos = 0
    
    def idx2xy(self,idx):
        x = int(idx / self.y)
        y = idx % self.y
        return x, y

    def xy2idx(self,x,y):
        return x*self.y + y

    def resetAgent(self, pos):
        self.agentPos = int(pos)

    def setReward(self, x, y, r):
        goalState = self.xy2idx(x, y)
        self.R[goalState] = r

    def getState(self):
        return self.agentPos

    def getReward(self):
        return self.R[self.agentPos]

    def getNumOfStates(self):
        return self.x*self.y
 
    def getNumOfActions(self):
        return 4

    def move(self,id):
        x_, y_ = self.idx2xy(self.agentPos)
        tmpX = x_
        tmpY = y_
        if id == 0: # move DOWN
            tmpX += 1
        elif id == 1: # move UP
            tmpX -= 1
        elif id == 2: # move RIGHT
            tmpY += 1
        elif id == 3: # move LEFT
            tmpY -= 1
        else:
            print("ERROR: Unknown action")

        if self.validMove(tmpX, tmpY):
            self.agentPos = self.xy2idx(tmpX,tmpY)

    def validMove(self,x,y):
        valid = True
        if x < 0 or x >= self.x:
            valid = False
        if y < 0 or y >= self.y:
            valid = False
        return valid

class Agent(object):
    def __init__(self, world):
        self.world = world
        self.numOfActions = self.world.getNumOfActions()
        self.numOfStates = self.world.getNumOfStates()
        self.Q = np.loadtxt('initial_Q_values.txt')
        self.rand_number = np.loadtxt('random_numbers.txt')
        self.rand1 = iter(self.rand_number)
        self.alpha = 0.7
        self.gamma = 0.4
        self.epsilon = 0.25
        self.temp=0.1

    def actionSelection(self, state):
        prob = np.exp(self.Q[state]/self.temp) / np.sum(np.exp(self.Q[state]/self.temp)) 
        c_prob = np.cumsum(prob)
        random1 = next(self.rand1)
        action = np.searchsorted(c_prob, random1)
        return action
 
    def train(self, iter1):
        self.world.resetAgent(0)
        self.reward1=[]
        
        
        self.steps1=[]
        for itr in range(iter1):
            self.steps=0
            self.reward2=0

            state = 0
            self.world.resetAgent(state)

            # choose action
            a = self.actionSelection(state)
            expisode = True
          
            while expisode:
                # perform action
                self.world.move(a)
                self.steps=self.steps+1
                # look for reward
                reward = self.world.getReward()
                self.reward2 = self.reward2 + reward
                state_new = int(self.world.getState())

                # new action
                a_new = self.actionSelection(state_new)

                # update Q-values
                self.Q[state,a] += self.alpha*(reward +
                                    self.gamma*self.Q[state_new,a_new]-
                                    self.Q[state,a])
        
                state = state_new
                a = a_new
                
                if reward == 1.0:
                    self.Q[state_new,:] = 0
                    expisode = False
            self.steps1.append(self.steps)
            self.reward1.append(int(self.reward2))
                
        
        print(self.Q)
        
    
        
        

    def plotQValues(self):
        plt.rcParams.update({'font.size': 11})
        plt.imshow(self.Q, cmap='Oranges', interpolation='nearest', aspect='auto')
        plt.colorbar()
        plt.title("Q-values")
        plt.xlabel("Actions")
        plt.ylabel("States")
        plt.xticks(np.arange(4), ('Down', 'Up', 'Right', 'Left'))
        plt.yticks(np.arange(self.numOfStates), np.arange(self.numOfStates))
        plt.show()
        
        plt.figure()
        plt.plot(range(len(self.steps1)), self.steps1)
        plt.xlabel('Episodes')
        plt.ylabel('Steps')
        plt.title('Steps per episode')
        plt.show()
        
        plt.figure()
        plt.plot(range(len(self.reward1)), self.reward1)
        plt.xlabel('Episodes')
        plt.ylabel('Reward')
        plt.title('Accumulated Reward')
        plt.show()
    
        
if __name__ == "__main__":
    world = World(3,4)
    world.setReward(2, 3, 1.0) #Goal state
    world.setReward(1, 1, -1.0) #Fear region
    
  
    learner = Agent(world)
    learner.train(1000)
    
    learner.plotQValues()

# Q-Learning Softmax
import numpy as np
import matplotlib.pyplot as plt

class World(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.R = np.zeros(self.x*self.y)
        self.agentPos = 0
    
    def idx2xy(self,idx):
        x = int(idx / self.y)
        y = idx % self.y
        return x, y

    def xy2idx(self,x,y):
        return x*self.y + y

    def resetAgent(self, pos):
        self.agentPos = int(pos)

    def setReward(self, x, y, r):
        goalState = self.xy2idx(x, y)
        self.R[goalState] = r

    def getState(self):
        return self.agentPos

    def getReward(self):
        return self.R[self.agentPos]

    def getNumOfStates(self):
        return self.x*self.y
 
    def getNumOfActions(self):
        return 4

    def move(self,id):
        x_, y_ = self.idx2xy(self.agentPos)
        tmpX = x_
        tmpY = y_
        if id == 0: # move DOWN
            tmpX += 1
        elif id == 1: # move UP
            tmpX -= 1
        elif id == 2: # move RIGHT
            tmpY += 1
        elif id == 3: # move LEFT
            tmpY -= 1
        else:
            print("ERROR: Unknown action")

        if self.validMove(tmpX, tmpY):
            self.agentPos = self.xy2idx(tmpX,tmpY)

    def validMove(self,x,y):
        valid = True
        if x < 0 or x >= self.x:
            valid = False
        if y < 0 or y >= self.y:
            valid = False
        return valid

class Agent(object):
    def __init__(self, world):
        self.world = world
        self.numOfActions = self.world.getNumOfActions()
        self.numOfStates = self.world.getNumOfStates()
        self.Q = np.loadtxt('initial_Q_values.txt')
        self.rand_number = np.loadtxt('random_numbers.txt')
        self.rand1 = iter(self.rand_number)
        self.alpha = 0.7
        self.gamma = 0.4
        self.epsilon = 0.25
        self.temp=0.1

    
    def actionSelection(self, state):
        prob = np.exp(self.Q[state]/self.temp) / np.sum(np.exp(self.Q[state]/self.temp)) 
        c_prob = np.cumsum(prob)
        random1 = next(self.rand1)
        action = np.searchsorted(c_prob, random1)
        return action
    
 
    def train(self, iter1):
        self.world.resetAgent(0)
        self.reward1=[]
        
        self.steps1=[]
        for itr in range(iter1):
            self.steps=0
            self.reward2=0
            

            state = 0
            self.world.resetAgent(state)

            
            
            expisode = True
          
            while expisode:
                a = self.actionSelection(state)
                # perform action
                self.world.move(a)
                self.steps=self.steps+1
                # look for reward
                reward = self.world.getReward()
                self.reward2 = self.reward2 + reward
                
                state_new = int(self.world.getState())

                
                
                
                

                # update Q-values
                self.Q[state,a] += self.alpha*(reward +
                                    self.gamma*np.max(self.Q[state_new,:])-
                                    self.Q[state,a])
        
                state = state_new
                
                
                if reward == 1.0:
                    self.Q[state_new,:] = 0
                    expisode = False
            self.steps1.append(self.steps)
            self.reward1.append(int(self.reward2))
                
        
        print(self.Q)
        
        
        

    def plotQValues(self):
        plt.figure(1)
        plt.rcParams.update({'font.size': 11})
        plt.imshow(self.Q, cmap='Oranges', interpolation='nearest', aspect='auto')
        plt.colorbar()
        plt.title("Q-values")
        plt.xlabel("Actions")
        plt.ylabel("States")
        plt.xticks(np.arange(4), ('Down', 'Up', 'Right', 'Left'))
        plt.yticks(np.arange(self.numOfStates), np.arange(self.numOfStates))
        plt.show()
        
        plt.figure()
        plt.plot(range(len(self.steps1)), self.steps1)
        plt.xlabel('Episodes')
        plt.ylabel('Steps')
        plt.title('Steps per episode')
        plt.show()
        
        plt.figure()
        plt.plot(range(len(self.reward1)), self.reward1)
        plt.xlabel('Episodes')
        plt.ylabel('Reward')
        plt.title('Accumulated Reward')
        plt.show()
        
        
    
        
if __name__ == "__main__":
    world = World(5,6)
    world.setReward(2, 3, 1.0) #Goal state
    world.setReward(1, 1, -1.0) #Fear region
    
  
    learner = Agent(world)
    learner.train(1000)
    
    learner.plotQValues()



  



  


  



  