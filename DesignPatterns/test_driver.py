import inspect
import test

class Test2(object):
    pass
class Test3(object):
    pass

def test_fun():
    print("test fun called")


class TestDriver(object):
    @test.on("sabya")
    def visit(self, node):
        print("Visit1 called")

    #print("Locals after 1st call", inspect.currentframe().f_locals)
    @test.when(Test2)
    def visit(self, node):
        print("visit2 called")

    #print("Locals after 2nd call", inspect.currentframe().f_locals)

    @test.when(Test3)
    def visit(self, node):
        print("visit3 called")

    #print("Locals after 3rd call", inspect.currentframe().f_locals)

#my_test = TestDriver()
#my_test.visit(Test2())
#my_test.visit(Test3())




