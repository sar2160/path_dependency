
import random


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



my_urn = Urn(1,1)

p_time = []
for n in range(100):
    my_urn.run_process(my_urn.balancing)
    p_time.append(my_urn.get_p())

print p_time
