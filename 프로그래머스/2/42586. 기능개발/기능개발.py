def solution(progresses, speeds):
    answer = []
    
    # 이전 배포일 초기화
    prev_deploy = 0
    
    for i in range(len(progresses)):
        # 배포에 필요한 일 수 계산
        deploy = (100 - progresses[i]) // speeds[i]
        # 작업이 완료되기 위해 추가로 남은 일 수
        deploy_check = (100 - progresses[i]) % speeds[i]
        
        if deploy_check > 0:
            # 작업이 덜 끝났으므로 하루 추가
            deploy += 1

        if deploy > prev_deploy:
            # 뒤에 배포가 더 오래 걸릴 경우
            answer.append(1)
            prev_deploy = deploy
        else:
            # 앞에 배포가 더 오래 걸릴 경우
            answer[-1] += 1

    return answer