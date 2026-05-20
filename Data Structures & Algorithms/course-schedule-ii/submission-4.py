class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre={}
        for i in range(numCourses):
            pre[i]=set()
        for i,j in prerequisites:

            pre[j].add(i)

       
        path=set()
        order=[]
        visited=set()
    
        def noCycle(course: int)-> bool:
            if course in path:
                return False
            if course in visited:
           
                return True
            
            path.add(course)
            visited.add(course)
    
            for preReq in pre[course]:
               
         
                if not noCycle(preReq):
                    return False
            path.remove(course)
            order.append(course)
           

            return True
        
        for course in range(numCourses):
            if not noCycle(course):
                #print("here")
                return []
        #print(order)
        order.reverse()
        return order 



        