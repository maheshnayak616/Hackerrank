'''
Created on 18-Jul-2015

@author: mahesh.nayak
'''
import sys
def get_sorted_formatted_mobile_list(list_of_mobile):
    def format_number(number):
        return "+91 " + number[-10 : -5] + " " + number[-5 : ] 
    def sort_numbers(list_of_mobile):
        x = [format_number(y) for y in list_of_mobile]
        x.sort()
        return x
    return sort_numbers

@get_sorted_formatted_mobile_list
def test(list_of_mobile_numbers):
    return list_of_mobile_numbers

a = int(sys.stdin.readline().strip())
list_of_mobile_numbers = []
while(a):
    list_of_mobile_numbers.append(sys.stdin.readline().strip())
    a = a -1 
q =  test(list_of_mobile_numbers)
for s in q:
    print s