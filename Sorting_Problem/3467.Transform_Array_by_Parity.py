def transformArray(nums):
        ans = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                ans.append(0)
            else:
                ans.append(1)
        ans.sort()

        return ans

print(transformArray(nums = [7, 6, 8, 9, 5]))