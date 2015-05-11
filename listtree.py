__author__ = 'yahor_hamaliy'


class ListTree:
    def __str__(self):
        self.__visited = {}

        return 'Instance of {0}{1}'.format(
            self.__class__.__name__,
            self.__listclass(self.__class__, 4))


    def __listclass(self, aClass, indent):
        dots = ' ' * indent

        # if aClass in self.__visited:
        # return '\n{0}<Class {1}:, address {2}: (see above)>'.format(dots,
        #                                                                   aClass.__name__, id(aClass))
        # else:
        # self.__visited[aClass] = True
        genabove = (self.__listclass(c, indent + 4) for c in aClass.__bases__)
        return '\n{0}Class {1}{2}'.format(
            dots,
            aClass.__name__,
            ''.join(genabove)
        )


class Super:
    def __init__(self):
        self.data1 = 'spam'


    def ham(self):
        pass


class Sub(Super, ListTree):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42


    def spam(self):
        pass


if __name__ == '__main__':
    X = Sub()
    print(X)