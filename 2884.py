hour,minute = map(int,input().split())

h = [x for x in range(24)]
m = [x for x in range(60)]

h_index = h.index(hour)
m_index = m.index(minute)

if m_index - 45 < 0:
    print(h[h_index-1],m[m_index-45])
else:
    print(h[h_index], m[m_index - 45])
