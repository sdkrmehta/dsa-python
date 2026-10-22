import heapq

def numberGame(nums):
    heapq.heapify(nums)
    ans = []

    while nums:
        alice_min = heapq.heappop(nums)
        bob_min = heapq.heappop(nums)

        ans.append(bob_min)
        ans.append(alice_min)

    return ans

print(numberGame(nums = [5,4,2,3]))
print(numberGame(nums = [5,2]))
    
    
    
    
    
    # nums = sorted(nums)
    # ans = []

    # for i in range(0, len(nums), 2):
    #     alice_min = nums[i]
    #     bob_min = nums[i + 1]

    #     ans.append(bob_min)
    #     ans.append(alice_min)

    # return ans