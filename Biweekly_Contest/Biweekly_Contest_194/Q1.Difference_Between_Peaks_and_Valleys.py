def peakValleyDifference(nums):
        peak = []
        valley = []

        for i in range(1, len(nums) -1):
            if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
                peak.append(nums[i])
            elif nums[i] < nums[i + 1] and nums[i] < nums[i - 1]:
                valley.append(nums[i])

        return sum(peak) - sum(valley)

print(peakValleyDifference(nums = [1,5,2,4,1,3,0]))
print(peakValleyDifference(nums = [-5,-6,-1,-2,5,3,2]))
print(peakValleyDifference(nums = [6,5,2,5,5,3,6]))