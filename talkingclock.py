"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""




    # This will convert military hours to regular hours, and determine AM vs PM
  
class Solution:
    def ClockTalker(self, input_time):
        numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
        tens = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}
        tens_words = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
        am_pm = {'am': 'am', 'pm': 'pm'}
        hours, minutes = input_time.split(':')
        if hours == '12':
            hours = '12'
            am_pm_str = 'pm'
        elif hours == '00':
            hours = '12'
            am_pm_str = 'am'
        elif int(hours) > 12:
            hours = str(int(hours) - 12)
            am_pm_str = 'pm'
        else:
            am_pm_str = 'am'
        int(hours)
        int(minutes)
        answer = "It's" ""
def main():
     str1=input()"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""

# This will convert military hours to regular hours, and determine AM vs PM

reg_tens = {2:"twenty",3:"thirty",4:"forty",5:"fifty"}
teens = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
ones = {1:"oh one","2":"oh two","3":"oh three","4":"oh four","5":"oh five","6":"oh six","7":"oh seven","8":"oh eight","9":"oh nine"}
reg_ones = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 0:"twelve"}

class Solution:    
    def ClockTalker(self, input_time):
        end_str = ""
        if int(input_time.split(":")[0]) < 12:
            a="am"
            hour = int(input_time.split(":")[0])
        else:
            a="pm"
            hour = int(input_time.split(":")[0]) - 12
        minutes = int(input_time.split(":")[1])
        end_str += "It's "
        end_str += reg_ones[hour]
        if minutes == 0:
            end_str += " " + a
            return end_str
        if minutes < 10:
            end_str += " oh " + reg_ones[minutes] + " " + a
            return end_str
        if minutes < 20:
            end_str += " " + teens[minutes] + " " + a
            return end_str
        f = minutes % 10
        if f == 0:
            end_str += " " + reg_tens[int(minutes/10)] + " " + a
            return end_str
        end_str += " " + reg_tens[int(minutes/10)] + " " + reg_ones[f] + " " + a
        return end_str

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        