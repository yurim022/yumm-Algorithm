def solution(routes):
    #정렬과 그리디를 사용해서 푸는 문제
    #exit이 빠른 순서대로 정렬
    routes.sort(key = lambda x : x[1])
    numOfCamera = 0
    n = len(routes)
    meetCamera = [False]*n
    cameraAt = 0
    for i in range(n):
        if meetCamera[i] : #이미 카메라를 만난것 제외
            continue
        cameraAt = routes[i][1] # exit에 있는 위치에 카메라 설치
        numOfCamera += 1 #설치한 카메라 개수 증가
        meetCamera[i] = True
        for j in range(i+1,n):
            #카메라 범위안에 위치하면 true 표시
            if routes[j][0] <= cameraAt and routes[j][1] >= cameraAt:
                meetCamera[j] = True

    return numOfCamera






## someone's code...its so clear
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]: #install camera when start of routes is larger than camera location.
            answer += 1
            last_camera = route[1]

    return answer
