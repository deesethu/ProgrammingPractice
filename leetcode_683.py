class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        day = -1
        length = len(flowers)
        position = [0] * length
        count = 1
        
        #Boundary condition
        if (length < k + 2):
            return -1
        
        #Create a position array
        for flo in flowers:
            position[flo - 1] = count
            count = count + 1

        #traverse with sliding window
        for i in range(length - k - 1):
            win = i + k + 1
            max_win = max(position[i], position[win])
            j = i + 1
            min_win = position[j]
            flag = 0
            if ((min_win < max_win) and (k != 0)):
                flag = 1
            else:
                j = j + 1
                #Traverse between the window to get min
                while j < win:
                    if (position[j] < min_win):
                        min_win = position[j]
                        if(min_win < max_win):
                            flag = 1
                            break
                    j = j + 1
            if (not flag):  
                if (day > max_win or day == -1):
                    day = max_win
            i = j
        return day
