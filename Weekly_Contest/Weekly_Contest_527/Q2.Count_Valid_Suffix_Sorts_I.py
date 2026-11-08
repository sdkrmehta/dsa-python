from collections import defaultdict

def countSuffix(nums, target):
        n = len(nums)
        limit = n

        for i in range(n):
            if nums[i] != target[i]:
                limit = i
                break

        freq_diff = defaultdict(int)
        unmatched = 0
        ans = 0

        for i in range(n - 1, -1, -1):
            if i < n - 1 and target[i] < target[i + 1]:
                break

            x, y = nums[i], target[i]
            if x != y:
                if freq_diff[x] == 0:
                    unmatched += 1
                elif freq_diff[x] == -1:
                    unmatched -= 1
                freq_diff[x] += 1

                if freq_diff[y] == 0:
                    unmatched += 1
                elif freq_diff[y] == 1:
                    unmatched -= 1
                freq_diff[y] -= 1

            if i <= limit and unmatched == 0:
                ans += 1

        return ans

print(countSuffix(nums = [1,2,3], target = [3,2,1]))