def solution():
    concentration, mass = [],[]
    for i in range(5):
        test_case = input(f'{i+1}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')
        if test_case == 'Done':
            break
        a, b = test_case.split()
        a = int(a.replace("%",""))
        b = int(b.replace("g",""))
        concentration.append(round(float((b*a) / 100), 2))
        mass.append(round(float(b),2))

    return (f'{(sum(concentration) / sum(mass)) * 100}% {sum(mass)}g')
