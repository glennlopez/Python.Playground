'''
https://classroom.udacity.com/courses/ud1110/lessons/8655bee4-19e1-4de0-8177-4f895a74b57b/concepts/6305f6e8-d28d-4120-856b-a6cb612f110e
'''
start_num = 0 #provide some start number
end_num = 13 #provide some end number that you stop when you hit
count_by = 5 #provide some number to count by
break_num = start_num

# write a while loop that uses break_num as the ongoing number to
#   check against end_num

while break_num < end_num:
    break_num += count_by
    if break_num + count_by > end_num:
        break

print(break_num)

