class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

        s = date.split(" ")
        year = s[2]
        month = months[s[1]]
        day = s[0]
        if len(day) == 4:
            day = day[:2]
        else:
            day = '0' + day[:1]
        
        return year + '-' + month + '-' + day