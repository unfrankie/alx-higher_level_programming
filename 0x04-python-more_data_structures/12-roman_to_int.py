#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    nums = []
    chif = 0

    if not roman_string or type(roman_string) is not str:
        return 0
    else:
        for elem in roman_string:
            nums.append(roman_dict[elem])

        for num in nums:
            if len(nums) == 1:
                chif = num
            elif nums[-1] < nums[0]:
                chif += num
            elif nums[-1] > nums[0]:
                subs = sum(nums[:-1])
                chif = nums[-1] - subs
        return chif
