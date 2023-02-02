class Solution:
    def __init__(self):
        self.words = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    def recurr(self,num):
        ans = ""
        if num >= 1000000000:
            ans += self.recurr(int(num//1000000000)) + " Billion " + self.recurr(num%1000000000)
        elif num >= 1000000:
            ans += self.recurr(int(num//1000000)) + " Million " + self.recurr(num%1000000)
        elif num >= 1000:
            ans += self.recurr(int(num//1000)) + " Thousand " + self.recurr(num%1000)
        elif num >= 100:
            ans += self.recurr(int(num//100)) + " Hundred " + self.recurr(num%100)
        elif num >= 20:
            ans += self.words[int((num - 20)//10 + 20)] + " " + self.recurr(num%10)
        else:
            ans += self.words[num]
        
        return ans.strip()
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ans = self.recurr(num)
        return ans      
