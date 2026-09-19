def findRestaurant(list1, list2):
    count = {}

    for i in range(len(list1)):
        count[list1[i]] = i

    ans = float('inf')
    result = []

    for i in range(len(list2)):
        if list2[i] in count:
            index_sum = count[list2[i]] + i

            if index_sum < ans:
                ans = index_sum
                result = [list2[i]]

            elif index_sum == ans:
                result.append(list2[i])

    return result

print(findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
print(findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))
print(findRestaurant(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]))

# def findRestaurant(list1, list2):
#     ans = float('inf')
#     result = []

#     for i in range(len(list1)):
#         for j in range(len(list2)):
#             if list1[i] == list2[j]:
#                 if i + j < ans:
#                     ans = i + j
#                     result = [list1[i]]
#                 elif i + j == ans:
#                     result.append(list1[i])

#     return result