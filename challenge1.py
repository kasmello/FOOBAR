import sys



def solution(area):
    area = int(area)
    factors = [1, area]

    i = 1
    factors_found = False
    while not factors_found:
        if i > area/i: ##first index of factors is small factor
            factors_found = True
            
        elif area%i == 0:
            factors[0] = i
            factors[1] = area/i
            print(factors)
        i += 1
            
        
    

    print(factors)
    area_remain = area 
    dim_remain = factors #dimensions of area remaining
    output_str = ''
    
    while area_remain > 0:
    
  
        if area > 1000000:
            area_remain = 0
        else:
            sqr = factors[0]**2
            output_str += str(int(sqr)) + ','
            factors[1] = factors[1]-factors[0]
            if factors[1] < factors[0]:
                temp = factors[0]
                factors[0] = factors[1]
                factors[1] = temp
            area_remain -= sqr
    return(output_str[:-1])

hm = sys.argv[1]
print(solution(hm))