def recursive_function(i):
    # 100 번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 함수에서', i + 1, '번쨰 재귀함수 종료')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다')


recursive_function(1)