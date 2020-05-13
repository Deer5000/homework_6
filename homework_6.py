'''     Problem #1

Given the array candies and the integer extraCandies, where candies[i] 
represents the number of candies that the ith kid has. For each kid check 
if there is a way to distribute extraCandies among the kids such that he or 
she can have the greatest number of candies among them. Notice that multiple 
kids can have the greatest number of candies.
      
'''
class Solution(object):
  def kidsWithCandies(self, candies, extraCandies):
    most = max(candies)
    for kid in candies:
      if extraCandies + kid >= most:
        print(True)
      else:
        print(False)

'''   Problem #2
Given an array of integers arr, a lucky integer is an integer
 which has a frequency in the array equal to its value.
Return a lucky integer in the array. If there are multiple
lucky integers return the largest of them. If there is
no lucky integer return -1.
'''

class Solution(object):
    def findLucky(self, arr):
        count = (arr)
        result = -1
        for k, v in count.iteritems():
            if k == v:
                result = max(result, k)
        return result
