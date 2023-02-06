
from pipegrid import Pipes



map = Pipes([["es","ew","e+","sw","s+"], ["ns","s+","w+","new","e+"], ["esw","nes","nsw+","esw","w+"], ["es","new","ne","nes","new"], ["s+","nw","e+","s+","s+"]], 100)
map.set_fill_state(2,2, True)
map.set_fill_state(2,3, True)
map.set_fill_state(1,2, True)
map.set_fill_state(1,1, True)
map.set_fill_state(1,3, True)
map.set_fill_state(0,3, True)

map.draw()

print("before: {}".format(map.get_cell(2,2)))
map.rotate_cw(2,2)
map.set_fill_state(3,2, True)
map.set_fill_state(3,3, True)
map.set_fill_state(4,2, True)
map.set_fill_state(4,3, True)
map.set_fill_state(2,3, False)
print("after: {}".format(map.get_cell(2,2)))
map.draw()

map.rotate_cw(3,2)
map.set_fill_state(4,2, False)
map.draw()

map.rotate_ccw(2,1)
map.set_fill_state(2,1, True)
map.draw()

map.rotate_cw(3,1)
map.set_fill_state(3,1, True)
map.set_fill_state(3,0, True)
map.set_fill_state(2,0, True)
map.draw()

map.rotate_cw(4,1)
map.rotate_cw(4,1)
map.set_fill_state(4,1, True)
map.draw()

map.rotate_ccw(4,2)
map.set_fill_state(4,2, True)
map.draw()

map.rotate_cw(4,0)
map.draw()

map.rotate_ccw(3,0)
map.set_fill_state(2,0, False)
map.set_fill_state(4,0, True)
map.draw()

map.rotate_ccw(0,2)
map.draw()

map.rotate_ccw(0,3)
map.set_fill_state(0,2, True)
map.set_fill_state(0,1, True)
map.set_fill_state(0,0, True)
map.set_fill_state(1,0, True)
map.draw()

map.rotate_ccw(1,2)
map.draw()

map.rotate_cw(1,3)
map.rotate_cw(1,3)
map.set_fill_state(1,4, True)
map.draw()

map.rotate_cw(2,0)
map.rotate_cw(2,0)
map.set_fill_state(2,0, True)
map.draw()

map.rotate_ccw(2,4)
map.draw()

map.rotate_ccw(2,3)
map.rotate_ccw(2,3)
map.set_fill_state(2,3, True)
map.set_fill_state(2,4, True)
map.draw()

map.rotate_ccw(3,4)
map.rotate_ccw(3,4)
map.set_fill_state(3,4, True)
map.draw()

map.rotate_cw(4,4)
map.rotate_cw(4,4)
map.draw()

map.rotate_ccw(4,3)
map.set_fill_state(4,4, True)
map.draw()

map.rotate_ccw(0,4)
map.set_fill_state(0,4, True)
map.draw()