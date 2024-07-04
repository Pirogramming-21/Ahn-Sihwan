# class Date:
#     @staticmethod
#     def is_date_valid(date_string):
#         year, month, day = map(int, date_string.split("-"))
#         return month <=12 and day <= 31

# if Date.is_date_valid('2000-13-31'):
#     print('올바른 날짜 형식입니다.')
# else:
#     print('잘못된 날짜 형식입니다.')


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    # 정답 코드
    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour<=24 and minute<=59 and second<=60

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time = cls(hour, minute, second)
        return time


time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')