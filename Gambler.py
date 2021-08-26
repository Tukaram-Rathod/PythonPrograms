"""
@Author: Tukaram Rathod
@Date: 2021-08-25 11:50:30 AM
@Title : Gambler
a. Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
    he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
    times he/she wins and the number of bets he/she makes. Run the experiment N
    times, averages the results, and prints them out.
b. I/P -> $Stake, $Goal and Number of times
c. Logic -> Play till the gambler is broke or has won
d. O/P -> Print Number of Wins and Percentage of Win and Loss.
"""

import random

class Gambler:
    def __init__(self,StartValue,TargetValue):
        #initialize constructor using parameter
        self.StartValue = StartValue
        self.TargetValue = TargetValue

    def calculateAvgCount(self):
        countBet = 0
        winCount =0
        lossCount = 0
        while True:
            if self.StartValue == 0 or self.StartValue == self.TargetValue:
                break
            else:
                random_Value = int(input(random.choice([0,1])))
                countBet = countBet + 1
                if random_Value == 1:
                    self.StartValue = self.StartValue + 1
                    winCount = winCount + 1
                else:
                    self.StartValue = self.StartValue - 1
                    lossCount = lossCount + 1
        return winCount,lossCount,countBet

while True:
    try:
        stack_value = int(input("Enter the start amount :"))
        if stack_value < 0:
            print("Please Enter Positive Value")
            continue
        goal_value = int(input("Enter goal Amount :"))
        if goal_value < 0:
            print("Please Enter Positive Value")
            continue
        gambler = Gambler(stack_value,goal_value)
        winCount,lossCount,countBet = gambler.calculateAvgCount()
        print("Percentage of win count",(winCount / countBet) * 100)
        print("Percentage of loss count ",(lossCount / countBet) * 100)
    except ValueError:
        print("Invalid Input")
    except:
        print("Exception Occured")