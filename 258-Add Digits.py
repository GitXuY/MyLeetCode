class Solution(object):
        def addAllNum(self, num):
                result = 0
                while True:    
                        remainder = num % 10;
                        quotient = num / 10;
                        result = result + remainder;
                        if quotient < 10:
                                result = result + quotient
                                return result
                        else:
                                num = quotient
                                
        def addDigits(self, num):
                while True:
                        num = self.addAllNum(num);
                        if num < 10:
                                return num
			

        
