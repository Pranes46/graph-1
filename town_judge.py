class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:  #tc - o(n), sc - o(n)
        
        indegree = [0]*n  #we are creating an indegree array as we did on course schedule
        for person,trusted_person in trust:# we are decrementing the value if the person trusts other person, we are incrementing the value if the other person doesnt trust him
            indegree[person-1]-=1 
            indegree[trusted_person-1]+=1 
            
        for i in range(len(indegree)):  #if there is any number with high value we are returning index+1 else we are returning -1
            if indegree[i] == n-1: 
                return i+1 
        return -1 
        