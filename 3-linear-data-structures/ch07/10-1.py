from typing import List

#n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라 .
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서 부터 오름차순으로 페어를 만들어 합 계산
            pair.append(n)
            if len(pair) == 2:

                sum += min(pair)
                pair = []

        return sum


