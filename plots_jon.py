from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from pylab import *

def hor_line(y, w, c='k'):
	plot([-w/2, w/2], [y, y], c)

def vert_line(x, w, c='k'):
	plot([x, x], [-w/2, w/2], c)


small_tick = 0.25
large_tick = 1

hor_line(0, 2)

x = linspace(-1, 1, 15, endpoint=False)
x += (x[1] - x[0])*0.2394287
for x_i in x:
	vert_line(x, small_tick, 'r')

x = linspace(-1, 1, 4, endpoint=False)
x += (x[1] - x[0])*0.623846
for x_i in x:
	vert_line(x, large_tick)



axis('off')

show()