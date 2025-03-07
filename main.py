import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

#Natural frequency
omega = 1
#Daming term
gamma = 0.1

def vField(x, y):
    u = y
    v = -omega**2*np.sin(x) - gamma*y
    return [u,v]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.healthy = True
        self.movmentType = 'random'
        if np.random.rand() < 0.05:
            self.movmentType = 'vField'


    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def infect(self):
        self.healthy = False

    def calculateDistance(self, other):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def move(self):
        if self.movmentType == 'random':
            self.x += np.random.uniform(-0.1, 0.1) * 0.3
            self.y += np.random.uniform(-0.1, 0.1) * 0.3
        elif self.movmentType == 'vField':
            evaluatedFeild = vField(self.x, self.y)
            self.x += evaluatedFeild[0] * 0.01
            self.y += evaluatedFeild[1] * 0.01


#generate 10 points and add them to the population


# Generate 10 random points
population = [Point(np.random.uniform(-1, 1), np.random.uniform(-1, 1)) for _ in range(500)]

#infect 1 random point
population[0].infect()

fig, ax = plt.subplots()

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

def update(frame):

    for P in population:
        P.move()

    for i in population:
        if not i.healthy:
            for k in population:
                if i==k:
                    continue
                else:
                    if i.calculateDistance(k) < 0.1:
                        if np.random.rand() < 0.3:
                            k.infect()

    col = []
    for P in population:
        if P.healthy:
            col.append('green')
        else:
            col.append('red')

    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    scat = ax.scatter([P.x for P in population], [P.y for P in population], s=10, alpha=0.5,
                      c=['green' if P.healthy else 'red' for P in population])
    print(frame)

    return scat,

ani = FuncAnimation(fig, update, frames=200, interval=100, blit=True)

plt.show()

ani.save('animations/animation.mp4', writer='ffmpeg')

