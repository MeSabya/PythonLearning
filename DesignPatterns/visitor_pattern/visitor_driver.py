from visitor_pattern import visitor_ast as ast

v = ast.VariableNode('x')
l = ast.Literal(5)
n = ast.AssignmentExpression(v, l)
visitor = ast.AbstractSyntaxTreeVisitor()
visitor.visit(n)
print ('')