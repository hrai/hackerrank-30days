from datetime import datetime


class Solution(object):

    def calc(self, ret_dt, due_dt):
        try:
            r_arr = list(map(int, ret_dt.split()))

            d_arr = list(map(int, due_dt.split()))

            if len(str(d_arr[2])) < 4:
                d_arr[2] += 2000
            if len(str(r_arr[2])) < 4:
                r_arr[2] += 2000

            returned_date = datetime(r_arr[2], r_arr[1], r_arr[0])
            due_date = datetime(d_arr[2], d_arr[1], d_arr[0])

            date_diff = returned_date - due_date

            if returned_date <= due_date:
                return 0
            elif returned_date.month == due_date.month and returned_date.year == due_date.year:
                return date_diff.days * 15
            elif returned_date.year == due_date.year:
                return (returned_date.month - due_date.month) * 500
            else:
                return 10000
        except:
            return 0

# sln=Solution()
# ret=input()
# due=input()
# print(sln.calc(ret, due))
