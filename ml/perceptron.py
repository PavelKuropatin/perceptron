import numpy as _


class Perceptron:

    def __init__(self, a: _.ndarray, lambdas: _.ndarray):
        self.__a: _.ndarray = a
        self.__lambdas: _.ndarray = lambdas
        self.__sums: _.ndarray = _.array([0] * len(lambdas[0]))
        self.__y: _.ndarray = _.array([0] * len(a))

    @property
    def a(self):
        return self.__a

    @property
    def out_data(self):
        return [self.y.tolist()] + self.lambdas.transpose().tolist()

    @property
    def y(self):
        return self.__y

    @property
    def lambdas(self):
        return self.__lambdas

    @property
    def sums(self):
        return self.__sums

    def __process_image(self, x: _.ndarray):
        x = _.concatenate(x)

        self.__y = _.array([
            1 if sum(a_i * x) else 0
            for a_i in self.__a
        ])

        self.__sums = self.__y @ self.__lambdas

        return self.__sums.argmax()

    def learning(self, x: _.ndarray, proper_class: int):
        out_class = self.__process_image(x)

        if out_class != proper_class:
            self.__lambdas = self.__lambdas.transpose()
            for i in range(len(self.__lambdas[proper_class])):
                self.__lambdas[proper_class][i] += 1 if self.__y[i] else -1
            self.__lambdas = self.__lambdas.transpose()

    def recognizing(self, x: _.ndarray):
        return self.__process_image(x)
