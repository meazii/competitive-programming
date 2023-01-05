def gradingStudents(grades):
    # Write your code here
    ans=[]
    for x in grades:
        if x%5>2 and x>37:
            ans.append(x+(5-(x%5)))
        else:
            ans.append(x)
    return ans
