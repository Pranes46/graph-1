class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:  #tc - o(n), sc - o(n)
        
        q = deque() #initializing dequeue to do the queue operation
        indegree = [0]*numCourses # creating indegree using numcourses to store on the index after completing the pre requisite
        courseStudied = 0 # setting course studied to 0
        
        adj = defaultdict(list) # adjacency matrix
        for course,prereq in prerequisites: #to append the course, prereq as key,val for adjacency matrix
            adj[prereq].append(course) #appending the course as value on the prereq key
            indegree[course]+=1  #after appending increase the particular index by 1
        
        for i in range(len(indegree)): #to check whether there are any independent courses, if the indegree has any 0's it is the independent courses
            if indegree[i] == 0: 
                q.append(i)  #appending that index in the queue
                
        if not q:  #if there are no 0's in the indegree we are returning false as we cant create any course schedule
            return False
        
        while q:   #loop will run untill the queue become empty
            curr = q.popleft()   #popping the first element from the queue
            courseStudied+=1 #increment the course studied as we are processing the prereq
            for dependent in adj[curr]: #after taking the prereq we are decrementing the value of that in indegree, after that if the value is 0 we are appending it on the queue
                indegree[dependent] -= 1 
                if indegree[dependent] == 0:
                    q.append(dependent)
        
        if courseStudied == numCourses: #if the course studied is equal to numcourses we are returning true
            return True
        return False  #we are returning false
        