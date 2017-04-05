# This is an O(n) solution since only one window is iterated through and then every other time
# the element being removed from the window and the element being added to the window are examined.
def find_subranges(n, k, prices):
    # inc_array and dec_array store the lengths of each subrange that is increasing or decreasing, respectively
    inc_array = []
    dec_array = []
    inc_length = 0
    dec_length = 0
    for start_point in range(n - k + 1):
        current = start_point
        total = 0
        # Changed this
        if start_point == 0:
            for index in range(1, k):
                # Check if this is a new subrange
                if inc_length == 0 and dec_length == 0:
                    if prices[start_point + index] < prices[current]:
                        dec_length += 1
                    elif prices[start_point + index] > prices[current]:
                        inc_length += 1
                elif inc_length > 0:
                    if prices[start_point + index] < prices[current]:
                        inc_array.append(inc_length)
                        inc_length = 0
                        dec_length += 1
                    elif prices[start_point + index] > prices[current]:
                        inc_length += 1
                elif dec_length > 0:
                    if prices[start_point + index] < prices[current]:
                        dec_length += 1
                    elif prices[start_point + index] > prices[current]:
                        dec_array.append(dec_length)
                        dec_length = 0
                        inc_length += 1
                # If end of window, append both lengths to each array.
                if index == k - 1:
                    inc_array.append(inc_length)
                    dec_array.append(dec_length)

                current += 1
        # I believe this is the correct way to calculate the total subranges contained in the a subrange of given length.
        for x in inc_array:
            num = x
            while num > 0:
                total += num
                num -= 1
        for y in dec_array:
            while y > 0:
                total -= y
                y -= 1
        print(total)
        # This is the new logic that adjusts both arrays depending on whether the window starts with an increasing
        # or decreasing subrange and also examines the new subrange at the end of the window.
        if start_point + k < n:
            if prices[start_point] < prices[start_point+1]:
                inc_array[0] -= 1
            elif prices[start_point] > prices[start_point+1]:
                dec_array[0] -= 1
            if prices[start_point + k] > prices[start_point + k - 1]:
                inc_array[len(inc_array) - 1] += 1
                dec_array.append(0)
            elif prices[start_point + k] < prices[start_point + k - 1]:
                dec_array[len(dec_array) - 1] += 1
                inc_array.append(0)
        if len(dec_array) > 0:
            if dec_array[0] == 0:
                del dec_array[0]
        if len(inc_array) > 0:
            if inc_array[0] == 0:
                del inc_array[0]


if __name__ == '__main__':
    inputfile = open('input.txt', 'r')
    n, k = [int(y) for y in inputfile.readline().split(' ')]
    prices = [int(x) for x in inputfile.readline().split(' ')]
    find_subranges(n, k, prices)
