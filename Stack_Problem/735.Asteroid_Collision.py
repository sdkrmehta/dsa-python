def asteroidCollision(asteroids):
    stack = []

    for num in asteroids:
        alive = True

        while stack and stack[-1] > 0 and num < 0:
            if stack[-1] < abs(num):
                stack.pop()
            elif stack[-1] == abs(num):
                stack.pop()
                alive = False
                break
            else:
                alive = False
                break

        if alive:
            stack.append(num)

    return stack

print(asteroidCollision(asteroids = [5,10,-5]))        
print(asteroidCollision(asteroids = [8,-8]))        
print(asteroidCollision(asteroids = [10,2,-5]))        
print(asteroidCollision(asteroids = [3,5,-6,2,-1,4]))        