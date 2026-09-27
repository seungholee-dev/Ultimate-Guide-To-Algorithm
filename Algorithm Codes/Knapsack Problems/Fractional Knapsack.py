#Fractional Knapsack Problem
'''
Suppose there is a thief. He wants to loot a vault and carry a sack with capacity M. There are different quantities of gold, where A[i] represents the value of the i-th quantity of gold and W[i] represents its weight. We need to help the thief collect as much profit as possible while keeping the total weight within the maximum capacity of his sack.

Time Complexity: O(NlogN) 
Space Complexity: O(N) 
where N is the number of gold items

Approach: For this problem, we will simply choose those quantities of gold that provide more value per unit weight.

For example: Suppose there are two quantities of gold:

         			Gold A        Gold B

Value: 				  100           200
Weight:                10            40
Value/Weight:          10             5

Although the value of Gold B is higher, Gold A provides more value per unit weight. Therefore, we should prioritize Gold A.

To achieve such ordering, we can sort the gold items according to the ratio value[i]/weight[i] in decreasing order.

Since this is the Fractional Knapsack problem, if the remaining capacity is not enough to take an entire quantity of gold, we can take only the fraction that fits in the sack.
Our goal is to return the maximum profit possible for the thief.
'''



def fractional_knapsack(cost : list, weight : list, capacity : int) -> float:
	#Sorting the array in descending order of cost[i]/weight[i]
	n=len(cost)
	index = [k for k in range(n)]
	index.sort(key = lambda i: cost[i]/weight[i], reverse = True)
	
	ans=0.0
	load=0.0
	for i in index:
		if load + weight[i] > capacity:
			# if the adding the gold item in the current load exceeds the capacity then we take only a part of the gold
			ans+=(cost[i]/weight[i])*(capacity - load)
			break
		# we take all the gold if it does not exeed the capacity
		ans+=cost[i]
		load+=weight[i]
	
	return ans
		
	
if __name__ == "__main__":
	cost   = [60, 100, 120]
	weight = [10, 20, 30]
	capacity = 50
	
	print(f"Maximum profit possible for the thief = {fractional_knapsack(cost,weight,capacity)}")
	
	
	
	
	
	
	
	
	
	
	
	
	

