from typing import List

#========================
#빗물 트래핑
#투 포인터 방식
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

'''

#디버깅용 코드
#높이 계산은 현재의 최대 높이에서 현재 높이를 빼는 것 
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        print("left:{}".format(left))
        print("right:{}".format(right))
        print("left_max:{}".format(height[left]))
        print("right_max:{}".format(height[right]))


        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                print("move right -> :{} added".format(left_max - height[left]))
                volume += left_max - height[left]
                left += 1
            else:
                print("move left <- : {} added".format(left_max - height[left]))
                volume += right_max - height[right]
                right -= 1
        return volume





'''
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume

'''



if __name__ == "__main__":

    #===========================
    #물 쌓기
    a = Solution()
    b= a.trap([0,1,0,2,1,0,3,2,1,2,1])
    print(b)
    #===========================
