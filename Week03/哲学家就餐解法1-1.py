import threading


class DiningPhilosophers:
    def __init__(self):
        self.cv = threading.Condition()
        # self.thread_list = [None for i in ragne(5)]
        self.d = {}
        for i in range(5):
            self.d[i] = False

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self, philosopher: int, *actions) -> None:
        """
        Solution 2, using threading condition
        """
        neighbors = [philosopher - 1, philosopher + 1]
        if neighbors[0] < 0: neighbors[0] = 4
        if neighbors[1] > 4: neighbors[1] = 0

        with self.cv:
            self.cv.wait_for(lambda: not self.d[neighbors[0]] and not self.d[neighbors[1]])
            self.d[philosopher] = True

            [*map(lambda func: func(), actions)]

        self.d[philosopher] = False

