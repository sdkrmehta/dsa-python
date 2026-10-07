# The isBadVersion API is already defined in leetcode.
# def isBadVersion(version: int) -> bool:

# def firstBadVersion(n):
#     left = 0
#     right = n

#     while left < right:
#         mid = (left + right) // 2
#         if isBadVersion(mid):
#             right = mid
#         else:
#             left = mid + 1
    
#     return left