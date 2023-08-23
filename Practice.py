# student_marks = {
#     'Krishna' :[67 ,68 ,69],
#     'Arjun':[ 70, 98, 63],
#     'Malika': [52 ,56 ,60]
# }
# query_name = input()
# for key,value in student_marks.items():
#     if key == query_name:
#          sum = 0
#          count = 0
#          for i in value:
#              sum = sum + i
#              count += 1
#          avg = sum / count
#          avg = format(avg,".2f")
#          print(avg)
#################################################################
#Task2
def wrap(string,max_width):
    result = ""
    count = 0
    for s in string:
        result = result + s
        count += 1
        if count == max_width:
            count = 0
            result += '\n'
    return result
string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)