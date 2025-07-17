#Find All Pairs in a List That Sum to Target
user_input = list(map(int,input("enter a number:").split(",")))
target = int(input("enter a target:"))
def find_pairs(nums, target):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = (nums[i], nums[j])
                if pair not in result and (pair[1], pair[0]) not in result:
                    result.append(pair)

    return result
print("enter a values:",find_pairs(user_input,target))