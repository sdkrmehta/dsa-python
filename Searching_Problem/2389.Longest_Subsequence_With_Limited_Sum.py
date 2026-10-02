def answerQueries(nums, queries):
    nums.sort()
    ans = []

    for query in queries:
        summ = 0
        count = 0

        for num in nums:
            summ += num

            if summ > query:
                break
            else:
                count += 1
        ans.append(count)
        
    return ans

print(answerQueries(nums = [4,5,2,1], queries = [3,10,21]))