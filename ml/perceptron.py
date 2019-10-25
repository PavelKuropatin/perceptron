import numpy as _


class Perceptron:

    def __init__(self, a: _.ndarray, lambdas: _.ndarray):
        self.__a: _.ndarray = a
        self.__lambdas: _.ndarray = lambdas
        self.__sums: _.ndarray = None
        self.__y: _.ndarray = None

    def __process_image(self, x: _.ndarray):
        x = _.concatenate(x)

        self.__y = _.array([
            1 if sum(a_i * x) else 0
            for a_i in self.__a
        ])

        self.__sums = self.__y @ self.__lambdas.transpose()

        return self.__sums.argmax()

    def learning(self, x: _.ndarray, proper_class: int):
        out_class = self.__process_image(x)
        print(out_class)
        if out_class != proper_class:
            print(self.__sums)
            print(self.__lambdas)
            for i in range(len(self.__lambdas[proper_class])):
                self.__lambdas[proper_class][i] += 1 if self.__y[i] else -1
            print(self.__lambdas)

    def recognizing(self, x: _.ndarray):
        return self.__process_image(x)
