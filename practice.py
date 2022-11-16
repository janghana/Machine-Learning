#!/usr/bin/env python
# coding: utf-8

# ## 1

# In[14]:


import sys

################ ################ ################ ################
# Algorithm 문제 2번 설명
# 이중 for문과 그 안에 sum method를 추가하여 O(n^3)의 복잡도로 구현하였다.
# 이중 for문을 통하여 모든 sum 들의 값을 sum_list에 저장하고 정렬한 뒤 line번째
# 값을 받아 해당 line번째 값을 index에서 -1 하여 출력한다.
################ ################ ################ ################

# main() method

def main(data_list, line):
    sum_list = []
    for i in range(0,len(data_list)):
        for j in range(i,len(data_list)):
            sum_list.append(sum(data_list[i:j+1]))
    sum_list.sort()
    print(sum_list[line-1])

# __main__
if __name__ == "__main__":
    data_list = list(map(int, input().split()))
    line = int(input())
    main(data_list, line)

# In[405]:


import sys
from collections import Counter

################ ################ ################ ################
# Algorithm 문제 3번 설명
# __main__에서 data_list에 입력 받은 배열의 값을 list로 바꾸어 Counter처리하여 받는다.
# 그리고 main()함수를 호출하여 해당 Counter로 변환된 list를 인자로 넘겨주고 main()에선 
# 최종 dinosaur의 값을 반환한다.
# main() method에서 result에 최종 값을 넣고, 해당 data_list가 각각 0일 경우, 1일 경우 예외를
# 처리해주고, 그 외의 경우와 해당 경우를 포함하여 default case로 값을 고려한다.
# 0을 받을 경우 자기 자신이므로 1씩 카운트 하면 되고, 1일 경우 여러 개가 들어올 경우,
# 이를 테면, 1 1 1 or 1 1 1 1 이 둘 다 최소 4마리로 가정되므로 같은 값이 나와야 하는 경우가 그렇다.
# 그리하여 for문과 if문을 사용하여 result에 값을 더해준다.
# 그리고 default 경우를 고려하여 값이 여러 번 들어오는 경우와 그렇지 않은 경우를 나누어
# 계산해주고, 최종 result 값을 return하여 넘겨준다.
################ ################ ################ ################

# main() method
def main(data_list):
    result = 0
    for i in data_list:
        if i == 0:
            result += data_list[i]
            continue
        if i == 1:
            for _ in range(0, int(data_list[i] / (i+1))):
                result += i + 1
            if data_list[i] % 2 == 1:
                result += i + 1
            continue
        for _ in range(1, int(data_list[i] / (i+2)+1)):
            result += i + 1
        result += i + 1
    return result

# __main__
if __name__ == "__main__":
    data_list = Counter(list(map(int, input().split())))
    print(main(data_list))

# ## 2

# In[12]:


################ ################ ################ ################
# Algorithm 문제 1번 설명
# fibonacci의 특성을 고려하여 n번째 fibonacci 수는 n-1번, n-2번째 수의 합으로 이루어지므로,
# 아래와 같이 재귀적으로 구성하였고, n == 0, n == 1인 경우로 base case를 두었다.
################ ################ ################ ################
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else :
        return fibonacci(n-2) + fibonacci(n-1)

# main() method
def main():
    a = int(input())
    print(fibonacci(a))
    
if __name__ == "__main__":
    main()

# In[69]:


################ ################ ################ ################
# Algorithm 문제 2번 설명
# 유클리드 호제법
# 입력 받은 수 a, b에 대하여 b를 a로 나눈 나머지로 다시 a를 나누고
# 계속해서 재귀적으로 구현하였다.
################ ################ ################ ################
def uc(a,b):
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    else:
        return uc(b%a,a)
    
def main():
    a,b = map(int, input().split())
    print(uc(a,b))
    
if __name__ == "__main__":
    main()

# In[66]:


### ################ ################ ################
# Algorithm 문제 3번 설명
# 해당 경우들에 대하여 2 <= n <= 9인 경우 even 경우와 odd 경우로 나눌 수 있다.
# 2, 4, 6, 8인 경우에 대해서 수의 앞 뒤 경우는 0이 들어갈 수 없고 나머지 안 쪽의 경우는 들어갈 수 있음을 파악하는 것이
# 이 과제의 핵심이라고 생각된다. 그리하여 다음과 같은 예시를 들 수 있다.
# 가령, n = 4이면, ㅁㅁㅁㅁ으로 "ㅁ11ㅁ" "ㅁ69ㅁ""ㅁ96ㅁ""ㅁ00ㅁ" "ㅁ88ㅁ" 안 쪽의 경우 5개의 경우의 수,
# 양쪽 끝 경우는 4가지 이다. 이를 파악하여 아래와 같이 짝수인 경우는 마지막에 4를 곱하여 양쪽의 경우를 고려해줬다.
# 이는 2인 경우에도 바로 4로 들어갈 수 있기 때문에 base case를 num == 2로 설정한 이유가 된다.
# 그리고 홀수인 경우는,
# 가령, n = 5이면, ㅁㅁㅁㅁㅁ으로 "ㅁㅁ0ㅁㅁ" "ㅁㅁ8ㅁㅁ" "ㅁㅁ1ㅁㅁ"으로 3가지, 그리고 위와 같이 5가지 경우, 그리고
# 양쪽 4가지 경우를 고려하여 num == 3일 경우 3 * 4로 고려하였다.
# num이 2씩 빠질 때마다 5씩 곱해주어 계산하여 재귀적으로 풀이하였다.
################ ################ ################ ################
def rotate(num):
    # even
    if num == 2:
        return 4
    # odd
    elif num == 3:
        return 3 * 4
    else:
        return rotate(num - 2) * 5
    
# main() method
def main():
    num = int(input())
    print(int(rotate(num)))
    
if __name__ == "__main__":
    main()

# ## 3

# In[44]:


### ################ ################ ################
# Algorithm 문제 1번 설명
# Anagram
# 문자열을 sort하여 문자열이 같은지 비교한다.
################ ################ ################ ################
def func(str1, str2):
    result1 = []
    result2 = []
    for i in range(0, len(str1)):
        result1.append(str1[i])
    for i in range(0, len(str2)):
        result2.append(str2[i])
    result1.sort()
    result2.sort()
    if result1 == result2:
        return "True"
    else :
        return "False"
    
# main() method
def main():
    str1, str2 = input().split(" ")
    print(func(str1, str2))
    
if __name__ == "__main__":
    main()

# In[7]:


### ################ ################ ################
# Algorithm 문제 2번 설명
# dictionary에 dictionary 형태로 저장된 List 값들을 넣는다. 각각 result1, result2를
# 각각 key, value를 넣는다. 그리고 이미 나온 key 값이 나온 경우, 그 key 값에 대한 value 값이
# 다른 값으로 나와 있다면 False를 return하고 모든 경우에 대해 그것이 아니면 True를 return 한다.
################ ################ ################ ################
def func(str1, str2):
    
    result1 = []
    result2 = []
    dictionary = {}
    for i in range(0, len(str1)):
        result1.append(str1[i])
    for i in range(0, len(str2)):
        result2.append(str2[i])
        
    dictionary[result1[0]] = str(result2[0])

    
    for i in range(1,len(result1)):
        if result1[i] == dictionary.get(result1[i]):
            if dictionary.get(result1[i]) != result2[i]:
                return "False"
        dictionary[result1[i]] = str(result2[i])
    return "True";

# main() method
def main():
    str1, str2 = input().split(" ")
    print(func(str1, str2))
    
if __name__ == "__main__":
    main()

# In[ ]:


### ################ ################ ################
# Algorithm 문제 3번 설명
# 이번 과제는 삼중 for문을 이용하여 풀이하였다.
# result에 data의 문자열들을 하나씩 넣는다. 그리고 문자열의 길이가 0이거나 1이면 True를 반환한다.
# 그리고 만약, 받은 num이 3이라면 3이하의 개수를 제외하는 경우의 수를 고려해 주어야 하므로,
# for문으로 값을 하나씩 줄여서 고려해 주었다. 그리고 for문 안에 이중 for문으로 하나 씩,
# list를 combinations해서 풀어준다. 그리고 combi에 하나씩 회문인지를 이중 for문으로 모두 고려한다.
################ ################ ################ ################
from collections import Counter
import math
from itertools import combinations

def func(data, num):
    result = []
    for i in range(0, len(data)):
        result.append(data[i])
    
    if len(data) - num == 0 or len(data) - num == 1:
        return "True"
    
    for f in range(0, num):
        combi = list(combinations(result, len(result)-num+f))
        for i in combi:
            k = 1
            for j in range(0,len(i)):
                if i[j] != i[len(i)-k]:
                    break;
                elif (len(i) - k) == (len(i)//2):
                    return "True"
                elif i[j] == i[len(i) - k]:
                    k += 1
                    continue
    return "False"

# main() method
def main():
    data, num = input().split(" ")
    print(func(data, int(num)))
    
if __name__ == "__main__":
    main()

# In[ ]:




# In[ ]:




# In[ ]:



