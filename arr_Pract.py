arr = [2,5,3,6,8,7,9]
prefix_sum= [0]*len(arr)
prefix_sum[0]= arr[0]
for i in range(1,len(arr)):
    prefix_sum[i]= prefix_sum[i-1]+ arr[i]

print(prefix_sum)

arr = [2,5,3,6,8,7,9]
n= len(arr)
suffix= [0]*n
for i in range(n):
    for j in range(i,n):
        suffix[i]= suffix[i]+arr[j]

print(suffix)



arr=[1,2,3,4]
n= len(arr)
for i in range(n):
    for j in range(i,n):
        for k in range(i,j+1):
            print(arr[k],end=" ")
        print()


arr = [3,4,-5,8,-12,7,6,-2]
n = len(arr)

maxi = float("-inf")  # largest subarray sum
for i in range(n):
    prefix = 0
    for j in range(i, n):
        prefix += arr[j]
        maxi = max(prefix, maxi)

print("Largest Subarray Sum:", maxi)



arr = [3,4,-5,8,-12,7,6,-2]  #kadan's algorithm
n = len(arr)
prefix=0
maxi = float("-inf")  # largest subarray sum
for i in range(n):
    prefix += arr[i]
    maxi = max(prefix, maxi)
    if prefix<0:
        prefix=0

print("Largest Subarray Sum:", maxi)



arr = [1, 2, 90, 10, 110]
n = len(arr)
max_diff = arr[1]-arr[0]  # maximum difference 
for i in range(n):
    for j in range(i+1,n):
        if (max_diff<arr[j]-arr[i]):
            max_diff = arr[j]-arr[i]

print(max_diff)




arr= [4,2,0,5,2,6,2,3]
n= len(arr)
left_max= [0]*n        # rain water
right_max=[0]*n
water_trap= 0
left_max[0]= arr[0]
for i in range(1,n):
    left_max[i]= max(left_max[i-1],arr[i])
right_max[n - 1] = arr[n - 1]
for i in range(n-2,-1,-1):
    right_max[i]= max(right_max[i+1],arr[i])
for i in range(n):
    water_trap= water_trap + min(left_max[i],right_max[i])- arr[i]

print(water_trap)


class Solution:
    def segregate0and1(self, arr):
        n = len(arr)
        start = 0     # two pointer
        end = n - 1

        while start < end:
            if arr[start] == 0:
                start += 1
            else:
                if arr[end] == 0:
                    arr[start], arr[end] = arr[end], arr[start]
                    start += 1
                    end -= 1
                else:
                    end -= 1

        return arr
arr = [0, 1, 0, 1, 1, 0, 0, 1]
solution = Solution()
print(solution.segregate0and1(arr))


numbers= [1,2,6,7,8,9]
target= 15
start = 0
end = len(numbers) - 1
while (start < end):
    if numbers[start] + numbers[end] == target:
        print([start + 1, end + 1])  # two sum array
        break
    elif numbers[start] + numbers[end] < target:
        start += 1
    else:
        numbers[start] + numbers[end] > target
        end -= 1


