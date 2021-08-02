""" Class to find the optimal solution which retunrs maximum jobs that can be scheduled in a day """

class Scheduling:
    def schedule(self, A : [[int]]) -> int:
        """ Scheuduling function """

        # Sort the jobs by their finish time
        A.sort(key=lambda le: le[1])

        count = 0
        p_start = 90000
        p_end = -90000
        flag = True

        # For the normal condition where job doesn't cross the midnight
        for i in range(0, len(A)):
            s_time, e_time = A[i][0], A[i][1]
            if s_time < e_time:
                if s_time >= p_end:
                    count += 1
                    p_end = e_time
                    p_start = s_time
            elif flag:
                p_start = s_time
                p_end = e_time
                flag = False
        
        # for the jobs which cross the midnight
        for i in range(0, len(A)):
            s_time, e_time = A[i][0],A[i][1]
            if s_time>e_time:
                if s_time>=p_end:
                    count += 1
                    break 

        #Get the no.of jobs selected in the process
        return count

A = [[64800, 21600], [75600, 14400], [10800, 50400], [46800, 68400]]

print(Scheduling().schedule(A))
