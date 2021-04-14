from pandas import Series

high = Series([42800, 42700, 42100, 42950, 43000])
low = Series([42150, 42150, 41300, 42150, 42350])

diff = high - low
print(diff)