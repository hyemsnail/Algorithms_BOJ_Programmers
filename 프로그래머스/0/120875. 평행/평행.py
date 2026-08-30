def solution(dots):
    answer = 0
    # 6번만 조합하면 됨 - 평행이려면 x랑 y 움직이는 간격이 비례
    if (dots[0][0]-dots[1][0])/(dots[0][1]-dots[1][1]) == (dots[2][0]-dots[3][0])/(dots[2][1]-dots[3][1]):
        return 1
    if (dots[0][0]-dots[2][0])/(dots[0][1]-dots[2][1]) ==(dots[1][0]-dots[3][0])/(dots[1][1]-dots[3][1]):
        return 1
    if (dots[0][0]-dots[3][0])/(dots[0][1]-dots[3][1]) == (dots[2][0]-dots[1][0])/(dots[2][1]-dots[1][1]):
        return 1
    return 0