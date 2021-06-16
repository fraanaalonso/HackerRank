from collections import defaultdict

def largestRectangle(h):


    #We should reduce the complexity
    h.sort()
    k = 1
    d = defaultdict(list)
    for i in range(1, len(h)):
        a = []
        for j in range(i - 1, len(h)):
            a.append(h[i-1] * k)
            d[i] = a
            k+=1
        k = 1
    a = []
    for x, v in d.items():
        a.append(max(v))
    return max(a),d

def largestRectangle1(heights):
    stack = list()
    index = 0
    largest_rectangle = 0
    while index < len(heights):
        if (not stack) or (heights[stack[-1]] <= heights[index]):
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            largest_rectangle = max(largest_rectangle, area)

    while stack:
        top_of_stack = stack.pop()
        area = (heights[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))
        largest_rectangle = max(largest_rectangle, area)

    return largest_rectangle



print(largestRectangle1([1,2,3,4,5]))