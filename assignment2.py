import socket

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        age = currentYear - self.year
        print(f'Your age is {age}')

    def listAnniversaries(self):
        today_year = 2024
        anniversaries = [i for i in range(10, today_year - self.year, 10)]
        return anniversaries

    def modifyYear(self, n):
        year_str = str(self.year)
        result = year_str[:2] * n + year_str[0::2] * n
        return result

    @staticmethod
    def checkGoodString(string):
        if len(string) >= 9 and string[0].islower() and string.count('0') == 1 and string.isalnum():
            return True
        else:
            return False

    @staticmethod
    def connectTcp(host, port):
        try:
            with socket.create_connection((host, port)) as sock:
                return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False

# Example usage:
a = Assignment2(2000)
a.tellAge(2024)

ret1 = a.listAnniversaries()
print(ret1)

ret2 = a.modifyYear(5)
print(ret2)

ret3 = Assignment2.checkGoodString("f1obar0more")
print(ret3)

ret4 = Assignment2.checkGoodString("foobar0more")
print(ret4)

ret5 = Assignment2.connectTcp("www.google.com", 80)
if ret5:
    print("Connection established correctly")
else:
    print("Some error")
