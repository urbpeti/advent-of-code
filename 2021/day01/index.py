nums = []
with open('input.txt') as f:
  for l in f:
    nums.append(int(l))

def get_increase(nums):
  prev = next(nums)
  increased = 0
  for n in nums:
    if n > prev:
      increased += 1
    prev = n
  return increased

print(f'Task 1 solution: {get_increase(iter(nums))}')

nums2 = (sum(nums[i-2:i+1]) for i, n in enumerate(nums) if i >= 2)
print(f'Task 2 solution: {get_increase(nums2)}')
