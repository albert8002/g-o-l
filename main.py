import itertools
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation
import os

class Generate:

    def canvas(self:int)-> np.ndarray[int]:
        return np.zeros((self, self))

    def neighbours_sum(self:list[int], args: np.ndarray[int]) -> int:
        x: set[int] = set(range(self[0]-1, self[0]+2))
        y: set[int] = set(range(self[1]-1, self[1]+2))
        comb: list[tuple] = itertools.product(x,y)
        n_val: list[int] = \
        [
            args[loc[0], loc[1]]
            for loc in comb
            if 0 <= loc[0] < args.shape[0]
            and 0 <= loc[1] < args.shape[1]
            and not loc == (tuple(self))
        ]
        return np.sum(n_val)


    def next_gen(self: np.ndarray[int]) -> np.ndarray[int]:
        for index, cell in np.ndenumerate(self):
            neighbours: int = Generate.neighbours_sum(index, self)
            self[index[0], index[1]] = np.abs(np.sign(self[index[0], index[1]]))
            if cell == 0 and neighbours == 3:
                self[index[0], index[1]] = 1
            elif cell == 1 and neighbours < 2:
                self[index[0], index[1]] = 0
            elif cell == 1 and neighbours > 3:
                self[index[0], index[1]] = 0
        return self

    def position(self:np.ndarray[int]) -> np.ndarray[int]:
        canv = self
        canv[4, 4] = 1
        canv[4, 5] = 1
        canv[4, 6] = 1
        canv[5, 3] = 1
        canv[5, 7] = 1
        canv[6, 4] = 1
        canv[6, 5] = 1
        canv[6, 6] = 1
        return canv

canv = Generate.position(Generate.canvas(25))
frames = 1000

class Animate:

    def plot(self: np.ndarray[int]) -> None:
        #print(self)
        plt.clf()
        plt.figure(0)
        sns.heatmap(self, vmin=0, vmax=1, cmap='rocket')
        plt.title('g.o.l simulation')

    def run(self: int):
        global canv
        global frames
        print(f'{self}/{frames}')
        canv = Generate.next_gen(canv)
        Animate.plot(canv)
    def exec(self:str, args:int, interval:int=100):
        plt.close(0)
        ani = FuncAnimation(plt.figure(0), Animate.run, frames=args, interval=interval)
        ani.save(self)
        print(f'saved to {os.path.join(os.getcwd(),self)}')




if __name__ == '__main__':
    Animate.exec('anim.mp4', frames)
