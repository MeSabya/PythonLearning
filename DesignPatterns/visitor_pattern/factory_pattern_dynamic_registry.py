from abc import ABC, abstractmethod
import logging
import shlex
import subprocess

logger = logging.getLogger(__name__)

class ExecutorFactory:
    registry = {}

    @classmethod
    def create_executor(cls, name, **kwargs):
        if name not in cls.registry:
            logger.warning("Class not present in registry", name)
            return
        exec_class = cls.registry[name]
        executor = exec_class(**kwargs)
        return executor

    @classmethod
    def register(cls, name):
        print("Registering the class ", name)
        def inner_wrapper(cls_name):
            if cls_name in cls.registry:
                print("Class already present in the registry", cls_name)
            cls.registry[name] = cls_name
            return cls_name

        return inner_wrapper

class ExecutorBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def run(self, command):
        pass

@ExecutorFactory.register('local')
class LocalExecutor(ExecutorBase):
    def run(self, command):
        print("LocalExecutor running ....")
        ''' Here we will learn how to execute shell command in python '''
        #args = shlex.split(command)
        #stdout, stderr = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        #out = stdout.decode('utf-8')
        #err = stderr.decode('utf-8')
        #return out, err

@ExecutorFactory.register('aws_remote')
class RemoteExecutor(ExecutorBase):
    def run(self, command):
        print("AWS remote connection executed")

if __name__ == '__main__':
    print("main method")
    # Creates a local executor
    local = ExecutorFactory.create_executor('local')
    local.run("sabya")

    remote = ExecutorFactory.create_executor('aws_remote')
    remote.run('sabya remote')
