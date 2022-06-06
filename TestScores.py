#declare variables
TestScore1 = 0.0
TestScore2 = 0.0
TestAvg = 0.0
TotalScores = 0.0

#ask user for test scores
TestScore1 = float(input("Enter test score 1:  "))
TestScore2 = float(input("Enter test score 2:  "))

#determine total and avg of scores
TotalScores = TestScore1 + TestScore2
TestAvg = TotalScores/2

print("The average is:  ", TestAvg)