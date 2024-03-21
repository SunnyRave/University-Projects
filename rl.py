# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:57:23 2023

@author: Francisco

Reinforcement learning

"""

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
 
    def train(self, iter):
        self.world.resetAgent(0)
        
        steps1=[]
        for itr in range(iter):
            self.steps=0

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
            steps1.append(self.steps)
                
        
        print(self.Q)
        print(steps1)
        
        

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
    
        
if __name__ == "__main__":
    world = World(3,4)
    world.setReward(2, 3, 1.0) #Goal state
    world.setReward(1, 1, -1.0) #Fear region
    
  
    learner = Agent(world)
    learner.train(1000)
    
    learner.plotQValues()



  