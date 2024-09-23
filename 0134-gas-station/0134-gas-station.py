class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum (cost):
            return -1
        start = 0
        tank = 0
        total_gas_less = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                total_gas_less += tank
                start = i + 1
                tank = 0
        if (tank - total_gas_less) >= 0:
            return start
        else:
            return -1