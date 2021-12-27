from geopy.distance import geodesic


# 학원의 위도 / 경도 를 tuple로.
coord_neppplus = (37.57781506100433, 127.03359166993611 )  # 여러개의 값을 넣으면, tuple 형태로 만들어짐. tuple : 내용 변경 불가능한 list

coord_home = ( 37.613980692808006, 126.92948953647392 )

print( geodesic(coord_neppplus, coord_home).km )