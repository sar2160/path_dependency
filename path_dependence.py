
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn

class Urn:
        def __init__(self,m,b):
            self.contents = []
            self.add_n_balls(m,b)

        def add_n_balls(self,m=0,b=0):
            self.contents.extend(['m' for i in range(m)])
            self.contents.extend(['b' for i in range(b)])

        def get_p(self,kind='m'):
            count_m = float(self.contents.count('m'))
            count_b = float(self.contents.count('b'))
            p = count_m / (count_m + count_b)
            if kind is 'b':
                return 1-p
            else:
                return p

        def choose_random(self):
            return random.choice(self.contents)

        def run_process(self, process_type):
            ''' runs a process type e.g, polya on itself'''
            return process_type()

        def polya(self):
            choose = self.choose_random()
            self.contents.extend([choose for i in range(2)])

        def balancing(self):
                choose = self.choose_random()
                opposite = [s for s in self.contents if s not in choose][0]
                self.contents.extend(opposite)



def create_process(urn ,process_type, periods=100,filename='process_animation.gif',just_outputs=False,chart_title='Process Animation',):
    p_time = []

    x_axis = range(periods)

    for n in x_axis:
        urn.run_process(process_type)
        p_time.append(urn.get_p())

    if just_outputs:
        return p_time

    y = p_time

    fig, ax = plt.subplots()
    line, = ax.plot(x_axis, y, color='#800000')

    def update(num, x_axis, y, line):
        line.set_data(x_axis[:num], y[:num])
        line.axes.axis([0, periods, 0, 1])
        return line,

    plt.title(chart_title)
    plt.xlabel('Periods (t)')
    plt.ylabel("Pct Maroon Balls")
    ani = animation.FuncAnimation(fig, update, len(x_axis), fargs=[x_axis, y, line],
                              interval=35, blit=False)
    ani.save(filename)
    plt.show()


def main():
    my_urn = Urn(1,1)
    create_process(my_urn,process_type=my_urn.polya,periods=250,chart_title='Polya Process',filename='animations/polya.gif')
    create_process(my_urn,process_type=my_urn.balancing,periods=250,chart_title='Balancing Process',filename='animations/balancing.gif')

    biased_urn = Urn(1,2)

    create_process(biased_urn,process_type=biased_urn.polya,periods=250,chart_title='Biased Polya Process',filename='animations/biased_polya.gif')



if __name__ == "__main__":
    main()
