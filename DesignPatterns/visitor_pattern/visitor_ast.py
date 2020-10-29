from visitor_pattern import visit as v
import sys
import inspect

class BaseNode:
  def accept(self, visitor):
    print("BAse node visitor called", inspect.currentframe().f_locals)
    visitor.visit(self)


class Literal(BaseNode):
  def __init__(self, val):
    self.value = val


class VariableNode(BaseNode):
  def __init__(self, name):
    self.name = name


class AssignmentExpression(BaseNode):
  def __init__(self, left, right):
    self.children = [left, right]


class AbstractSyntaxTreeVisitor(object):
  @v.on('node')
  def visit(self, node):
    """
    This is the generic method that initializes the
    dynamic dispatcher.
    """
    print("node visit called")

  @v.when(BaseNode)
  def visit(self, node):
    """
    Will run for nodes that do specifically match the
    provided type.
    """
    print("Unrecognized node:", node)

  @v.when(AssignmentExpression)
  def visit(self, node):
    """ Matches nodes of type AssignmentExpression. """
    print("Assignment expression visit called")
    node.children[0].accept(self)
    sys.stdout.write('=')
    node.children[1].accept(self)


  @v.when(VariableNode)
  def visit(self, node):
    """ Matches nodes that contain variables. """
    print("Visit Variable node")
    sys.stdout.write(str(node.name))

  @v.when(Literal)
  def visit(self, node):
    print("Visit literal node")
    sys.stdout.write(str(node.value))


