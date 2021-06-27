'''
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
**제한 조건**
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
'''
def solution(arr1, arr2):
    answer = []
    for each in range(len(arr1)):
       answer.append([])
       for eachInd in range(len(arr1[each])):
           answer[each].append(arr1[each][eachInd] + arr2[each][eachInd])
    return answer

'''
정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
제한 조건
num은 int 범위의 정수입니다.
0은 짝수입니다.
'''

'''
길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. 
a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.
이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)
**제한사항**
a, b의 길이는 1 이상 1,000 이하입니다.
a, b의 모든 수는 -1,000 이상 1,000 이하입니다.
'''