class Solution:
    def countBit(self,num):
        count = 0
        while num:
            count += num & 1
            num = num >> 1
        return count
    
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for hr in range(12):
            for mnt in range(60):
                if self.countBit(hr) + self.countBit(mnt) == turnedOn:
                    hour,minutes =  str(hr) ,"0"+str(mnt)
                    res.append(hour + ":" + minutes[-2:])
        
        return res