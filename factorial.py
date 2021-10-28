#   part 1 - Calculate the factorial of a given number
#   part 2 - Find the number of trailing zeroes in that number

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)

def find_trailing_zeroes(num):
    #fac = fact(num)
    count = 0
    i = 5
    # while fac % 10 == 0:
    #     count += 1
    #     fac = fac/10
    while num//i != 0:          # 5! = 5 * 4 * 3 * 2                                                    => number of 5's = 1
                                # 10!= 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2                               => number of 5's = 2
                                # 15!= 15 * 14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2      => number of 5's = 3

        count += int(num/i)
        i *= 5
            
    return count

num1 = int(input("Enter a number: "))
print(fact(num1))
print(find_trailing_zeroes(num1))