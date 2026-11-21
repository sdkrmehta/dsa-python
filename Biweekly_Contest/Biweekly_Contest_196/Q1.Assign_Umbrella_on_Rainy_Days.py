def assignUmbrella(rain):
    alice = 0
    bob = 0
    ans = []
    n = len(rain)

    for i in range(n):
        alice_need = (i < n - 1 and rain[i] == 1 and rain[i + 1] == 1)
        bob_need = (rain[i] == 1)

        if alice_need and bob_need:
            if alice <= bob:
                ans.append("Alice")
                alice += 1
            else:
                ans.append("Bob")
                bob += 1

        elif alice_need:
            ans.append("Alice")

        elif bob_need:
            ans.append("Bob")
            bob += 1

        else:
            ans.append("None")
            
    return ans

print(assignUmbrella(rain = [1,1,0,1,1]))