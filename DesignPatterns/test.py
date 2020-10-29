import inspect

def on(param_name):
    def f(fn):
        print("On F is called")
        dispatcher = Dispatcher(param_name, fn)
        return dispatcher
    return f

def when(param_type):
  def f(fn):
      last_frame = inspect.currentframe().f_back
      print("When: Locals last frame", last_frame.f_locals)
      dispatcher = last_frame.f_locals[fn.__name__]
      print("dispatcher is", dispatcher)

      if not isinstance(dispatcher, Dispatcher):
          dispatcher = dispatcher.dispatcher
      dispatcher.add_target_fn(param_type, fn)
      def ff(*args, **kwargs):
          print("when FF is called")
          return dispatcher(*args)
      ff.dispatcher = dispatcher
      return ff

  return f

class Dispatcher(object):
    def __init__(self, param_name, fn):
        print("Dispatcher is init called full argspec", self.__argspec(fn))
        self.param_index = self.__argspec(fn).args.index(param_name)
        print("Paramter index", self.param_index)
        self.param_name = param_name
        self.targets = {}

    def __call__(self, *args, **kwargs):
        print("Dispatcher object called", args)
        typ = args[self.param_index].__class__
        print("type is ", typ)

        fn = self.targets.get(typ)
        if fn is not None:
            return fn(*args, **kwargs)

    def add_target_fn(self, params, fn):
        self.targets[params] = fn

    @staticmethod
    def __argspec(fn):
        # Support for Python 3 type hints requires inspect.getfullargspec
        if hasattr(inspect, 'getfullargspec'):
            return inspect.getfullargspec(fn)
        else:
            return inspect.getargspec(fn)
