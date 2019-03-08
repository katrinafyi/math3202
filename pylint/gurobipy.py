from typing import Any
from io import TextIOBase as _TextIOBase

class LinExpr(object):
    def __repr__(self):
        """
Return repr(self).
        """
        ...
    def __lt__(self, value):
        """
Return self<value.
        """
        ...
    def __le__(self, value):
        """
Return self<=value.
        """
        ...
    def __eq__(self, value):
        """
Return self==value.
        """
        ...
    def __ne__(self, value):
        """
Return self!=value.
        """
        ...
    def __gt__(self, value):
        """
Return self>value.
        """
        ...
    def __ge__(self, value):
        """
Return self>=value.
        """
        ...
    def __init__(self, *args, **kwargs):
        """
Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
    def __add__(self, value):
        """
Return self+value.
        """
        ...
    def __radd__(self, value):
        """
Return value+self.
        """
        ...
    def __sub__(self, value):
        """
Return self-value.
        """
        ...
    def __rsub__(self, value):
        """
Return value-self.
        """
        ...
    def __mul__(self, value):
        """
Return self*value.
        """
        ...
    def __rmul__(self, value):
        """
Return value*self.
        """
        ...
    def __neg__(self):
        """
-self
        """
        ...
    def __iadd__(self, value):
        """
Return self+=value.
        """
        ...
    def __isub__(self, value):
        """
Return self-=value.
        """
        ...
    def __imul__(self, value):
        """
Return self*=value.
        """
        ...
    def __truediv__(self, value):
        """
Return self/value.
        """
        ...
    def __rtruediv__(self, value):
        """
Return value/self.
        """
        ...
    def __new__(*args, **kwargs):
        """
Create and return a new object.  See help(type) for accurate signature.
        """
        ...
    def _flatten(self, *args, **kwargs) -> Any:
        ...
    def _normalize(self, *args, **kwargs) -> Any:
        ...
    def add(self, expr, mult=1.0):
        """
ROUTINE:
  add(expr, mult=1.0)

PURPOSE:
  Add a linear multiple of one expression into another.

ARGUMENTS:
  expr (LinExpr): The expression to add
  mult (float):   The linear multiplier

EXAMPLE:
  expr1.add(expr2, 2.0)
        """
        ...
    def addConstant(self, constant):
        """
ROUTINE:
  addConstant(constant)

PURPOSE:
  Add a constant into a linear expression.

ARGUMENTS:
  constant (float): The value to add

EXAMPLE:
  expr.addConstant(3.5)
        """
        ...
    def addTerms(self, coeffs, vars):
        """
ROUTINE:
  addTerms(coeffs, vars)

PURPOSE:
  Add a list of terms into a linear expression.

ARGUMENTS:
  coeffs (list of float): The coefficients for the new terms
  vars (list of Var):     The variables for the new terms

EXAMPLE:
  expr.addTerms(1.0, x)
  expr.addTerms([1.0, 2.0], [x, y])
        """
        ...
    def _mul(self, *args, **kwargs) -> Any:
        ...
    def size(self):
        """
ROUTINE:
  size()

PURPOSE:
  Return the number of terms in a linear expression.

ARGUMENTS:
  None.

RETURN VALUE:
  Number of terms in expression.

EXAMPLE:
  print expr.size()
        """
        ...
    def getConstant(self):
        """
ROUTINE:
  getConstant()

PURPOSE:
  Return the constant terms from a linear expression.

ARGUMENTS:
  None.

RETURN VALUE:
  Constant for expression.

EXAMPLE:
  print expr.getConstant()
        """
        ...
    def getCoeff(self, i):
        """
ROUTINE:
  getCoeff(i)

PURPOSE:
  Return the coefficient for the term at index 'i'.

ARGUMENTS:
  i (Int): Index of term whose coefficient is requested

RETURN VALUE:
  The requested coefficient.

EXAMPLE:
  print expr.getCoeff(i)
        """
        ...
    def getVar(self, i):
        """
ROUTINE:
  getVar(i)

PURPOSE:
  Return the variable for the term at index 'i'.

ARGUMENTS:
  i (Int): Index of term whose variable is requested

RETURN VALUE:
  The requested variable (a Var object).

EXAMPLE:
  print expr.getVar(i)
        """
        ...
    def getValue(self):
        """
ROUTINE:
  getValue()

PURPOSE:
  Compute the value of the expression, using the current solution.

ARGUMENTS:
  None.

RETURN VALUE:
  The computed expression value.

EXAMPLE:
  print model.getObjective().getValue()
        """
        ...
    def remove(self, which):
        """
ROUTINE:
  remove(which)

PURPOSE:
  Remove a term from the expression.

ARGUMENTS:
  which: Term to remove.  Can be an Int, in which case the term at
         index 'which' is removed, or a Var, in which case all terms that
         involve the Var 'which' are removed.

EXAMPLE:
  print expr.remove(i)
        """
        ...
    def clear(self):
        """
ROUTINE:
  clear()

PURPOSE:
  Set a linear expression to zero.

EXAMPLE:
  print expr.clear()
        """
        ...
    def copy(self):
        """
ROUTINE:
  copy()

PURPOSE:
  Copy a linear expression.

EXAMPLE:
  expr2 = expr1.copy()
        """
        ...
    def __reduce__(self, *args, **kwargs) -> Any:
        ...
    def __setstate__(self, *args, **kwargs) -> Any:
        ...
class QuadExpr(object):
    def __repr__(self):
        """
Return repr(self).
        """
        ...
    def __lt__(self, value):
        """
Return self<value.
        """
        ...
    def __le__(self, value):
        """
Return self<=value.
        """
        ...
    def __eq__(self, value):
        """
Return self==value.
        """
        ...
    def __ne__(self, value):
        """
Return self!=value.
        """
        ...
    def __gt__(self, value):
        """
Return self>value.
        """
        ...
    def __ge__(self, value):
        """
Return self>=value.
        """
        ...
    def __init__(self, *args, **kwargs):
        """
Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
    def __add__(self, value):
        """
Return self+value.
        """
        ...
    def __radd__(self, value):
        """
Return value+self.
        """
        ...
    def __sub__(self, value):
        """
Return self-value.
        """
        ...
    def __rsub__(self, value):
        """
Return value-self.
        """
        ...
    def __mul__(self, value):
        """
Return self*value.
        """
        ...
    def __rmul__(self, value):
        """
Return value*self.
        """
        ...
    def __neg__(self):
        """
-self
        """
        ...
    def __iadd__(self, value):
        """
Return self+=value.
        """
        ...
    def __isub__(self, value):
        """
Return self-=value.
        """
        ...
    def __imul__(self, value):
        """
Return self*=value.
        """
        ...
    def __truediv__(self, value):
        """
Return self/value.
        """
        ...
    def __rtruediv__(self, value):
        """
Return value/self.
        """
        ...
    def __new__(*args, **kwargs):
        """
Create and return a new object.  See help(type) for accurate signature.
        """
        ...
    def _flatten(self, *args, **kwargs) -> Any:
        ...
    def _normalize(self, *args, **kwargs) -> Any:
        ...
    def add(self, expr, mult=1.0):
        """
ROUTINE:
  add(expr, mult=1.0)

PURPOSE:
  Add a linear multiple of one expression into another.

ARGUMENTS:
  expr (LinExpr or QuadExpr): The expression to add
  mult (float):               The linear multiplier

EXAMPLE:
  expr1.add(expr2, 2.0)
        """
        ...
    def addConstant(self, constant):
        """
ROUTINE:
  addConstant(constant)

PURPOSE:
  Add a constant into a quadratic expression.

ARGUMENTS:
  constant (float): The value to add

EXAMPLE:
  expr.addConstant(3.5)
        """
        ...
    def addTerms(self, coeffs, vars):
        """
ROUTINE:
  addTerms(coeffs, vars)
  addTerms(coeffs, vars, vars2)

PURPOSE:
  Add a list of terms, either linear or quadratic, into a quadratic
  expression.

ARGUMENTS:
  coeffs (list of float): The coefficients for the new terms
  vars (list of Var):     The variables for the new terms
  vars2 (list of Var):    The variables for the new terms

EXAMPLE:
  expr.addTerms(1.0, x)
  expr.addTerms(1.0, x, x)
  expr.addTerms([1.0, 2.0], [x, y])
  expr.addTerms([1.0, 2.0], [x, y], [x, y])
        """
        ...
    def _mul(self, *args, **kwargs) -> Any:
        ...
    def size(self):
        """
ROUTINE:
  size()

PURPOSE:
  Return the number of quadratic terms in a quadratic expression.

ARGUMENTS:
  None.

RETURN VALUE:
  Number of terms in expression.

EXAMPLE:
  print expr.size()
        """
        ...
    def getLinExpr(self):
        """
ROUTINE:
  getLinExpr()

PURPOSE:
  Return the linear portion of a quadration expression (as a LinExpr
  object).

ARGUMENTS:
  None.

RETURN VALUE:
  Linear expression.

EXAMPLE:
  print expr.getLinExpr()
        """
        ...
    def getCoeff(self, i):
        """
ROUTINE:
  getCoeff(i)

PURPOSE:
  Return the coefficient for the term at index 'i'.

ARGUMENTS:
  i (Int): Index of term whose coefficient is requested

RETURN VALUE:
  The requested coefficient.

EXAMPLE:
  print expr.getCoeff(i)
        """
        ...
    def getVar1(self, i):
        """
ROUTINE:
  getVar1(i)

PURPOSE:
  Return the first variable for the quadratic term at index 'i'.

ARGUMENTS:
  i (Int): Index of quadratic term whose variable is requested

RETURN VALUE:
  The requested variable.

EXAMPLE:
  print expr.getVar1(i)
        """
        ...
    def getVar2(self, i):
        """
ROUTINE:
  getVar2(i)

PURPOSE:
  Return the second variable for the quadratic term at index 'i'.

ARGUMENTS:
  i (Int): Index of quadratic term whose variable is requested

RETURN VALUE:
  The requested variable.

EXAMPLE:
  print expr.getVar2(i)
        """
        ...
    def getValue(self):
        """
ROUTINE:
  getValue()

PURPOSE:
  Compute the value of the expression, using the current solution.

ARGUMENTS:
  None.

RETURN VALUE:
  The computed expression value.

EXAMPLE:
  print model.getObjective().getValue()
        """
        ...
    def remove(self, which):
        """
ROUTINE:
  remove(which)

PURPOSE:
  Remove a quadratic term from the expression.

ARGUMENTS:
  which: Term to remove.  Can be an Int, in which case the quadratic term
         at index 'which' is removed, or a Var, in which case all quadratic
         terms that involve the Var 'which' are removed.

EXAMPLE:
  print expr.remove(i)
        """
        ...
    def clear(self):
        """
ROUTINE:
  clear()

PURPOSE:
  Set a linear expression to zero.

EXAMPLE:
  print expr.clear()
        """
        ...
    def copy(self):
        """
ROUTINE:
  copy()

PURPOSE:
  Copy a quadratic expression.

EXAMPLE:
  expr2 = expr1.copy()
        """
        ...
    def __reduce__(self, *args, **kwargs) -> Any:
        ...
    def __setstate__(self, *args, **kwargs) -> Any:
        ...
class Env(object):
    """
Gurobi environment object.  Methods on this object are:
  readParams(paramname): Read a set of parameter settings from a file.
  resetParams(): Reset all parameters to their default values.
  setParam(paramname, newval): Set a parameter to a new value.
  writeParams(paramname): Write the current parameter settings to a file.

Additional help can be obtained on any of these methods (e.g.,
help(Env.setParam)).  A list of all available parameters can be
obtained by typing 'help(GRB.param)'.
    """
    _default: bool = ...
    _user: bool = ...
    _modcnt: int = ...
    def __init__(self, logfilename='', empty=False, cenv=None, isDefault=False):
        ...
    def __del__(self):
        ...
    def __repr__(self):
        ...
    def _paramlist(self, paramname):
        ...
    def _message(self, msg):
        ...
    def _getParamInfo(self, paramname):
        ...
    def _Env__setone(self, paraminfo, newval):
        ...
    def setParam(self, paramname, newval, verbose=True):
        """
ROUTINE:
  setParam(paramname, newvalue)

PURPOSE:
  Set a parameter to a new value.

ARGUMENTS:
  paramname (string): The name of the parameter.
  newvalue: The desired new value.  The type of the value should be
            compatible with the parameter type (e.g., an integer parameter
            will take an integer value).  One important exception: the
            string "default" will return the specified parameter to its
            default value.

RETURN VALUE:
  None.

EXAMPLE:
  env.setParam("NodeLimit", 100)
  env.setParam("TimeLimit", "default")

NOTES:
  Use this routine to change parameter values in the default environment.
  The default environment is used to initialize parameter values when a
  new model is created.  Once the model exists, changes to the default
  environment will no longer affect that model.  Use Model.setParam()
  to change parameter settings for an existing model.

  Routine paramHelp() provides additional information on the available
  parameters.
        """
        ...
    def resetParams(self):
        """
ROUTINE:
  resetParams()

PURPOSE:
  Reset all parameters to their default values.

ARGUMENTS:
  None.

RETURN VALUE:
  None.

EXAMPLE:
  env.resetParams()

NOTES:
  This routine should normally be called on the default environment or on
  a model object.
        """
        ...
    def readParams(self, filename):
        """
ROUTINE:
  readParams(filename)

PURPOSE:
  Read a set of parameter settings from a file.

ARGUMENTS:
  filename (string): A path to a file containing a list of parameter
                     settings.

RETURN VALUE:
  None.

EXAMPLE:
  env.readParams('gurobi.prm')

NOTES:
  This routine should normally be called on the default environment or on
  a model object.

  The parameter file should contain "name value" pairs, each on its own
  line.  A hash symbol at the beginning of a line indicates that the line
  should be ignored.  Here is an example of a valid parameter file:

    # List of changed parameters
    TimeLimit      100
    IterationLimit 1000
        """
        ...
    def writeParams(self, filename):
        """
ROUTINE:
  writeParams(filename)

PURPOSE:
  Write non-default parameter settings to a file.

ARGUMENTS:
  filename (string): The name of the file to which non-default parameter
                     settings should be written.

RETURN VALUE:
  None.

EXAMPLE:
  env.writeParams('changed.prm')

NOTES:
  This routine should normally be called on the default environment or on
  a model object.

  Upon completion, the specified file will contain a set of "name value"
  pairs, one per line, that indicates the set of parameters that current
  have non-default values in the specified model.
        """
        ...
    def start(self):
        ...
    def dispose(self):
        ...
    @classmethod
    def ClientEnv(cls, *args, **kwargs) -> Any:
        ...
    @classmethod
    def CloudEnv(cls, *args, **kwargs) -> Any:
        ...
    @classmethod
    def OtherEnv(cls, *args, **kwargs) -> Any:
        ...
class Var(object):
    """
Gurobi variable object.  Variables have a number of attributes.
Some can be set (e.g., v.ub = 0.0), while others can only be queried
(e.g., print v.x). The most commonly used variable attributes are:
  obj: Linear objective coefficient.
  lb: Lower bound.
  ub: Upper bound.
  varName: Variable name.
  vType: Variable type ('C', 'B', 'I', 'S', or 'N').
  x: Solution value.
  rc: Solution reduced cost.
  xn: Solution value in an alternate MIP solution.

Type "help(GRB.attr)" for a list of all available attributes.

Note that attribute modifications are handled in a lazy fashion.  You
won't see the effect of a change until after the next call to Model.update()
or Model.optimize().
    """
    def __init__(self, cmodel, colno):
        ...
    def __dir__(self):
        ...
    def __colno__(self):
        ...
    def __repr__(self):
        ...
    def __numcols__(self):
        ...
    def __getattr__(self, name):
        ...
    def __setattr__(self, name, value):
        ...
    def getAttr(self, attrname):
        """
ROUTINE:
  getAttr(attrname)

PURPOSE:
  Request the value of a variable attribute.

ARGUMENTS:
  attrname (string): The name of the requested attribute.

RETURN VALUE:
  The attribute value.

EXAMPLE:
  print var.getAttr("varName")

NOTES:
  Type "help(GRB.attr)" for a list of all available attributes.
        """
        ...
    def setAttr(self, attrname, newval):
        """
ROUTINE:
  setAttr(attrname, newvalue)

PURPOSE:
  Change the value of a variable attribute.

ARGUMENTS:
  attrname (string): The name of the attribute.
  newvalue: The desired new value.  The type of the value should be
            compatible with the attribute type (e.g., an integer parameter
            will take an integer value).

RETURN VALUE:
  The attribute value.

EXAMPLE:
  var.setAttr("varName", "New name")

NOTES:
  Constraint attributes that can be set are:
    VarName:  Name of the variable.
    lb:       Lower bound.
    ub:       Upper bound.
    obj:      Objective coefficient.
    vType:    Variable type ('C', 'B', 'I', 'S', or 'N').

  Attributes changes are handled in a lazy fashion.  The effect of a
  change isn't visible until after the next call to Model.update() or
  Model.optimize().
        """
        ...
    def sameAs(self, other):
        """
ROUTINE:
  sameAs(othervar)

PURPOSE:
  Indicates whether two variable objects refer to the same Gurobi model
  variable.  You should use this instead of the '==' operator, since
  '==' is used to create linear constraints.

ARGUMENTS:
  othervar (Var): The variable to compare against.

RETURN VALUE:
  True if both Var objects refer to the same model variable.

EXAMPLE:
  var1.sameAs(var2)
        """
        ...
    def __le__(self, rhs):
        ...
    def __ge__(self, rhs):
        ...
    def __eq__(self, rhs):
        ...
    def __ne__(self, rhs):
        ...
    def __add__(self, expr):
        ...
    def __radd__(self, expr):
        ...
    def __iadd__(self, expr):
        ...
    def __sub__(self, expr):
        ...
    def __rsub__(self, expr):
        ...
    def __isub__(self, expr):
        ...
    def __mul__(self, expr):
        ...
    def __rmul__(self, expr):
        ...
    def __imul__(self, expr):
        ...
    def __div__(self, constant):
        ...
    def __truediv__(self, constant):
        ...
    def __neg__(self):
        ...
    lb = ...
    """Lower bound"""
    ub = ...
    """Upper bound"""
    obj = ...
    """Objective coefficient"""
    vType = ...
    """Variable type (GRB.CONTINUOUS, GRB.BINARY, GRB.INTEGER, GRB.SEMICONT, or GRB.SEMIINT)"""
    varName = ...
    """Variable name"""
    x = ...
    """Solution value"""
    rc = ...
    """Reduced cost"""
    xn = ...
    """Solution value in alternate MIP solution"""
    start = ...
    """Start vector (use GRB.UNDEFINED to leave a value unspecified)"""
    vBasis = ...
    """Basis status"""
    varHintVal = ...
    """Variable hint value"""
    varHintPri = ...
    """Variable hint priority"""
    branchPriority = ...
    """Variable branch priority"""
    partition = ...
    """Variable partition"""
    IISLB = ...
    """Does LB participate in IIS? (for infeasible models)"""
    IISUB = ...
    """Does UB participate in IIS? (for infeasible models)"""
    SAObjLow = ...
    """Smallest objective coefficient for which basis remains optimal"""
    SAObjUp = ...
    """Largest objective coefficient for which basis remains optimal"""
    SALBLow = ...
    """Smallest lower bound for which basis remains optimal"""
    SALBUp = ...
    """Largest lower bound for which basis remains optimal"""
    SAUBLow = ...
    """Smallest upper bound for which basis remains optimal"""
    SAUBUp = ...
    """Largest upper bound for which basis remains optimal"""
    unbdRay = ...
    """Unbounded ray"""
    pStart = ...
    """Primal solution (for warm-starting simplex)"""
    preFixVal = ...
    """The value of the variable (for variables fixed by presolve)"""
    varPreStat = ...
    """Status of variable in presolved model"""
class Constr(object):
    """
Gurobi constraint object.  Constraints have a number of attributes.
Some can be set (e.g., c.rhs = 0.0), while others can only be queried
(e.g., print c.pi).  The most commonly used constraint attributes are:
  sense: Constraint sense ('<', '>', or '=').
  rhs: Right-hand side value.
  constrName: Constraint name.
  pi: Dual value in current solution
  slack: Slack in current solution.

Type "help(GRB.attr)" for a list of all available attributes.

Note that attribute modifications are handled in a lazy fashion.  You
won't see the effect of a change until after the next call to Model.update()
or Model.optimize().
    """
    def __init__(self, cmodel, rowno):
        ...
    def __dir__(self):
        ...
    def __rowno__(self):
        ...
    def __repr__(self):
        ...
    def __numrows__(self):
        ...
    def __getattr__(self, name):
        ...
    def __setattr__(self, name, value):
        ...
    def getAttr(self, attrname):
        """
ROUTINE:
  getAttr(attrname)

PURPOSE:
  Request the value of a constraint attribute.

ARGUMENTS:
  attrname (string): The name of the requested attribute.

RETURN VALUE:
  None.

EXAMPLE:
  print constr.getAttr("constrName")

NOTES:
  Type "help(GRB.attr)" for a list of all available attributes.
        """
        ...
    def setAttr(self, attrname, newval):
        """
ROUTINE:
  setAttr(attrname, newvalue)

PURPOSE:
  Change the value of a constraint attribute.

ARGUMENTS:
  attrname (string): The name of the attribute.
  newvalue: The desired new value.  The type of the value should be
            compatible with the attribute type (e.g., an integer parameter
            will take an integer value).

RETURN VALUE:
  The attribute value.

EXAMPLE:
  constr.setAttr("constrName", "New name")

NOTES:
  Constraint attributes that can be set are:
    constrName: Constraint name.
    sense:      Constraint sense.
    rhs:        Right-hand side value.

  Attributes changes are handled in a lazy fashion.  The effect of a
  change isn't visible until after the next call to Model.update() or
  Model.optimize().
        """
        ...
    def sameAs(self, other):
        """
ROUTINE:
  sameAs(otherconstr)

PURPOSE:
  Indicates whether two constraint objects refer to the same Gurobi model
  constraints.

ARGUMENTS:
  otherconstr (Constr): The constraint to compare against.

RETURN VALUE:
  True if both Constr objects refer to the same model constraint.

EXAMPLE:
  constr1.sameAs(constr2)
        """
        ...
    sense = ...
    """Constraint sense"""
    rhs = ...
    """Constraint right-hand side value"""
    constrName = ...
    """Constraint name"""
    pi = ...
    """Dual value"""
    slack = ...
    """Constraint slack"""
    cBasis = ...
    """Basis status"""
    lazy = ...
    """Lazy constraint flag"""
    IISConstr = ...
    """Does constraint participate in IIS? (for infeasible models)"""
    SARHSLow = ...
    """Smallest RHS value for which basis remains optimal"""
    SARHSUp = ...
    """Largest RHS value for which basis remains optimal"""
    farkasDual = ...
    """Farkas dual for infeasible models"""
    dStart = ...
    """Dual solution (for warm-starting simplex)"""
class SOS(object):
    """
Gurobi SOS object.  SOS objects have a single attribute: IISSOS.
When an IIS is available, this attribute indicates whether the
SOS object participates in the IIS.
    """
    def __init__(self, cmodel, sosno):
        ...
    def __dir__(self):
        ...
    def __sosno__(self):
        ...
    def __repr__(self):
        ...
    def __getattr__(self, name):
        ...
    def getAttr(self, attrname):
        """
ROUTINE:
  getAttr(attrname)

PURPOSE:
  Request the value of an SOS attribute.

ARGUMENTS:
  attrname (string): The name of the requested attribute.

RETURN VALUE:
  The attribute value.

EXAMPLE:
  print sos.getAttr("IISSOS")

NOTES:
  Type "help(GRB.attr)" for a list of all available attributes.
        """
        ...
    IISSOS = ...
    """Does SOS participate in IIS? (for infeasible models)"""
class QConstr(object):
    """
Gurobi quadratic constraint object.  Quadratic constraints have
several attribute...
    """
    def __init__(self, cmodel, qconstrno):
        ...
    def __dir__(self):
        ...
    def __qconstrno__(self):
        ...
    def __repr__(self):
        ...
    def __getattr__(self, name):
        ...
    def __setattr__(self, name, value):
        ...
    def getAttr(self, attrname):
        """
ROUTINE:
  getAttr(attrname)

PURPOSE:
  Request the value of a quadratic constraint attribute.

ARGUMENTS:
  attrname (string): The name of the requested attribute.

RETURN VALUE:
  The attribute value.

EXAMPLE:
  print qc.getAttr("QCname")

NOTES:
  Type "help(GRB.attr)" for a list of all available attributes.
        """
        ...
    def setAttr(self, attrname, newval):
        """
ROUTINE:
  setAttr(attrname, newvalue)

PURPOSE:
  Change the value of a quadratic constraint attribute.

ARGUMENTS:
  attrname (string): The name of the attribute.
  newvalue: The desired new value.  The type of the value should be
            compatible with the attribute type (e.g., an integer parameter
            will take an integer value).

RETURN VALUE:
  The attribute value.

EXAMPLE:
  qc.setAttr("QCname", "New name")

NOTES:
  Constraint attributes that can be set are:
    QCname:  Constraint name.
    QCsense: Constraint sense.
    QCrhs:   Right-hand side value.

  Attributes changes are handled in a lazy fashion.  The effect of a
  change isn't visible until after the next call to Model.update() or
  Model.optimize().
        """
        ...
    QCsense = ...
    """Quadratic constraint sense"""
    QCrhs = ...
    """Quadratic constraint right-hand side value"""
    QCname = ...
    """Quadratic constraint name"""
    IISQConstr = ...
    """Does QC participate in IIS? (for infeasible models)"""
    QCpi = ...
    """Dual value"""
    QCslack = ...
    """Quadratic constraint slack"""
class GenConstr(object):
    """
Gurobi GenConstr object.  GenConstr objects has two attributes:
GenConstrType and IISGenConstr.
The GenConstrType attribute indicates the type of the general constraint.
When an IIS is available, the IISGenConstr attribute indicates whether the
GenConstr object participates in the IIS.
    """
    def __init__(self, cmodel, genconstrno):
        ...
    def __dir__(self):
        ...
    def __genconstrno__(self):
        ...
    def __repr__(self):
        ...
    def __getattr__(self, name):
        ...
    def getAttr(self, attrname):
        """
ROUTINE:
  getAttr(attrname)

PURPOSE:
  Request the value of an GenConstr attribute.

ARGUMENTS:
  attrname (string): The name of the requested attribute.

RETURN VALUE:
  The attribute value.

EXAMPLE:
  print genconstr.getAttr("IISGenConstr")

NOTES:
  Type "help(GRB.attr)" for a list of all available attributes.
        """
        ...
    GenConstrType = ...
    """General constraint type (e.g., GRB.GENCONSTR_MAX)"""
    GenConstrName = ...
    """General constraint name"""
    IISGenConstr = ...
    """Does general constraint participate in IIS? (for infeasible models)"""
class TempConstr(object):
    """
Gurobi temporary constraint object.  Objects of this class are created
as intermediate results when building constraints using overloaded
operators.
    """
    def __init__(self, lhs, sense, rhs):
        ...
    def __repr__(self):
        ...
    def __rshift__(self, other):
        ...
    def __le__(self, rhs):
        ...
    def __ge__(self, rhs):
        ...
class Column(object):
    """
Column class.  Columns consist of a set of coefficient, constraint
pairs.  They capture the set of linear constraints in which a
variable participates.

The constructor for this class takes two arguments: Column(coeffs, constrs).
The constrs argument gives a Constr or list of Constr.  The coeffs
argument gives the corresponding coefficients
(e.g., "col = Column([1.0, 2.0], [c0, c1])").

Available methods on Column objects are:
  addTerms(coeffs, constrs): Add terms into a column.
  clear(): Set a column to zero.
  copy(): Copy a column.
  getCoeff(i): Return the coefficient for the term at index 'i'.
  getConstr(i): Return the constraint for the term at index 'i'.
  remove(i): Remove a term from the column.
  size(): Return the number of terms in the column.

You can say "help(Column.method)" to get help on any method
(e.g., help(Column.size)).
    """
    def __init__(self, coeffs=None, constrs=None):
        ...
    def __repr__(self):
        ...
    def _normalize(self):
        ...
    def addTerms(self, coeffs, constrs):
        """
ROUTINE:
  addTerms(coeffs, constrs)

PURPOSE:
  Add a list of terms into a column.

ARGUMENTS:
  coeffs (float or list of float): The coefficients for the new terms
  constrs (Constr or list of Constr): The constraints for the new terms

EXAMPLE:
  c0.addTerms(1.0, x)
  c0.addTerms([1.0, 2.0], [x, y])
        """
        ...
    def size(self):
        """
ROUTINE:
  size()

PURPOSE:
  Return the number of terms in a column.

ARGUMENTS:
  None.

RETURN VALUE:
  Number of terms in column.

EXAMPLE:
  print c0.size()
        """
        ...
    def getCoeff(self, i):
        """
ROUTINE:
  getCoeff(i)

PURPOSE:
  Return the coefficient for the term at index 'i'.

ARGUMENTS:
  i (Int): Index of term whose coefficient is requested

RETURN VALUE:
  The requested coefficient.

EXAMPLE:
  print c0.getCoeff(i)
        """
        ...
    def getConstr(self, i):
        """
ROUTINE:
  getConstr(i)

PURPOSE:
  Return the constraint for the term at index 'i'.

ARGUMENTS:
  i (Int): Index of term whose constraint is requested

RETURN VALUE:
  The requested constraint (a Constr object).

EXAMPLE:
  print c0.getConstr(i)
        """
        ...
    def remove(self, which):
        """
ROUTINE:
  remove(which)

PURPOSE:
  Remove a term from the column.

ARGUMENTS:
  which: Term to remove.  Can be an Int, in which case the term at
         index 'which' is removed, or a Constr, in which case all terms
         that involve the Constr 'which' are removed.

EXAMPLE:
  print c0.remove(i)
        """
        ...
    def clear(self):
        """
ROUTINE:
  clear()

PURPOSE:
  Clear a column.

EXAMPLE:
  print c0.clear()
        """
        ...
    def copy(self):
        """
ROUTINE:
  copy()

PURPOSE:
  Copy a column.

EXAMPLE:
  c1 = c0.copy()
        """
        ...
class GRBStringIO(_TextIOBase):
    """
Text I/O implementation using an in-memory buffer.

The initial_value argument sets the value of object.  The newline
argument is like the one of TextIOWrapper's constructor.
    """
    def __next__(self):
        """
Implement next(self).
        """
        ...
    def __init__(self, *args, **kwargs):
        """
Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
    def __new__(*args, **kwargs):
        """
Create and return a new object.  See help(type) for accurate signature.
        """
        ...
    def close(self):
        """
Close the IO object.

Attempting any further operation after the object is closed
will raise a ValueError.

This method has no effect if the file is already closed.
        """
        ...
    def getvalue(self):
        """
Retrieve the entire contents of the object.
        """
        ...
    def read(self, size=-1):
        """
Read at most size characters, returned as a string.

If the argument is negative or omitted, read until EOF
is reached. Return an empty string at EOF.
        """
        ...
    def readline(self, size=-1):
        """
Read until newline or EOF.

Returns an empty string if EOF is hit immediately.
        """
        ...
    def tell(self):
        """
Tell the current file position.
        """
        ...
    def truncate(self, pos=None):
        """
Truncate size to pos.

The pos argument defaults to the current file position, as
returned by tell().  The current file position is unchanged.
Returns the new absolute position.
        """
        ...
    def seek(self, pos, whence=0):
        """
Change stream position.

Seek to character offset pos relative to position indicated by whence:
    0  Start of stream (the default).  pos should be >= 0;
    1  Current position - pos must be 0;
    2  End of stream - pos must be 0.
Returns the new absolute position.
        """
        ...
    def write(self, s):
        """
Write string to file.

Returns the number of characters written, which is always equal to
the length of the string.
        """
        ...
    def seekable(self):
        """
Returns True if the IO object can be seeked.
        """
        ...
    def readable(self):
        """
Returns True if the IO object can be read.
        """
        ...
    def writable(self):
        """
Returns True if the IO object can be written.
        """
        ...
    def __getstate__(self, *args, **kwargs) -> Any:
        ...
    def __setstate__(self, *args, **kwargs) -> Any:
        ...
class Model(object):
    """
Gurobi model object.  Commonly used methods on this object are:
  getConstrs(): Get a list of constraints in the model
  getParamInfo(paramname): Get information on a model parameter.
  getVars(): Get a list of variables in the model
  optimize(): Optimize the model.
  printAttr(attrname, filter): Print attribute values.
  printQuality(): Print solution quality statistics.
  printStats(): Print model statistics.
  read(filename): Read model data (MIP start, basis, etc.) from a file
  reset(): Discard any resident solution information.
  resetParams(): Reset all parameters to their default values.
  setParam(paramname, newval): Set a model parameter to a new value.
  write(filename): Write model data to a file.

Models have a number of attributes that can be queried or modified.
For example, "print model.objval" prints the objective value of
the current solution.  Commonly used model attributes are:
  numConstrs: Number of constraints in model
  numVars: Number of variables in model
  status: Optimization status
  objVal: Objective of current solution
Type "help(GRB.attr)" for a complete list.

Additional methods on this object are:
  addConstr(), addGenConstrMax(), addGenConstrMin(), addGenConstrAbs(),
  addGenConstrAnd(), addGenConstrOr(), addGenConstrIndicator(),
  addRange(), addSOS(), addVar(), chgCoeff(), computeIIS(),
  copy(), fixed(), getCoeff(), getCol(), getRow(), message(), presolve(),
  relax(), terminate(), update()

Additional help can be obtained on any of these methods (e.g.,
help(Model.optimize)).
    """
    _Model__updatemode: int = ...
    _Model__newranges: int = ...
    def __init__(self, name='', env=None, cmodel=None):
        ...
    def __dir__(self):
        ...
    def __del__(self):
        ...
    def __repr__(self):
        ...
    @staticmethod
    def _Model__indexname(*args, **kwargs) -> Any:
        ...
    @staticmethod
    def _Model__genexpr_key(*args, **kwargs) -> Any:
        ...
    class _Model__listify(object):
        def __init__(self, *indexes, **kwargs):
            ...
        def flatten(self, x):
            ...
        def listify(self, arg, default):
            ...
    def display(self, obj=None):
        ...
    def __getattr__(self, name):
        ...
    def __setattr__(self, name, value):
        ...
    def _Model__setup(self):
        ...
    def _Model__getVar(self, j):
        ...
    def _Model__getConstr(self, i):
        ...
    def _Model__getSOS(self, s):
        ...
    def _Model__getQConstr(self, i):
        ...
    def _Model__getGenConstr(self, i):
        ...
    def _Model__owns(self, object):
        ...
    def _Model__isAttrAvailable(self, attrname):
        ...
    def getVars(self):
        """
ROUTINE:
  getVars()

PURPOSE:
  Obtain a list of variables in the model.

ARGUMENTS:
  None.

RETURN VALUE:
  A list of Var objects.

EXAMPLE:
  vars = model.getVars()
  for v in vars:
    print v.VarName, v.X
        """
        ...
    def getConstrs(self):
        """
ROUTINE:
  getConstrs()

PURPOSE:
  Obtain a list of linear constraints in the model.

ARGUMENTS:
  None.

RETURN VALUE:
  A list of Constr objects.

EXAMPLE:
  constrs = model.getConstrs()
  for c in constrs:
    print c.ConstrName, c.Slack
        """
        ...
    def getSOSs(self):
        """
ROUTINE:
  getSOSs()

PURPOSE:
  Obtain a list of SOS constraints in the model.

ARGUMENTS:
  None.

RETURN VALUE:
  A list of SOS objects.

EXAMPLE:
  sos = model.getSOSs()
  for s in sos:
    print s
        """
        ...
    def getQConstrs(self):
        """
ROUTINE:
  getQConstrs()

PURPOSE:
  Obtain a list of quadratic constraints in the model.

ARGUMENTS:
  None.

RETURN VALUE:
  A list of QConstr objects.

EXAMPLE:
  qconstrs = model.getQConstrs()
  for c in qconstrs:
    print c.QCname
        """
        ...
    def getGenConstrs(self):
        """
ROUTINE:
  getGenConstrs()

PURPOSE:
  Obtain a list of general constraints in the model.

ARGUMENTS:
  None.

RETURN VALUE:
  A list of GenConstr objects.

EXAMPLE:
  genconstrs = model.getGenConstrs()
  for c in genconstrs:
    print c.name
        """
        ...
    def getVarByName(self, name):
        """
ROUTINE:
  getVarByName()

PURPOSE:
  Retrieve a variable with the specified name from the model.

ARGUMENTS:
  Variable name.

RETURN VALUE:
  A Var object, or None if no matching variable is found.

EXAMPLE:
  var = model.getVarByName("x1")
        """
        ...
    def getConstrByName(self, name):
        """
ROUTINE:
  getConstrByName()

PURPOSE:
  Retrieve a linear constraint with the specified name from the model.

ARGUMENTS:
  Constraint name.

RETURN VALUE:
  A Constr object, or None if no matching variable is found.

EXAMPLE:
  constr = model.getConstrByName("c1")
        """
        ...
    def getConcurrentEnv(self, num):
        """
ROUTINE:
  getConcurrentEnv()

PURPOSE:
  Retrieve a concurrent environment.  This is used to manually
  configure the parameter settings used by different threads
  in the concurrent optimizer (for LP models).   You should make
  multiple calls to getConcurrentEnv() with integer arguments from
  0 through n-1, where n is the number of different solves you
  would like to launch,  You can set parameters on each concurrent
  environment to capture the desired behavior of each concurrent
  thread.

ARGUMENTS:
  Concurrent environment number.

RETURN VALUE:
  An Env object.

EXAMPLE:
  env0 = model.getConcurrentEnv(0)
  env1 = model.getConcurrentEnv(1)

  env0.setParam('Method', 0)
  env1.setParam('Method', 1)

  model.optimize()
        """
        ...
    def discardConcurrentEnvs(self):
        """
ROUTINE:
  discardConcurrentEnvs()

PURPOSE:
  Discard concurrent environments previously created through
  getConcurrentEnv(), thus restoring the concurrent optimizer
  to its default behavior.

ARGUMENTS:
  None.

RETURN VALUE:
  None.

EXAMPLE:
  env0 = model.getConcurrentEnv(0)
  env1 = model.getConcurrentEnv(1)

  env0.setParam('Method', 0)
  env1.setParam('Method', 1)

  model.optimize()

  model.discardConcurrentEnvs()
        """
        ...
    def getMultiobjEnv(self, num):
        """
ROUTINE:
  getMultiobjEnv()

PURPOSE:
  Retrieve a multiobj environment.  This is used to manually
  configure the parameter settings used in the multiobj
  optimizer.  You should make multiple calls to getMultiobjEnv()
  with integer arguments from 0 through n-1, where n is the
  number of different priorities for the multi-objectives.
  You can set parameters on each multiobj environment to capture
  the desired behavior of the optimization for each objective
  priority

ARGUMENTS:
  Multiobj environment number.

RETURN VALUE:
  An Env object.

EXAMPLE:
  env0 = model.getMultiobjEnv(0)
  env1 = model.getMultiobjEnv(1)

  env0.setParam('Method', 0)
  env1.setParam('Method', 1)

  model.optimize()
        """
        ...
    def discardMultiobjEnvs(self):
        """
ROUTINE:
  discardMultiobjEnvs()

PURPOSE:
  Discard multiobj environments previously created through
  getMultiobjEnv(), thus restoring the multiobj optimizer
  to its default behavior.

ARGUMENTS:
  None.

RETURN VALUE:
  None.

EXAMPLE:
  env0 = model.getMultiobjEnv(0)
  env1 = model.getMultiobjEnv(1)

  env0.setParam('Method', 0)
  env1.setParam('Method', 1)

  model.optimize()

  model.discardMultiobjEnvs()
        """
        ...
    def optimize(self, callback=None):
        """
ROUTINE:
  optimize()

PURPOSE:
  Optimize the model.

ARGUMENTS:
  None.

RETURN VALUE:
  None.

EXAMPLE:
  model.optimize()

NOTES:
  The algorithm used to optimize the model depends on the model type and
  on the parameter settings.  A MIP model will always be optimized using
  the branch-and-cut algorithm.  A continuous model will be optimized
  using the dual simplex algorithm by default; the Method parameter
  can be used to choose a different algorithm.
        """
        ...
    def computeIIS(self):
        """
ROUTINE:
  computeIIS()

PURPOSE:
  Compute an Irreducible Infeasible Subsystem (IIS).

ARGUMENTS:
  None.

RETURN VALUE:
  None.

EXAMPLE:
  model.computeIIS()
        """
        ...
    def tune(self):
        """
ROUTINE:
  tune()

PURPOSE:
  Tune parameter settings

ARGUMENTS:
  None.

RETURN VALUE:
  None.

EXAMPLE:
  model.tune()
        """
        ...
    def getTuneResult(self, i):
        """
ROUTINE:
  getTuneResult()

PURPOSE:
  Retrive tuned parameter settings.

ARGUMENTS:
  Tuning result number.

RETURN VALUE:
  None.

EXAMPLE:
  model.getTuneResult(0)
        """
        ...
    def remove(self, items):
        """
ROUTINE:
  remove()

PURPOSE:
  Remove variables, linear constraints, SOS constraints, quadratic
  constraints, or general constraints from the model.

ARGUMENTS:
  items: Items to remove from model.  The argument can be
         a single Constr, Var, SOS, QConstr, or GenConstr,
         or it can be a list, tuple, or dict containing
         such items.  For a dict, the dict values will be
         removed, not the keys.

RETURN VALUE:
  None.

EXAMPLE:
  model.remove(model.getVars()[0])
  model.remove(model.getConstrs()[0:10])
        """
        ...
    def _removeone(self, item):
        ...
    def reset(self, clearall=0):
        """
ROUTINE:
  reset()

PURPOSE:
  Discard any solution information.  The next optimize() call starts
  from scratch.

ARGUMENTS:
  clearall (int, optional): Should additional information such as MIP
           starts, variable hints, branching priorities, lazy flags,
           and partition information be cleared?

RETURN VALUE:
  None.

EXAMPLE:
  model.reset()
        """
        ...
    def update(self):
        """
ROUTINE:
  update()

PURPOSE:
  Apply any pending changes to the model.

ARGUMENTS:
  None.

RETURN VALUE:
  None.

EXAMPLE:
  model.update()

NOTES:
  Model modifications are handled in a lazy fashion.  A bound change, for
  example, isn't reflected in the model until the user either calls
  model.optimize() or model.update().
        """
        ...
    def copy(self):
        """
ROUTINE:
  copy()

PURPOSE:
  Create an exact copy of a model.

ARGUMENTS:
  None.

RETURN VALUE:
  The copied Model object.

EXAMPLE:
  copy = model.copy()
  copy.optimize()
        """
        ...
    def write(self, filename):
        """
ROUTINE:
  write(filename)

PURPOSE:
  Write model data to a file.  The type of data is determined by the
  file suffix: .lp or .mps to write the model itself, .mst to write
  the current solution as a MIP start, .bas to write the current
  simplex basis, or .prm to write the modified parameters.

ARGUMENTS:
  filename (string): The name of the file to write.

RETURN VALUE:
  None.

EXAMPLE:
  model.write("model.lp")
  model.write("model.mst")
        """
        ...
    def getParamInfo(self, paramname):
        """
ROUTINE:
  getParamInfo(paramname)

PURPOSE:
  Get the current value of a parameter.

ARGUMENTS:
  paramname (string): The name of the parameter.

RETURN VALUE:
  None.

EXAMPLE:
  model.getParamInfo("NodeLimit")

NOTES:
  Returns a tuple, containing the parameter name, the paramter type,
  the current value, the minimum allowed value, the maximum allowed value,
  and the default value.

  Routine paramHelp() provides additional information on the available
  parameters.
        """
        ...
    def setObjective(self, expr, sense=None):
        """
ROUTINE:
  setObjective(expression, sense=None)

PURPOSE:
  Set the model objective equal to a LinExpr or QuadExpr

ARGUMENTS:
  expr: The desired objective function.  The objective can be
        a linear expression (LinExpr) or a quadratic expression (QuadExpr).
        This routine will replace the 'Obj' attribute on model variables
        with the corresponding values from the supplied expression.
  sense (optional): Objective sense.  By default, this method uses the
        modelSense model attribute to determine the sense.  Use
        GRB.MINIMIZE or GRB.MAXIMIZE to ignore modelSense and pick a
        specific sense.

RETURN VALUE:
  None.

EXAMPLE:
  model.setObjective(x + y)
  model.setObjective(x + y + 2*z, GRB.MAXIMIZE)
        """
        ...
    def setObjectiveN(self, expr, index, priority=0, weight=1.0, abstol=0.0, reltol=0.0, name=''):
        """
ROUTINE:
  setObjectiveN(expression, index)

PURPOSE:
  Set the model objective equal to a LinExpr or QuadExpr

ARGUMENTS:
  expr:     The desired objective function.  The objective can be
            a linear expression (LinExpr) a variable (Var) or a constant.
            This routine will replace the 'ObjNVal' attribute on model variables
            with the corresponding values from the supplied expression for
            multi-objective 'index'
  index:    Identify which multi-objective to set
  priority: Set the ObjNPriority attribute for this multi-objective (default is zero)
  weight:   Set the ObjNWeight attribute for this multi-objective (default is 1.0)
  abstol:   Set the ObjNAbsTol  attribute for this multi-objective (default is zero)
  reltol:   Set the ObjNRelTol  attribute for this multi-objective (default is zero)
  name:     multi-objective name (default is no name)

RETURN VALUE:
  None.

EXAMPLE:
  model.setObjectiveN(x + y, 1)
  model.setObjectiveN(x + y + 2*z, 2)
        """
        ...
    def getObjective(self, index=None):
        """
ROUTINE:
  getObjective()

PURPOSE:
  Query the model objective

ARGUMENTS:
  None.

RETURN VALUE:
  Model objective function, returned as either a LinExpr or QuadExpr
  object.

EXAMPLE:
  expr = model.getObjective()
        """
        ...
    def setPWLObj(self, var, x, y):
        """
ROUTINE:
  setPWLObj(var, x, y)

PURPOSE:
  Set a piecewise-linear objective for a variable

ARGUMENTS:
  var: the Var whose objective is set.
  x: A list of x coordinates.
  y: A list of y coordinates.

RETURN VALUE:
  None.

EXAMPLE:
  model.setPWLObj(v, [1, 2, 3], [1, 2, 4])
        """
        ...
    def getPWLObj(self, var):
        """
ROUTINE:
  getPWLObj(var)

PURPOSE:
  Retrieves the piecewise-linear objective for a variable

ARGUMENTS:
  var: the Var whose piecewise objective is returned.

RETURN VALUE:
  A list of tuples, where each tuple captures a point on
  the piecewise-linear function.

EXAMPLE:
  print model.getPWLObj(v)
        """
        ...
    def setParam(self, paramname, newval, verbose=True):
        """
ROUTINE:
  setParam(paramname, newvalue)

PURPOSE:
  Set a parameter to a new value.

ARGUMENTS:
  paramname (string): The name of the parameter.
  newvalue: The desired new value.  The type of the value should be
            compatible with the parameter type (e.g., an integer parameter
            will take an integer value).  One important exception: the
            string "default" will return the specified parameter to its
            default value.

RETURN VALUE:
  None.

EXAMPLE:
  model.setParam("NodeLimit", 100)
  model.setParam("TimeLimit", "default")

NOTES:
  Use this routine to change parameter values in the default environment.
  The default environment is used to initialize parameter values when a
  new model is created.  Once the model exists, changes to the default
  environment will no longer affect that model.  Use Model.setParam()
  to change parameter settings for an existing model.

  Routine paramHelp() provides additional information on the available
  parameters.
        """
        ...
    def resetParams(self):
        """
ROUTINE:
  resetParams()

PURPOSE:
  Reset all parameters to their default values.

ARGUMENTS:
  None.

RETURN VALUE:
  None.

EXAMPLE:
  model.resetParams()
        """
        ...
    def read(self, filename):
        """
ROUTINE:
  read(filename)

PURPOSE:
  Import model data from a file.  The type of data is determined by
  the file suffix: .mst for MIP start data, .bas for basis
  information, or .prm for parameter settings.

ARGUMENTS:
  filename (string): The name of the file.

RETURN VALUE:
  None.

EXAMPLE:
  model.read("start.mst")

NOTES:
  The file name may contain the '*' and '?' wildcard characters.  If
  more than one file matches, this routine will read the first match.
        """
        ...
    def getAttr(self, attrname, arg2=None):
        """
ROUTINE:
  getAttr(attrname), or
  getAttr(attrname, objects)

PURPOSE:
  Request the value of an attribute.

ARGUMENTS:
  attrname (string): The name of the requested attribute.
  objects (optional): List or dictionary of variables or constraints

RETURN VALUE:
  The attribute value.  If argument 'objects' is present,
  a list of values is returned.

EXAMPLE:
  print model.getAttr("modelName")
  print model.getAttr("lb", model.getVars())
  print model.getAttr("qcrhs", model.getQConstrs())

NOTES:
  Type "help(GRB.attr)" for a list of all available attributes.
        """
        ...
    def setAttr(self, attrname, arg1, arg2=None):
        """
ROUTINE:
  setAttr(attrname, newvalue), or
  setAttr(attrname, objects, newvalues)

PURPOSE:
  Change the value(s) of an attribute.

ARGUMENTS:
  attrname (string): The name of the requested attribute.
  objects(optional): A list of variables or constraints.
  newvalue: The desired new value.  The type of the value should be
            compatible with the attribute type (e.g., an integer parameter
            will take an integer value).

RETURN VALUE:
  The attribute value.

EXAMPLE:
  model.setAttr("modelSense", -1)
  model.setAttr("lb", [x, y, z], [1, 1, 1])

NOTES:
  Model attributes that can be set are:
    modelName:  Model name.
    modelSense: Objective sense.

  Attributes changes are handled in a lazy fashion.  The effect of a
  change isn't visible until after the next call to Model.update() or
  Model.optimize().
        """
        ...
    def message(self, msg):
        """
ROUTINE:
  message(msg)

PURPOSE:
  Write a message to the Gurobi log file.

ARGUMENTS:
  msg (string): Message to append to log file.

RETURN VALUE:
  None.

EXAMPLE:
  model.message("Found a new solution with objective " + str(obj))
        """
        ...
    def relax(self):
        """
ROUTINE:
  relax()

PURPOSE:
  Return the relaxed version of the MIP model, in which all integrality
  restrictions, SOS conditions, semi-continuous and semi-integer
  requirements on variables have been relaxed and general constraints
  have been removed.

ARGUMENTS:
  None.

RETURN VALUE:
  A new, relaxed model.

EXAMPLE:
  relaxed = model.relax()
  relaxed.optimize()

NOTES:
  If the model is already continuous, then this method produces the
  same result as cloning the model.
        """
        ...
    def fixed(self):
        """
ROUTINE:
  fixed()

PURPOSE:
  Return the fixed version of the MIP model.

ARGUMENTS:
  None.

RETURN VALUE:
  A new model, containing the fixed version of the MIP model.

EXAMPLE:
  fixed = model.fixed()
  fixed.optimize()
        """
        ...
    def presolve(self):
        """
ROUTINE:
  presolve()

PURPOSE:
  Return the presolved version of the model.

ARGUMENTS:
  None.

RETURN VALUE:
  A new model, containing the presolved version of the original model.

EXAMPLE:
  presolved = model.presolve()
  presolved.optimize()
        """
        ...
    def feasibility(self):
        """
ROUTINE:
  feasibility()

PURPOSE:
  Return the feasibility version of the MIP model.

ARGUMENTS:
  None.

RETURN VALUE:
  A copy of the given model with a cancelled objective function.

EXAMPLE:
  feasibility = model.feasibility()
  feasibility.optimize()
        """
        ...
    def linearize(self):
        """
ROUTINE:
  linearize()

PURPOSE:
  Return the linearized version of the MIQP model.

ARGUMENTS:
  None.

RETURN VALUE:
  A new model, containing the linearized version of the original model.

EXAMPLE:
  linearized = model.linearize()
  linearized.optimize()
        """
        ...
    def _Model__feasrelax(self, relaxobjtype, minrelax, vlen, clen, vars, lbpen, ubpen, constrs, rhspen):
        ...
    def feasRelaxS(self, relaxobjtype, minrelax, vrelax, crelax):
        """
ROUTINE:
  feasRelaxS(relaxobjtype, minrelax, vrelax, crelax)

PURPOSE:
  Perform a feasibility relaxation on the model.  Add penalty
  variables and a penalty objective.  Simple version; consider using
  feasRelax() if you want more control over the relaxation.

ARGUMENTS:
  relaxobjtype (int): Select the relaxation objective function.  Options
                      are linear (0), quadratic (1), or cardinality (2).
  minrelax (Boolean): Indicate whether to solve feasrelax model to
                      enforce minimal relaxation
  vrelax (Boolean): If True, variable bound violations are allowed
  crelax (Boolean): If True, constraint violations are allowed

RETURN VALUE:
  feasRelax model objective value, if minimal relaxation is enforced,
  0 otherwise

EXAMPLE:
  if model.status == GRB.INFEASIBLE:
    model.feasRelaxS(1, False, False, True)
    model.optimize()
        """
        ...
    def feasRelax(self, relaxobjtype, minrelax, vars, lbpen, ubpen, constrs, rhspen):
        """
ROUTINE:
  feasRelax(relaxobjtype, minrelax, vars, lbpen, ubpen, constrs, rhspen)

PURPOSE:
  Perform a feasibility relaxation on the model.  Add penalty
  variables and a penalty objective.  Consider using feasRelaxS()
  if you want a simpler argument list.

ARGUMENTS:
  relaxobjtype (int): Select the relaxation objective function.  Options
                      are linear (0), quadratic (1), or cardinality (2).
  minrelax (Boolean): Indicate whether to solve feasrelax model to
                      enforce minimal relaxation
  vars (list of Var): Variable that are allowed to violate bounds
  lbpen (list of float): Penalties for lower bound violations
  ubpen (list of float): Penalties for upper bound violations
  constrs (list of Constr): Constraints that can be violated
  rhspen (list of float): Penalties for constraint violations

RETURN VALUE:
  feasRelax model objective value, if minimal relaxation is enforced,
  0 otherwise

EXAMPLE:
  if model.status == GRB.INFEASIBLE:
    vars = model.getVars()
    ubpen = [1.0]*model.numVars
    model.feasRelax(1, False, vars, None, ubpen, None, None)
    model.optimize()
        """
        ...
    def printAttr(self, attrname, filter='*'):
        """
ROUTINE:
  printAttr(attrname, filter)

PURPOSE:
  Print model attribute data.

ARGUMENTS:
  attrname (string): The name of the attribute to print.  For attributes
                     with numerical values, only non-zero entries will
                     be printed.  Can be a list of attribute names,
                     in which case all listed attributes will be printed.
  filter (string): Regular expression for filtering results.   Only
                   variables/constraints whose names match the
                   (optional) filter are printed.

RETURN VALUE:
  None.

EXAMPLE:
  model.optimize()
  model.printAttr("x", "v*")     # print 'x' when var name begins with 'v'
  model.printAttr(["lb", "ub"])  # print 'lb' and 'ub' attribute values
        """
        ...
    def printQuality(self):
        """
ROUTINE:
  printQuality()

PURPOSE:
  Print solution quality statistics.

ARGUMENTS:
  None.

RETURN VALUE:
  None.

EXAMPLE:
  model.optimize()
  model.printQuality()
        """
        ...
    def printStats(self):
        """
ROUTINE:
  printStats()

PURPOSE:
  Print model statistics.

ARGUMENTS:
  None.

RETURN VALUE:
  None.

EXAMPLE:
  model.printStats()
        """
        ...
    def addVar(self, lb=0.0, ub=1e+100, obj=0.0, vtype='C', name='', column=None):
        """
ROUTINE:
  addVar(lb, ub, obj, vtype, name, column)

PURPOSE:
  Add a variable to the model.

ARGUMENTS:
  lb (float): Lower bound (default is zero)
  ub (float): Upper bound (default is infinite)
  obj (float): Objective coefficient (default is zero)
  vtype (string): Variable type (default is GRB.CONTINUOUS)
  name (string): Variable name (default is no name)
  column (Column): Initial coefficients for column (default is None)

RETURN VALUE:
  The created Var object.

EXAMPLE:
  v = model.addVar(ub=2.0, name="NewVar")
        """
        ...
    def addVars(self, *indexes, **kwargs):
        """
addVars(*indexes, lb=0.0, ub=GRB.INFINITY, obj=0.0, vtype=GRB.CONTINUOUS,
           name="")

Add variables in bulk, given one or more lists or integers that serve as
indexes for the variables.  Returns a dictionary of Var objects, indexed by
the values (or tuples of values) from the index set.

The optional parameters (lb, ub, obj, vtype, name) work similar
to the addVar() method, with the following exceptions:
1. The parameter name is required (ex: vtype=GRB.BINARY)
2. You can specify the value as a scalar, a list or a dictionary.  For a scalar,
   the value will be used for all variables; for a list, the values must be
   in the same order as the index set; for a dictionary, they must be indexed
   by the variable index.
3. If you specify a scalar string for name, the variable name will be
   subscripted automatically.
        """
        ...
    def addLConstr(self, lhs, sense=None, rhs=None, name=''):
        """
ROUTINE:
  addLConstr(lhs, sense, rhs, name)

PURPOSE:
  Add a linear constraint to the model.

ARGUMENTS:
  lhs (float, Var, LinExpr or TempConstr): Left-hand side
  sense (char): Constraint sense (e.g., GRB.LESS_EQUAL)
  rhs (float, Var, or LinExpr): Right-hand side
  name (string): Constraint name (default is no name)

RETURN VALUE:
  The created Constr object.

EXAMPLE:
  c = model.addLConstr(x + y <= 1)
  c = model.addLConstr(LinExpr([1.0,1.0], [x,y]), GRB.LESS_EQUAL, 1)
  c = model.addLConstr(lhs = 5 * x + y, sense = GRB.LESS_EQUAL, rhs = 3 * z, name = "C1")
        """
        ...
    def _Model__addConstr(self, expr, sense, lower, upper, name):
        ...
    def addConstr(self, lhs, sense=None, rhs=None, name=''):
        """
ROUTINE:
  addConstr(lhs, sense, rhs, name)

PURPOSE:
  Add a constraint to the model.

ARGUMENTS:
  lhs (float, Var, LinExpr or TempConstr): Left-hand side
  sense (char): Constraint sense (e.g., GRB.LESS_EQUAL)
  rhs (float, Var, or LinExpr): Right-hand side
  name (string): Constraint name (default is no name)

RETURN VALUE:
  The created Constr object.

EXAMPLE:
  c = model.addConstr(x + y <= 1)
  c = model.addConstr(x + y + z == [1, 2])
  c = model.addConstr(x*x + y*y <= 1)
  c = model.addConstr(z == and_(y, x, w))
  c = model.addConstr(z == min_(x, y))
  c = model.addConstr((w == 1) >> (x + y <= 1))
        """
        ...
    def addQConstr(self, lhs, sense=None, rhs=None, name=''):
        """
ROUTINE:
  addQConstr(lhs, sense, rhs, name)

PURPOSE:
  Add a quadratic constraint to the model.

ARGUMENTS:
  lhs (float, Var, LinExpr, or QuadExpr): Left-hand side
  sense (char): Constraint sense (e.g., GRB.LESS_EQUAL)
  rhs (float, Var, LinExpr, or QuadExpr): Right-hand side
  name (string): Constraint name (default is no name)

RETURN VALUE:
  The created QConstr object.

EXAMPLE:
  qc = model.addQConstr(x*x + y*y <= 1)
        """
        ...
    def addRange(self, expr, lower, upper, name=''):
        """
ROUTINE:
  addRange(expr, lhs, rhs, name)

PURPOSE:
  Add a range constraint to the model.

ARGUMENTS:
  expr (Var, or LinExpr): Linear expression being constrained
  lower (float): Lower bound on linear expression
  upper (float): Upper bound on linear expression
  name (string): Constraint name (default is no name)

RETURN VALUE:
  The created Constr object.

EXAMPLE:
  c = model.addRange(x + y, 1.0, 2.0)
        """
        ...
    def addConstrs(self, constrs, name=''):
        """
addConstrs(constrs, name="")

Add constraints in bulk, using a generator expression.  Returns a dictionary
of Constr objects, indexed by the values (or tuples of values) used by the
generator expression.

If you specify a name, the constraints will get that name.  If name is a scalar
string, the names will be subscripted by the generator index.  If name
equals the underscore character ("_"), then the names will equal the index value.
        """
        ...
    def addSOS(self, type, vars, wts=None):
        """
ROUTINE:
  addSOS(type, vars, wts)

PURPOSE:
  Add an SOS constraint to the model.

ARGUMENTS:
  type (Int): SOS type 1 (GRB.SOS_TYPE1) or type 2 (GRB.SOS_TYPE2)
  vars (list of Var): Variables in SOS
  wts (list of float): Weights for variables in SOS

RETURN VALUE:
  The created SOS object.

EXAMPLE:
  sos = model.addSOS(GRB.SOS_TYPE1, [x, y, z])
        """
        ...
    def addGenConstrMax(self, resvar, vars, constant=None, name=''):
        """
ROUTINE:
  addGenConstrMax(resvar, vars, constant, name)

PURPOSE:
  Add a general constraint of type MAX to the model.

ARGUMENTS:
  resvar (Var): Resultant variable of MAX constraint
  vars (list of Var, or tupledict): Argument variables of MAX constraint
  constant (float, optional): Constant of MAX constraint
  name (string, optional): Constraint name (default is no name)

RETURN VALUE:
  The created general constraint object.

EXAMPLE:
  genconstr = model.addGenConstrMax(z, [x1, x2, x3], 17.5, "myMaxConstr")
        """
        ...
    def addGenConstrMin(self, resvar, vars, constant=None, name=''):
        """
ROUTINE:
  addGenConstrMin(resvar, vars, constant, name)

PURPOSE:
  Add a general constraint of type MIN to the model.

ARGUMENTS:
  resvar (Var): Resultant variable of MIN constraint
  vars (list of Var, or tupledict): Argument variables of MIN constraint
  constant (float, optional): Constant of MIN constraint
  name (string, optional): Constraint name (default is no name)

RETURN VALUE:
  The created general constraint object.

EXAMPLE:
  genconstr = model.addGenConstrMin(z, [x1, x2, x3], 17.5, "myMinConstr")
        """
        ...
    def addGenConstrAbs(self, resvar, argvar, name=''):
        """
ROUTINE:
  addGenConstrAbs(resvar, argvar, name)

PURPOSE:
  Add a general constraint of type ABS to the model.

ARGUMENTS:
  resvar (Var): Resultant variable of ABS constraint
  argvar (Var): Argument variable of ABS constraint
  name (string): Constraint name (default is no name)

RETURN VALUE:
  The created general constraint object.

EXAMPLE:
  genconstr = model.addGenConstrAbs(z, x1, "myAbsConstr")
        """
        ...
    def addGenConstrAnd(self, resvar, vars, name=''):
        """
ROUTINE:
  addGenConstrAnd(resvar, vars, name)

PURPOSE:
  Add a general constraint of type AND to the model.

ARGUMENTS:
  resvar (Var): Resultant variable of AND constraint
  vars (list of Var, or tupledict): Argument variables of AND constraint
  name (string): Constraint name (default is no name)

RETURN VALUE:
  The created general constraint object.

EXAMPLE:
  genconstr = model.addGenConstrAnd(z, [x1, x2, x3], "myAndConstr")
        """
        ...
    def addGenConstrOr(self, resvar, vars, name=''):
        """
ROUTINE:
  addGenConstrOr(resvar, vars, name)

PURPOSE:
  Add a general constraint of type OR to the model.

ARGUMENTS:
  resvar (Var): Resultant variable of OR constraint
  vars (list of Var, or tupledict): Argument variables of OR constraint
  name (string): Constraint name (default is no name)

RETURN VALUE:
  The created general constraint object.

EXAMPLE:
  genconstr = model.addGenConstrOr(z, [x1, x2, x3], "myOrConstr")
        """
        ...
    def addGenConstrIndicator(self, binvar, binval, lhs, sense=None, rhs=None, name=''):
        """
ROUTINE:
  addGenConstrIndicator(binvar, binval, lhs, sense, rhs, name)

PURPOSE:
  Add a general constraint of type INDICATOR to the model.

ARGUMENTS:
  GRB.GENCONSTR_INDICATOR (option 1):
    binvar (Var): Antecedent variable of indicator constraint
    binval (Boolean): Value of antecedent variable that activates the linear constraint
    lhs (float, Var, or LinExpr): Linear expression of constraint triggered by the indicator
    sense (char): Sense of constraint triggered by the indicator (e.g., GRB.LESS_EQUAL)
    rhs (float): Right-hand side of linear constraint triggered by the indicator
    name (string): Constraint name (default is no name)

  GRB.GENCONSTR_INDICATOR (option 2):
    binvar (Var): Antecedent variable of indicator constraint
    binval (Boolean): Value of antecedent variable that activates the linear constraint
    lhs (TempConstr): Linear constraint triggered by indicator
    name (string): Constraint name (default is no name)

RETURN VALUE:
  The created general constraint object.

EXAMPLE:
  genconstr = model.addGenConstr(z, 0, 2*x1 - 1.5*x2 + 3.0*x3 == 4.5, name="myIndicatorConstr")
        """
        ...
    def getCoeff(self, constr, var):
        """
ROUTINE:
  getCoeff(constr, var)

PURPOSE:
  Retrieve a coefficient from the constraint matrix.

ARGUMENTS:
  constr (Constr): Constraint of interest
  var (Var): Variable of interest

RETURN VALUE:
  The coefficient for 'var' in 'constr'

EXAMPLE:
  coeff = model.getCoeff(model.getConstrs()[0], model.getVars()[0])
        """
        ...
    def chgCoeff(self, constr, var, newvalue):
        """
ROUTINE:
  chgCoeff(constr, var, newvalue)

PURPOSE:
  Change a coefficient in the constraint matrix.

ARGUMENTS:
  constr (Constr): The constraint for the changed coefficient
  var (Var): The variable for the changed coefficient
  newvalue (float): Desired new value

RETURN VALUE:
  None.

EXAMPLE:
  model.chgCoeff(model.getConstrs()[0], model.getVars()[0], 1.0)
        """
        ...
    def getCol(self, var):
        """
ROUTINE:
  getCol(var)

PURPOSE:
  Obtain all terms associated with a Var.

ARGUMENTS:
  None.

RETURN VALUE:
  A Column object containing a list of terms associated with the Var.

EXAMPLE:
  col = model.getCol(model.getVars()[0])
  for i in range(col.size()):
    print col.getCoeff(i), expr.getConstr(i)
        """
        ...
    def getRow(self, constr):
        """
ROUTINE:
  getRow(constr)

PURPOSE:
  Obtain all terms associated with a constraint.

ARGUMENTS:
  None.

RETURN VALUE:
  A LinExpr object containing the left-hand side of the constraint.

EXAMPLE:
  expr = model.getRow(model.getConstrs()[0])
  for i in range(expr.size()):
    print expr.getCoeff(i), expr.getVar(i)
        """
        ...
    def getSOS(self, sos):
        """
ROUTINE:
  getSOS(sos)

PURPOSE:
  Obtain all variables and weights associated with an SOS constraint.

ARGUMENTS:
  None.

RETURN VALUE:
  A tuple that contains the SOS type (1 or 2), the list of member
  Var objects, and the associated SOS weights.

EXAMPLE:
  (type, vars, weights) = model.getSOS(model.getSOSs()[0])
        """
        ...
    def getQCRow(self, qc):
        """
ROUTINE:
  getQCRow(qc)

PURPOSE:
  Obtain all terms associated with a quadratic constraint.

ARGUMENTS:
  None.

RETURN VALUE:
  A QuadExpr object containing the left-hand side of the constraint.

EXAMPLE:
  expr = model.getQCRow(model.getQConstrs()[0])
  model.addConstr(expr >= 0)
        """
        ...
    def getGenConstrMax(self, genconstr):
        """
ROUTINE:
  getGenConstrMax(genconstr)

PURPOSE:
  Obtain all data associated with a general constraint of type MAX.

ARGUMENTS:
  None.

RETURN VALUE:
  A tuple (resvar, vars, constant) that contains the data for the general constraint.
    resvar (Var): Resultant variable of MAX constraint
    vars (list of Var): Operand variables of MAX constraint
    constant (float): Constant of MAX constraint

EXAMPLE:
  (resvar, vars, constant) = model.getGenConstrMax(model.getGenConstrs()[0])
        """
        ...
    def getGenConstrMin(self, genconstr):
        """
ROUTINE:
  getGenConstrMin(genconstr)

PURPOSE:
  Obtain all data associated with a general constraint of type MIN.

ARGUMENTS:
  None.

RETURN VALUE:
  A tuple (resvar, vars, constant) that contains the data for the general constraint.
    resvar (Var): Resultant variable of MIN constraint
    vars (list of Var): Operand variables of MIN constraint
    constant (float): Constant of MIN constraint

EXAMPLE:
  (resvar, vars, constant) = model.getGenConstrMin(model.getGenConstrs()[0])
        """
        ...
    def getGenConstrAbs(self, genconstr):
        """
ROUTINE:
  getGenConstrAbs(genconstr)

PURPOSE:
  Obtain all data associated with a general constraint of type ABS.

ARGUMENTS:
  None.

RETURN VALUE:
  A tuple (resvar, argvar) that contains the data for the general constraint.
    resvar (Var): Resultant variable of ABS constraint
    argvar (Var): Argument variable of ABS constraint

EXAMPLE:
  (resvar, argvar) = model.getGenConstrAbs(model.getGenConstrs()[0])
        """
        ...
    def getGenConstrAnd(self, genconstr):
        """
ROUTINE:
  getGenConstrAnd(genconstr)

PURPOSE:
  Obtain all data associated with a general constraint of type AND.

ARGUMENTS:
  None.

RETURN VALUE:
  A tuple (resvar, vars) that contains the data for the general constraint.
    resvar (Var): Resultant variable of AND constraint
    vars (list of Var): Operand variables of AND constraint

EXAMPLE:
  (resvar, vars) = model.getGenConstrAnd(model.getGenConstrs()[0])
        """
        ...
    def getGenConstrOr(self, genconstr):
        """
ROUTINE:
  getGenConstrOr(genconstr)

PURPOSE:
  Obtain all data associated with a general constraint of type OR.

ARGUMENTS:
  None.

RETURN VALUE:
  A tuple (resvar, vars) that contains the data for the general constraint.
    resvar (Var): Resultant variable of OR constraint
    vars (list of Var): Operand variables of OR constraint

EXAMPLE:
  (resvar, vars) = model.getGenConstrOr(model.getGenConstrs()[0])
        """
        ...
    def getGenConstrIndicator(self, genconstr):
        """
ROUTINE:
  getGenConstrIndicator(genconstr)

PURPOSE:
  Obtain all data associated with a general constraint of type INDICATOR.

ARGUMENTS:
  None.

RETURN VALUE:
  A tuple (binvar, binval, vars, vals, sense, rhs) that contains the data for the general constraint.
    binvar (Var): Antecedent variable of indicator constraint
    binval (Boolean): Value of antecedent variable that activates the linear constraint
    expr (LinExpr): LinExpr object containing the left-hand side of the constraint triggered by the indicator
    sense (char): Sense of linear constraint triggered by the indicator (e.g., GRB.LESS_EQUAL)
    rhs (float): Right-hand side of linear constraint triggered by the indicator

EXAMPLE:
  (binvar, binval, expr, sense, rhs) = model.getGenConstr(model.getGenConstrs()[0])
        """
        ...
    def terminate(self):
        """
ROUTINE:
  terminate()

PURPOSE:
  Terminate any optimization in progress (from a callback).

ARGUMENTS:
  None.

RETURN VALUE:
  None.

EXAMPLE:
  model.terminate()
        """
        ...
    def cbStopOneMultiObj(self, objnum):
        """
ROUTINE:
  cbStopOneMultiObj(objnum)

PURPOSE:
  terminate individual optimization for the multi-objectives of the MIP model (from a callback).

ARGUMENTS:
  objnum

RETURN VALUE:
  None

EXAMPLE:
  model.cbStopOneMultiObj(objnum)
        """
        ...
    def cbGet(self, what):
        ...
    def cbGetNodeRel(self, vars):
        ...
    def cbGetSolution(self, vars):
        ...
    def cbSetSolution(self, vars, solution):
        ...
    def cbUseSolution(self):
        ...
    def cbCut(self, lhs, sense=None, rhs=None):
        ...
    def cbLazy(self, lhs, sense=None, rhs=None):
        ...
    def _Model__cbCutOrLazy(self, lhs, sense, isCut):
        ...
    def _Model__getattrinfo(self, attrname):
        ...
    def _Model__gettypedattr(self, attrname, attrtype):
        ...
    def _Model__gettypedattrlist(self, attrname, attrtype, inputlist):
        ...
    def _Model__getupdatemode(self):
        ...
    numConstrs = ...
    """Number of constraints"""
    numVars = ...
    """Number of variables"""
    numSOS = ...
    """Number of SOS constraints"""
    numQConstrs = ...
    """Number of quadrtic constraints"""
    numGenConstrs = ...
    """Number of general constraints"""
    numNZs = ...
    """Number of non-zero coefficients"""
    numQNZs = ...
    """Number of non-zero quadratic objective coefficients"""
    numIntVars = ...
    """Number of integer variables (including binary variables)"""
    numBinVars = ...
    """Number of binary variables"""
    modelName = ...
    """Model name"""
    modelSense = ...
    """Model sense: minimization (1) or maximization (-1)"""
    objCon = ...
    """Constant offset for objective function"""
    objVal = ...
    """Objective value for current solution"""
    objBound = ...
    """Best available lower bound on solution objective"""
    poolObjBound = ...
    """Bound on objective for undiscovered solutions"""
    poolObjVal = ...
    """Retrieve the objective value of an alternate MIP solution"""
    MIPGap = ...
    """Current relative MIP optimality gap"""
    runtime = ...
    """Runtime (in seconds) for most recent optimization"""
    status = ...
    """Current status of model (help(GRB) gives a list of codes)"""
    solCount = ...
    """Number of stored solutions"""
    iterCount = ...
    """Number of simplex iterations performed"""
    nodeCount = ...
    """Number of branch-and-cut nodes explored"""
    barIterCount = ...
    """Number of barrier iterations performed"""
    isMIP = ...
    """Indicates whether the model is MIP (1) or not (0)"""
    isQP = ...
    """Indicates whether the model has a quadratic objective"""
    isQCP = ...
    """Indicates whether the model has quadratic constraints"""
    isMultiObj = ...
    """Indicates whether the model has multiple objectives"""
    IISMinimal = ...
    """Is computed IIS minimal?"""
    kappa = ...
    """Condition number of current LP basis"""
    maxCoeff = ...
    """Maximum constraint coefficient (in absolute value)"""
    minCoeff = ...
    """Minimum non-zero constraint coefficient (in absolute value)"""
    maxBound = ...
    """Maximum finite variable bound (in absolute value)"""
    minBound = ...
    """Minimum non-zero variable bound (in absolute value)"""
    maxObjCoeff = ...
    """Maximum objective coefficient (in absolute value)"""
    minObjCoeff = ...
    """Minimum objective coefficient (in absolute value)"""
    maxRHS = ...
    """Maximum linear constraint right-hand side (in absolute value)"""
    minRHS = ...
    """Minimum linear constraint right-hand side (in absolute value)"""
    maxQCRHS = ...
    """Maximum quadratic constraint right-hand side (in absolute value)"""
    minQCRHS = ...
    """Minimum quadratic constraint right-hand side (in absolute value)"""
    maxQCCoeff = ...
    """Maximum quadratic constraint coefficient in quadratic part (in absolute value)"""
    minQCCoeff = ...
    """Minimum non-zero quadratic constraint coefficient in quadratic part (in absolute value)"""
    maxQCLCoeff = ...
    """Maximum quadratic constraint coefficient in linear part (in absolute value)"""
    minQCLCoeff = ...
    """Minimum non-zero quadratic constraint coefficient in linear part (in absolute value)"""
    maxQObjCoeff = ...
    """Maximum quadratic objective coefficient (in absolute value)"""
    minQObjCoeff = ...
    """Minimum quadratic objective coefficient (in absolute value)"""
    farkasProof = ...
    """Infeasible amount for Farkas proof for infeasible models"""
    numStart = ...
    """number of MIP starts"""
class GenExpr(object):
    """
General expression class.  Used by General constraints.
    """
    def __init__(self, f, v):
        ...
    def __repr__(self):
        ...
    def __ne__(self, other):
        ...
    def __eq__(delf, other):
        ...
def exprfactory(*args, **kwargs) -> Any:
    ...
def exprfactory_iter(*args, **kwargs) -> Any:
    ...
def abs_(arg):
    """
Return the absolute value of x, or the absolute value general constraint
    """
    ...
def all_(*args, **kwargs):
    """
Return the general constraint of type and
    """
    ...
def any_(*args, **kwargs):
    """
Return the general constraint of type or
    """
    ...
def max_(*args, **kwargs):
    """
Return the general constraint of type max
    """
    ...
def min_(*args, **kwargs):
    """
Return the general constraint of type min
    """
    ...
def and_(*args, **kwargs):
    """
Return the general constraint of type and
    """
    ...
def or_(*args, **kwargs):
    """
Return the general constraint of type or
    """
    ...
def multidict(data):
    """
ROUTINE:
  multidict(data)
PURPOSE:
  Split a single dictionary into multiple dictionaries.
ARGUMENTS:
  data: A dictionary that maps each key to a list of 'n' values.
RETURN VALUE:
  A list of the shared keys, followed by individual tupledicts.
EXAMPLE:
  (keys, dict1, dict2) = multidict( {
           'key1': [1, 2],
           'key2': [1, 3],
           'key3': [1, 4] } )
    """
    ...
class AttrConstClass(object):
    """
Attributes are used throughout the Gurobi interface to query and
modify model properties.  You refer to them as you would any
other object attribute.  For example, "print model.numConstrs"
prints the number of constraints in a model.  You can assign new values to
some attributes (e.g., model.ModelName = "New"), while others can only
be queried.  Note that attribute modification is handled in a lazy fashion,
so you won't see the effect of a change until after the next call to
Model.update() or Model.optimize().

Capitalization is ignored in Gurobi attribute names, so
model.numConstrs and model.NumConstrs are equivalent.

Gurobi attributes can be grouped into the following categories:

General model attributes (e.g., model.numConstrs):

  numConstrs: Number of constraints
  numVars: Number of variables
  numSOS: Number of SOS constraints
  numQConstrs: Number of quadrtic constraints
  numGenConstrs: Number of general constraints
  numNZs: Number of non-zero coefficients
  numQNZs: Number of non-zero quadratic objective coefficients
  numIntVars: Number of integer variables (including binary variables)
  numBinVars: Number of binary variables
  modelName: Model name
  modelSense: Model sense: minimization (1) or maximization (-1)
  objCon: Constant offset for objective function
  objVal: Objective value for current solution
  objBound: Best available lower bound on solution objective
  poolObjBound: Bound on objective for undiscovered solutions
  poolObjVal: Retrieve the objective value of an alternate MIP solution
  MIPGap: Current relative MIP optimality gap
  runtime: Runtime (in seconds) for most recent optimization
  status: Current status of model (help(GRB) gives a list of codes)
  solCount: Number of stored solutions
  iterCount: Number of simplex iterations performed
  nodeCount: Number of branch-and-cut nodes explored
  barIterCount: Number of barrier iterations performed
  isMIP: Indicates whether the model is MIP (1) or not (0)
  isQP: Indicates whether the model has a quadratic objective
  isQCP: Indicates whether the model has quadratic constraints
  isMultiObj: Indicates whether the model has multiple objectives
  IISMinimal: Is computed IIS minimal?
  kappa: Condition number of current LP basis
  maxCoeff: Maximum constraint coefficient (in absolute value)
  minCoeff: Minimum non-zero constraint coefficient (in absolute value)
  maxBound: Maximum finite variable bound (in absolute value)
  minBound: Minimum non-zero variable bound (in absolute value)
  maxObjCoeff: Maximum objective coefficient (in absolute value)
  minObjCoeff: Minimum objective coefficient (in absolute value)
  maxRHS: Maximum linear constraint right-hand side (in absolute value)
  minRHS: Minimum linear constraint right-hand side (in absolute value)
  maxQCRHS: Maximum quadratic constraint right-hand side (in absolute value)
  minQCRHS: Minimum quadratic constraint right-hand side (in absolute value)
  maxQCCoeff: Maximum quadratic constraint coefficient in quadratic part (in absolute value)
  minQCCoeff: Minimum non-zero quadratic constraint coefficient in quadratic part (in absolute value)
  maxQCLCoeff: Maximum quadratic constraint coefficient in linear part (in absolute value)
  minQCLCoeff: Minimum non-zero quadratic constraint coefficient in linear part (in absolute value)
  maxQObjCoeff: Maximum quadratic objective coefficient (in absolute value)
  minQObjCoeff: Minimum quadratic objective coefficient (in absolute value)
  farkasProof: Infeasible amount for Farkas proof for infeasible models
  numStart: number of MIP starts

Variable attributes (e.g., var.lb):

  lb: Lower bound
  ub: Upper bound
  obj: Objective coefficient
  vType: Variable type (GRB.CONTINUOUS, GRB.BINARY, GRB.INTEGER,
                        GRB.SEMICONT, or GRB.SEMIINT)
  varName: Variable name
  x: Solution value
  rc: Reduced cost
  xn: Solution value in alternate MIP solution
  start: Start vector (use GRB.UNDEFINED to leave a value unspecified)
  vBasis: Basis status
  varHintVal: Variable hint value
  varHintPri: Variable hint priority
  branchPriority: Variable branch priority
  partition: Variable partition
  IISLB: Does LB participate in IIS? (for infeasible models)
  IISUB: Does UB participate in IIS? (for infeasible models)
  SAObjLow: Smallest objective coefficient for which basis remains optimal
  SAObjUp: Largest objective coefficient for which basis remains optimal
  SALBLow: Smallest lower bound for which basis remains optimal
  SALBUp: Largest lower bound for which basis remains optimal
  SAUBLow: Smallest upper bound for which basis remains optimal
  SAUBUp: Largest upper bound for which basis remains optimal
  unbdRay: Unbounded ray
  pStart: Primal solution (for warm-starting simplex)
  preFixVal: The value of the variable (for variables fixed by presolve)
  varPreStat: Status of variable in presolved model

Constraint attributes (e.g., constr.sense):

  sense: Constraint sense
  rhs: Constraint right-hand side value
  constrName: Constraint name
  pi: Dual value
  slack: Constraint slack
  cBasis: Basis status
  lazy: Lazy constraint flag
  IISConstr: Does constraint participate in IIS? (for infeasible models)
  SARHSLow: Smallest RHS value for which basis remains optimal
  SARHSUp: Largest RHS value for which basis remains optimal
  farkasDual: Farkas dual for infeasible models
  dStart: Dual solution (for warm-starting simplex)

SOS (e.g., sos.IISSOS):

  IISSOS: Does SOS participate in IIS? (for infeasible models)

Quadratic constraint attributes (e.g., qc.sense):

  QCsense: Quadratic constraint sense
  QCrhs: Quadratic constraint right-hand side value
  QCname: Quadratic constraint name
  IISQConstr: Does QC participate in IIS? (for infeasible models)
  QCpi: Dual value
  QCslack: Quadratic constraint slack

GenConstr (e.g., genconstr.IISGenConstr):

  GenConstrType: General constraint type (e.g., GRB.GENCONSTR_MAX)
  GenConstrName: General constraint name
  IISGenConstr: Does general constraint participate in IIS? (for infeasible models)

Solution quality (e.g., model.constrVio):

  You generally access quality information through Model.printQuality().
  Please refer to the Attributes section of the Gurobi Reference Manual for
  the full list of quality attributes.

Multi-objectives

  ObjN: objectives of multi-objectives
  ObjNCon: constant terms of multi-objectives
  ObjNPriority: priorities of multi-objectives
  ObjNWeight: weights of multi-objectives
  ObjNRelTol: relative tolerances of multi-objectives
  ObjNAbsTol: absolute tolerances of multi-objectives
  ObjNVal: objective value for multi-objectives
  ObjNName: names of multi-objectives
  NumObj: number of multi-objectives
    """
    def __setattr__(self, name, value):
        ...
    NumConstrs: str = ...
    NumVars: str = ...
    NumSOS: str = ...
    NumQConstrs: str = ...
    NumGenConstrs: str = ...
    NumNZs: str = ...
    NumQNZs: str = ...
    NumQCNZs: str = ...
    NumIntVars: str = ...
    NumBinVars: str = ...
    NumPWLObjVars: str = ...
    ModelName: str = ...
    ModelSense: str = ...
    ObjCon: str = ...
    IsMIP: str = ...
    IsQP: str = ...
    IsQCP: str = ...
    IsMultiObj: str = ...
    IISMinimal: str = ...
    Kappa: str = ...
    KappaExact: str = ...
    MaxCoeff: str = ...
    MinCoeff: str = ...
    MaxBound: str = ...
    MinBound: str = ...
    MaxObjCoeff: str = ...
    MinObjCoeff: str = ...
    MaxRHS: str = ...
    MinRHS: str = ...
    MaxQCRHS: str = ...
    MinQCRHS: str = ...
    MaxQCCoeff: str = ...
    MinQCCoeff: str = ...
    MaxQCLCoeff: str = ...
    MinQCLCoeff: str = ...
    MaxQObjCoeff: str = ...
    MinQObjCoeff: str = ...
    ObjVal: str = ...
    ObjBound: str = ...
    ObjBoundC: str = ...
    PoolObjBound: str = ...
    PoolObjVal: str = ...
    MIPGap: str = ...
    Runtime: str = ...
    Status: str = ...
    SolCount: str = ...
    IterCount: str = ...
    NodeCount: str = ...
    BarIterCount: str = ...
    FarkasProof: str = ...
    NumStart: str = ...
    TuneResultCount: str = ...
    LicenseExpiration: str = ...
    LB: str = ...
    UB: str = ...
    Obj: str = ...
    VType: str = ...
    VarName: str = ...
    X: str = ...
    RC: str = ...
    Xn: str = ...
    BarX: str = ...
    Start: str = ...
    VarHintVal: str = ...
    VarHintPri: str = ...
    BranchPriority: str = ...
    Partition: str = ...
    VBasis: str = ...
    PWLObjCvx: str = ...
    IISLB: str = ...
    IISUB: str = ...
    SAObjLow: str = ...
    SAObjUp: str = ...
    SALBLow: str = ...
    SALBUp: str = ...
    SAUBLow: str = ...
    SAUBUp: str = ...
    UnbdRay: str = ...
    PStart: str = ...
    PreFixVal: str = ...
    VarPreStat: str = ...
    Sense: str = ...
    RHS: str = ...
    ConstrName: str = ...
    Pi: str = ...
    Slack: str = ...
    CBasis: str = ...
    IISConstr: str = ...
    SARHSLow: str = ...
    SARHSUp: str = ...
    FarkasDual: str = ...
    DStart: str = ...
    Lazy: str = ...
    IISSOS: str = ...
    QCSense: str = ...
    QCRHS: str = ...
    QCName: str = ...
    IISQConstr: str = ...
    QCPi: str = ...
    QCSlack: str = ...
    GenConstrType: str = ...
    GenConstrName: str = ...
    IISGenConstr: str = ...
    BoundVio: str = ...
    BoundSVio: str = ...
    BoundVioIndex: str = ...
    BoundSVioIndex: str = ...
    BoundVioSum: str = ...
    BoundSVioSum: str = ...
    ConstrVio: str = ...
    ConstrSVio: str = ...
    ConstrVioIndex: str = ...
    ConstrSVioIndex: str = ...
    ConstrVioSum: str = ...
    ConstrSVioSum: str = ...
    ConstrResidual: str = ...
    ConstrSResidual: str = ...
    ConstrResidualIndex: str = ...
    ConstrSResidualIndex: str = ...
    ConstrResidualSum: str = ...
    ConstrSResidualSum: str = ...
    DualVio: str = ...
    DualSVio: str = ...
    DualVioIndex: str = ...
    DualSVioIndex: str = ...
    DualVioSum: str = ...
    DualSVioSum: str = ...
    DualResidual: str = ...
    DualSResidual: str = ...
    DualResidualIndex: str = ...
    DualSResidualIndex: str = ...
    DualResidualSum: str = ...
    DualSResidualSum: str = ...
    ComplVio: str = ...
    ComplVioIndex: str = ...
    ComplVioSum: str = ...
    IntVio: str = ...
    IntVioIndex: str = ...
    IntVioSum: str = ...
    ObjN: str = ...
    ObjNCon: str = ...
    ObjNPriority: str = ...
    ObjNWeight: str = ...
    ObjNRelTol: str = ...
    ObjNAbsTol: str = ...
    ObjNVal: str = ...
    ObjNName: str = ...
    NumObj: str = ...
    Server: str = ...
    JobID: str = ...
class ParamClass(object):
    """
Gurobi parameters are used to control the optimization process.  They all
have default values, but their values can be queried or modified through the
Model.Params class (e.g., 'limit = model.Params.nodeLimit',
'model.Params.MIPGap = 0.0').

Parameters fall into the following categories:

Termination: affect the termination of an optimize() call
  BarIterLimit: limits the number of barrier iterations performed
  BestBdStop: sets a best bound values at which optimization should stop
  BestObjStop: sets an objective value at which optimization should stop
  Cutoff: sets a target objective value
  IterationLimit: limits the number of simplex iterations performed
  NodeLimit: limits the number of MIP nodes explored
  SolutionLimit: sets a target for the number of feasible solutions found
  TimeLimit: limits the total time expended (in seconds)

Tolerances: control the allowable feasibility or optimality violations
  BarConvTol: barrier convergence tolerance
  BarQCPConvTol: barrier convergence tolerance for QCP models
  FeasibilityTol: primal feasibility tolerance
  IntFeasTol: integer feasibility tolerance
  MarkowitzTol: threshold pivoting tolerance
  MIPGap: target relative MIP optimality gap
  MIPGapAbs: target absolute MIP optimality gap
  OptimalityTol: dual feasibility tolerance
  PSDTol: QP positive semidefinite tolerance

Simplex: affect the simplex algorithms
  InfUnbdInfo: makes additional information available for infeasible or
               unbounded LP models
  NormAdjust: chooses different pricing norm variants
  ObjScale: controls objective scaling
  PerturbValue: controls the magnitude of any simplex perturbations
  Quad: turns quad precision on or off
  ScaleFlag: turns model scaling on or off
  Sifting: dual simplex sifting strategy for LP, MIP root and MIP nodes
  SiftMethod: chooses from dual, primal and barrier to solve sifting
              subproblems
  SimplexPricing: determines variable pricing strategy

Barrier: affect the barrier algorithms
  BarCorrectors: limits the number of central corrections
  BarHomogeneous: selects the barrier homogeneous algorithm
  BarOrder: determines the fill reducing ordering strategy
  Crossover: controls barrier crossover
  CrossoverBasis: controls initial crossover basis construction
  QCPDual: enables dual variable computation for continuous QCP models

MIP: affect the MIP algorithms
  BranchDir: controls the branching node selection
  ConcurrentMIP: enables concurrent MIP optimization
  ConcurrentJobs: enables distributed concurrent optimization
  DegenMoves: limit degenerate simplex moves
  Disconnected: controls the disconnected component strategy
  Heuristics: controls the amount of time spent in MIP heuristics
  ImproveStartGap: gap at which to switch MIP search strategies
  ImproveStartNodes: node count at which to switch MIP search strategies
  ImproveStartTime: time at which to switch MIP search strategies
  MinRelNodes: controls the minimum relaxation heuristic
  MIPFocus: affects the high-level MIP search strategy
  MIQCPMethod: controls whether to solve QCP node relaxation or to use OA
  NodefileDir: determines the directory used to store nodes on disk
  NodefileStart: memory nodes may use (in GB) before being written to disk
  NodeMethod: determines the algorithm used to solve MIP node relaxations
  NoRelHeuristic: determines whether the NoRel heuristic should be used
  PartitionPlace: controls when the partition heursitic runs
  PumpPasses: controls the feasibility pump heuristic
  RINS: sets the frequency of the RINS heuristic
  SolutionNumber: controls access to alternate MIP solutions
  SubMIPNodes: limits the numbers of nodes explored in a RINS sub-MIP
  Symmetry: controls access to alternate MIP solutions
  VarBranch: controls the branch variable selection strategy
  ZeroObjNodes: controls the zero objective heuristic

Tuning: affect the operation of the tuning tool
  TuneCriterion: specify different tuning criteria
  TuneJobs: enables distributed tuning
  TuneOutput: tuning output level
  TuneResults: number of imroved parameter sets returned
  TuneTimeLimit: tuning time limit
  TuneTrials: number of trial runs with each parameter set

Multiple solutions: determines how the MIP search looks for solutions
  PoolGap: determines the quality of the retained solutions
  PoolSearchMode: chooses the approach used to search for solutions
  PoolSolutions: determines the number of solutions that are stored

MIP cuts: affect the generation of MIP cutting planes
  Cuts: global cut generation control
  CliqueCuts: controls clique cut generation
  CoverCuts: controls cover cut generation
  CutAggPasses: limits aggregation during cut generation
  CutPasses: limits the number of cut passes
  FlowCoverCuts: controls flow cover cut generation
  FlowPathCuts: controls flow path cut generation
  GomoryPasses: controls the number of Gomory cut passes
  GUBCoverCuts: controls GUB cover cut generation
  ImpliedCuts: controls implied bound cut generation
  InfProofCuts: controls infeasibility proof cut generation
  MIPSepCuts: controls MIP separation cut generation
  MIRCuts: controls MIR cut generation
  ModKCuts: controls mod-k cut generation
  NetworkCuts: controls network cut generation
  ProjImpliedCuts: controls projected implied bound cut generation
  StrongCGCuts: controls Strong-CG cut generation
  SubMIPCuts: controls sub-MIP cut generation
  ZeroHalfCuts: controls zero-half cut generation

Compute Server: used for compute server based optimizations
  ComputeServer: server URL to access the cluster
  CSGroup: group name
  CSIdleTimeout: job idle timeout
  CSPriority: compute server job priority
  CSQueueTimeout: queue timeout for new jobs
  CSRouter: router URL
  CSTLSInsecure: TLS security mode
  ServerPassword: cluster client password
  ServerTimeout: network timeout

Token Server: affect token server parameters
  TokenServer: adress of token server
  TSPort: token server port

Distributed algorithms: used for distributed optimization
  WorkerPassword: cluster client password
  WorkerPool: server URL to access the cluster

Cloud: parameters used for cloud-based optimization
  CloudAccessID: Instant Cloud access ID
  CloudPool: Instant Cloud pool name
  CloudSecretKey: Instant Cloud secret key

Other:
  AggFill: controls the level of presolve aggregation
  Aggregate: turns presolve aggregation on or off
  DisplayInterval: sets the frequency at which log lines are printed
  DualReductions: controls presolve dual reductions
  FeasRelaxBigM: BigM value for feasibility relaxation
  IgnoreNames: indicates whether to ignore names provided by users
  IISMethod: method used to find an IIS
  LazyConstraints: programs that use lazy constraints must set this to 1
  LogFile: sets the name of the Gurobi log file
  LogToConsole: turn logging to the console on or off
  Method: algorithm used to solve a continuous model or the root node of a
          MIP model (auto, primal simplex, dual simplex, barrier, or
          concurrent)
  NumericFocus: controls numerically conservative level
  MultiObjMethod: warm-start method to solve for subsequent objectives
  MultiObjPre: controls initial presolve level on multi-objective models
  ObjNumber: selects the objective index of multi-objectives
  OutputFlag: turn logging on or off
  PreCrush: allows presolve to crush any user cut
  PreDepRow: controls the presolve dependent row reduction
  PreDual: determines whether presolve forms the dual of the input model
  PrePasses: limits the number of presolve passes
  PreQLinearize: controls presolve Q matrix linearization
  Presolve: turns presolve on or off
  PreSOS1BigM: threshold for presolve SOS1 conversion to binary form
  PreSOS2BigM: threshold for presolve SOS2 conversion to binary form
  PreSparsify: enables the presolve sparsify reduction
  PreMIQCPForm: chooses the form for MIQCP presolved model
  Record: enables replay
  ResultFile: result file to write when optimization completes
  Seed: sets the random number seed
  StartNodeLimit: limits nodes in MIP start sub-MIP
  StartNumber: selects the MIP start index
  Threads: sets the number of threads to apply to parallel MIP
  UpdateMode: controls the way how to update a model

For further information on any of these parameters, type
paramHelp('paramname') (e.g., paramHelp("NodeLimit")).  Wildcards
are also accepted for paramHelp().
    """
    def __init__(self, env):
        ...
    def __repr__(self):
        ...
    def __dir__(self):
        ...
    def __getattr__(self, name):
        ...
    def __setattr__(self, name, value):
        ...
    def _getChangeList(self):
        ...
class ParamConstClass(object):
    """
Gurobi parameters are used to control the optimization process.  They all
have default values, but their values can be changed using the setParam()
function.  Current values can be retrieved using the Model.getParamInfo()
method.

Parameters fall into the following categories:

Termination: affect the termination of an optimize() call
  BarIterLimit: limits the number of barrier iterations performed
  BestBdStop: sets a best bound values at which optimization should stop
  BestObjStop: sets an objective value at which optimization should stop
  Cutoff: sets a target objective value
  IterationLimit: limits the number of simplex iterations performed
  NodeLimit: limits the number of MIP nodes explored
  SolutionLimit: sets a target for the number of feasible solutions found
  TimeLimit: limits the total time expended (in seconds)

Tolerances: control the allowable feasibility or optimality violations
  BarConvTol: barrier convergence tolerance
  BarQCPConvTol: barrier convergence tolerance for QCP models
  FeasibilityTol: primal feasibility tolerance
  IntFeasTol: integer feasibility tolerance
  MarkowitzTol: threshold pivoting tolerance
  MIPGap: target relative MIP optimality gap
  MIPGapAbs: target absolute MIP optimality gap
  OptimalityTol: dual feasibility tolerance
  PSDTol: QP positive semidefinite tolerance

Simplex: affect the simplex algorithms
  InfUnbdInfo: makes additional information available for infeasible or
               unbounded LP models
  NormAdjust: chooses different pricing norm variants
  ObjScale: controls objective scaling
  PerturbValue: controls the magnitude of any simplex perturbations
  Quad: turns quad precision on or off
  ScaleFlag: turns model scaling on or off
  Sifting: dual simplex sifting strategy for LP, MIP root and MIP nodes
  SiftMethod: chooses from dual, primal and barrier to solve sifting
              subproblems
  SimplexPricing: determines variable pricing strategy

Barrier: affect the barrier algorithms
  BarCorrectors: limits the number of central corrections
  BarHomogeneous: selects the barrier homogeneous algorithm
  BarOrder: determines the fill reducing ordering strategy
  Crossover: controls barrier crossover
  CrossoverBasis: controls initial crossover basis construction
  QCPDual: enables dual variable computation for continuous QCP models

MIP: affect the MIP algorithms
  BranchDir: controls the branching node selection
  ConcurrentMIP: enables concurrent MIP optimization
  ConcurrentJobs: enables distributed concurrent optimization
  DegenMoves: limit degenerate simplex moves
  Disconnected: controls the disconnected component strategy
  Heuristics: controls the amount of time spent in MIP heuristics
  ImproveStartGap: gap at which to switch MIP search strategies
  ImproveStartNodes: node count at which to switch MIP search strategies
  ImproveStartTime: time at which to switch MIP search strategies
  MinRelNodes: controls the minimum relaxation heuristic
  MIPFocus: affects the high-level MIP search strategy
  MIQCPMethod: controls whether to solve QCP node relaxation or to use OA
  NodefileDir: determines the directory used to store nodes on disk
  NodefileStart: memory nodes may use (in GB) before being written to disk
  NodeMethod: determines the algorithm used to solve MIP node relaxations
  NoRelHeuristic: determines whether the NoRel heuristic should be used
  PartitionPlace: controls when the partition heursitic runs
  PumpPasses: controls the feasibility pump heuristic
  RINS: sets the frequency of the RINS heuristic
  SolutionNumber: controls access to alternate MIP solutions
  SubMIPNodes: limits the numbers of nodes explored in a RINS sub-MIP
  Symmetry: controls access to alternate MIP solutions
  VarBranch: controls the branch variable selection strategy
  ZeroObjNodes: controls the zero objective heuristic

Tuning: affect the operation of the tuning tool
  TuneCriterion: specify different tuning criteria
  TuneJobs: enables distributed tuning
  TuneOutput: tuning output level
  TuneResults: number of imroved parameter sets returned
  TuneTimeLimit: tuning time limit
  TuneTrials: number of trial runs with each parameter set

Multiple solutions: determines how the MIP search looks for solutions
  PoolGap: determines the quality of the retained solutions
  PoolSearchMode: chooses the approach used to search for solutions
  PoolSolutions: determines the number of solutions that are stored

MIP cuts: affect the generation of MIP cutting planes
  Cuts: global cut generation control
  CliqueCuts: controls clique cut generation
  CoverCuts: controls cover cut generation
  CutAggPasses: limits aggregation during cut generation
  CutPasses: limits the number of cut passes
  FlowCoverCuts: controls flow cover cut generation
  FlowPathCuts: controls flow path cut generation
  GomoryPasses: controls the number of Gomory cut passes
  GUBCoverCuts: controls GUB cover cut generation
  ImpliedCuts: controls implied bound cut generation
  InfProofCuts: controls infeasibility proof cut generation
  MIPSepCuts: controls MIP separation cut generation
  MIRCuts: controls MIR cut generation
  ModKCuts: controls mod-k cut generation
  NetworkCuts: controls network cut generation
  ProjImpliedCuts: controls projected implied bound cut generation
  StrongCGCuts: controls Strong-CG cut generation
  SubMIPCuts: controls sub-MIP cut generation
  ZeroHalfCuts: controls zero-half cut generation

Compute Server: used for compute server based optimizations
  ComputeServer: server URL to access the cluster
  CSGroup: group name
  CSIdleTimeout: job idle timeout
  CSPriority: compute server job priority
  CSQueueTimeout: queue timeout for new jobs
  CSRouter: router URL
  CSTLSInsecure: TLS security mode
  ServerPassword: cluster client password
  ServerTimeout: network timeout

Token Server: affect token server parameters
  TokenServer: adress of token server
  TSPort: token server port

Distributed algorithms: used for distributed optimization
  WorkerPassword: cluster client password
  WorkerPool: server URL to access the cluster

Cloud: parameters used for cloud-based optimization
  CloudAccessID: Instant Cloud access ID
  CloudPool: Instant Cloud pool name
  CloudSecretKey: Instant Cloud secret key

Other:
  AggFill: controls the level of presolve aggregation
  Aggregate: turns presolve aggregation on or off
  DisplayInterval: sets the frequency at which log lines are printed
  DualReductions: controls presolve dual reductions
  FeasRelaxBigM: BigM value for feasibility relaxation
  IgnoreNames: indicates whether to ignore names provided by users
  IISMethod: method used to find an IIS
  LazyConstraints: programs that use lazy constraints must set this to 1
  LogFile: sets the name of the Gurobi log file
  LogToConsole: turn logging to the console on or off
  Method: algorithm used to solve a continuous model or the root node of a
          MIP model (auto, primal simplex, dual simplex, barrier, or
          concurrent)
  NumericFocus: controls numerically conservative level
  MultiObjMethod: warm-start method to solve for subsequent objectives
  MultiObjPre: controls initial presolve level on multi-objective models
  ObjNumber: selects the objective index of multi-objectives
  OutputFlag: turn logging on or off
  PreCrush: allows presolve to crush any user cut
  PreDepRow: controls the presolve dependent row reduction
  PreDual: determines whether presolve forms the dual of the input model
  PrePasses: limits the number of presolve passes
  PreQLinearize: controls presolve Q matrix linearization
  Presolve: turns presolve on or off
  PreSOS1BigM: threshold for presolve SOS1 conversion to binary form
  PreSOS2BigM: threshold for presolve SOS2 conversion to binary form
  PreSparsify: enables the presolve sparsify reduction
  PreMIQCPForm: chooses the form for MIQCP presolved model
  Record: enables replay
  ResultFile: result file to write when optimization completes
  Seed: sets the random number seed
  StartNodeLimit: limits nodes in MIP start sub-MIP
  StartNumber: selects the MIP start index
  Threads: sets the number of threads to apply to parallel MIP
  UpdateMode: controls the way how to update a model

Parameters can be referred to using the Param class (e.g.
"setParam(GRB.param.threads, 1)"), or by using the name as a string
(e.g., "setParam('threads', 1)).  You can use the '*' and '?' wildcards
when inputting parameter names, and text case is ignored
(so "setParam('thr*', 1)" would also work).

For further information on any of these parameters, type
paramHelp('paramname') (e.g., paramHelp("NodeLimit")).  Wildcards
are also accepted for paramHelp().
    """
    def __setattr__(self, name, value):
        ...
    BarIterLimit: str = ...
    Cutoff: str = ...
    IterationLimit: str = ...
    NodeLimit: str = ...
    SolutionLimit: str = ...
    TimeLimit: str = ...
    BestObjStop: str = ...
    BestBdStop: str = ...
    BarConvTol: str = ...
    BarQCPConvTol: str = ...
    FeasibilityTol: str = ...
    IntFeasTol: str = ...
    MarkowitzTol: str = ...
    MIPGap: str = ...
    MIPGapAbs: str = ...
    OptimalityTol: str = ...
    PSDTol: str = ...
    InfUnbdInfo: str = ...
    NormAdjust: str = ...
    ObjScale: str = ...
    PerturbValue: str = ...
    Quad: str = ...
    ScaleFlag: str = ...
    Sifting: str = ...
    SiftMethod: str = ...
    SimplexPricing: str = ...
    BarCorrectors: str = ...
    BarHomogeneous: str = ...
    BarOrder: str = ...
    Crossover: str = ...
    CrossoverBasis: str = ...
    QCPDual: str = ...
    BranchDir: str = ...
    DegenMoves: str = ...
    ConcurrentJobs: str = ...
    ConcurrentMIP: str = ...
    Disconnected: str = ...
    DistributedMIPJobs: str = ...
    Heuristics: str = ...
    ImproveStartGap: str = ...
    ImproveStartNodes: str = ...
    ImproveStartTime: str = ...
    MinRelNodes: str = ...
    MIPFocus: str = ...
    MIQCPMethod: str = ...
    NodefileDir: str = ...
    NodefileStart: str = ...
    NodeMethod: str = ...
    NoRelHeuristic: str = ...
    PartitionPlace: str = ...
    PumpPasses: str = ...
    RINS: str = ...
    SolutionNumber: str = ...
    SubMIPNodes: str = ...
    Symmetry: str = ...
    VarBranch: str = ...
    ZeroObjNodes: str = ...
    TuneCriterion: str = ...
    TuneJobs: str = ...
    TuneOutput: str = ...
    TuneResults: str = ...
    TuneTimeLimit: str = ...
    TuneTrials: str = ...
    PoolSearchMode: str = ...
    PoolSolutions: str = ...
    PoolGap: str = ...
    Cuts: str = ...
    CliqueCuts: str = ...
    CoverCuts: str = ...
    FlowCoverCuts: str = ...
    FlowPathCuts: str = ...
    GUBCoverCuts: str = ...
    ImpliedCuts: str = ...
    InfProofCuts: str = ...
    MIPSepCuts: str = ...
    MIRCuts: str = ...
    ModKCuts: str = ...
    NetworkCuts: str = ...
    ProjImpliedCuts: str = ...
    StrongCGCuts: str = ...
    SubMIPCuts: str = ...
    ZeroHalfCuts: str = ...
    CutAggPasses: str = ...
    CutPasses: str = ...
    GomoryPasses: str = ...
    WorkerPassword: str = ...
    WorkerPool: str = ...
    ComputeServer: str = ...
    ServerPassword: str = ...
    ServerTimeout: str = ...
    CSRouter: str = ...
    CSGroup: str = ...
    CSPriority: str = ...
    CSQueueTimeout: str = ...
    CSTLSInsecure: str = ...
    CSIdleTimeout: str = ...
    TokenServer: str = ...
    TSPort: str = ...
    CloudAccessID: str = ...
    CloudSecretKey: str = ...
    CloudPool: str = ...
    CloudHost: str = ...
    AggFill: str = ...
    Aggregate: str = ...
    DisplayInterval: str = ...
    DualReductions: str = ...
    FeasRelaxBigM: str = ...
    IISMethod: str = ...
    LazyConstraints: str = ...
    LogFile: str = ...
    LogToConsole: str = ...
    Method: str = ...
    NumericFocus: str = ...
    MultiObjMethod: str = ...
    MultiObjPre: str = ...
    IgnoreNames: str = ...
    ObjNumber: str = ...
    OutputFlag: str = ...
    PreCrush: str = ...
    PreDepRow: str = ...
    PreDual: str = ...
    PrePasses: str = ...
    PreQLinearize: str = ...
    Presolve: str = ...
    PreSOS1BigM: str = ...
    PreSOS2BigM: str = ...
    PreSparsify: str = ...
    PreMIQCPForm: str = ...
    Record: str = ...
    ResultFile: str = ...
    Seed: str = ...
    StartNodeLimit: str = ...
    StartNumber: str = ...
    Threads: str = ...
    UpdateMode: str = ...
class GurobiError(Exception):
    """
Gurobi exception class
    """
    def _get_message(self):
        ...
    def _set_message(self, message):
        ...
    message: property = ...
    def __init__(self, errno, argument):
        ...
    def __str__(self):
        ...
class CallbackClass(object):
    """
Callbacks are user methods that are called by the Gurobi solver
during the optimization.  To use a callback, define a method
that takes two integer arguments (model and where), and pass it
as the argument to Model.optimize.  Once optimization begins,
your method will be called with one of the following 'where' values:

Possible 'where' values (e.g., where == GRB.Callback.MIP) are:

  POLLING:  Regular polling callback - no user queries allowed
  PRESOLVE: In presolve
  SIMPLEX:  In simplex
  BARRIER:  In barrier
  MIP:      In MIP
  MIPSOL:   New MIP incumbent available
  MIPNODE:  MIP node information available
  MULTIOBJ: In multi-objective optimization
  MESSAGE:  Optimizer output a message

Your method can call Model.cbGet() to obtain detailed information
on the progress of the optimization.  Allowed values depend
on 'where'.  The prefix of the 'what' name indicate which
ones are allowed for each 'where' (so 'PRE_COLDEL' can only
be called when where == SIMPLEX).

Allowed 'what' values (e.g., cbGet(GRB.Callback.MIP_OBJBND) are:

  RUNTIME: Elapsed solver runtime
  PRE_COLDEL: Deleted column count
  PRE_ROWDEL: Deleted row count
  PRE_SENCHG: Changed constraint sense count
  PRE_BNDCHG: Bound change count
  SPX_ITRCNT: Iteration count
  SPX_OBJVAL: Primal objective value
  SPX_PRIMINF: Primal infeasibility
  SPX_DUALINF: Dual infeasibility
  SPX_ISPERT: Has model been perturbed?
  BARRIER_ITRCNT: Barrier iteration count
  BARRIER_PRIMOBJ: Barrier iterate primal objective
  BARRIER_DUALOBJ: Barrier iterate dual objective
  BARRIER_PRIMINF: Barrier iterate primal infeasibility
  BARRIER_DUALINF: Barrier iterate dual infeasibility
  BARRIER_COMPL: Barrier iterate complementarity violation
  MIP_OBJBST: Best known objective bound
  MIP_OBJBND: Best known feasible objective
  MIP_NODCNT: Nodes explored so far
  MIP_SOLCNT: Solutions found so far
  MIP_CUTCNT: Cuts added to the model so far
  MIP_NODLFT: Unexplored nodes
  MIP_ITRCNT: Simplex iterations performed so far
  MIPSOL_SOL: Feasible solution (a vector)
  MIPSOL_OBJ: Objective value for feasible solution
  MIPSOL_OBJBST: Best known objective bound
  MIPSOL_OBJBND: Best known feasible objective
  MIPSOL_NODCNT: Node count for feasible solution
  MIPSOL_SOLCNT: Solutions found so far
  MIPNODE_STATUS: Optimization status of node relaxation
  MIPNODE_REL: Node relaxation solution or ray if unbounded
  MIPNODE_OBJBST: Best known objective bound
  MIPNODE_OBJBND: Best known feasible objective
  MIPNODE_NODCNT: Nodes explored so far
  MIPNODE_SOLCNT: Solutions found so far
  MIPNODE_SBRVAR: Node branching variable
  MULTIOBJ_OBJCNT: Objective count optimized so far
  MULTIOBJ_SOLCNT: Solutions found so far
  MULTIOBJ_SOL: Feasible solution (a vector)
  MSG_STRING: Output message

Your callback method can call other methods on the model object:
  cbCut(), cbGet(), cbGetNodeRel(), cbGetSolution(), cbSetSolution()
    """
    _where: int = ...
    _n: int = ...
    POLLING: int = ...
    PRESOLVE: int = ...
    SIMPLEX: int = ...
    MIP: int = ...
    MIPSOL: int = ...
    MIPNODE: int = ...
    MESSAGE: int = ...
    BARRIER: int = ...
    MULTIOBJ: int = ...
    PRE_COLDEL: int = ...
    PRE_ROWDEL: int = ...
    PRE_SENCHG: int = ...
    PRE_BNDCHG: int = ...
    PRE_COECHG: int = ...
    SPX_ITRCNT: int = ...
    SPX_OBJVAL: int = ...
    SPX_PRIMINF: int = ...
    SPX_DUALINF: int = ...
    SPX_ISPERT: int = ...
    BARRIER_ITRCNT: int = ...
    BARRIER_PRIMOBJ: int = ...
    BARRIER_DUALOBJ: int = ...
    BARRIER_PRIMINF: int = ...
    BARRIER_DUALINF: int = ...
    BARRIER_COMPL: int = ...
    MIP_OBJBST: int = ...
    MIP_OBJBND: int = ...
    MIP_NODCNT: int = ...
    MIP_SOLCNT: int = ...
    MIP_CUTCNT: int = ...
    MIP_NODLFT: int = ...
    MIP_ITRCNT: int = ...
    MIPSOL_SOL: int = ...
    MIPSOL_OBJ: int = ...
    MIPSOL_OBJBST: int = ...
    MIPSOL_OBJBND: int = ...
    MIPSOL_NODCNT: int = ...
    MIPSOL_SOLCNT: int = ...
    MIPNODE_STATUS: int = ...
    MIPNODE_REL: int = ...
    MIPNODE_OBJBST: int = ...
    MIPNODE_OBJBND: int = ...
    MIPNODE_NODCNT: int = ...
    MIPNODE_SOLCNT: int = ...
    MIPNODE_BRVAR: int = ...
    MSG_STRING: int = ...
    RUNTIME: int = ...
    MULTIOBJ_OBJCNT: int = ...
    MULTIOBJ_SOLCNT: int = ...
    MULTIOBJ_SOL: int = ...
    def __init__(self, model, function):
        ...
    def _solnow(self):
        ...
    def callback(self, model, cbdata, where):
        ...
class ErrorConstClass(object):
    """
Gurobi error codes (e.g., exception.errno == GRB.ERROR_OUT_OF_MEMORY):

  OUT_OF_MEMORY: Exhausted available memory
  NULL_ARGUMENT: NULL argument value
  INVALID_ARGUMENT: Invalid argument value
  UNKNOWN_ATTRIBUTE: Unknown attribute name
  DATA_NOT_AVAILABLE: Requested data not available
  INDEX_OUT_OF_RANGE: Constr/var index out of range
  UNKNOWN_PARAMETER: Unknown parameter name
  VALUE_OUT_OF_RANGE: Parameter value outside of valid range
  NO_LICENSE: No Gurobi license found
  SIZE_LIMIT_EXCEEDED: Exceeded licensed model size limit
  CALLBACK: Error in callback
  FILE_READ: Error reading file
  FILE_WRITE: Error writing file
  NUMERIC: Numeric error encountered
  IIS_NOT_INFEASIBLE: Can't compute an IIS on a feasible model
  NOT_FOR_MIP: Method not valid for MIP models
  OPTIMIZATION_IN_PROGRESS: Must stop optimization to query results
  DUPLICATES: Duplicate entries in list
  NODEFILE: Problem reading or writing node file
  Q_NOT_PSD: Q matrix isn't Positive Semi-Definite
  QCP_EQUALITY_CONSTRAINT: Quadratic constraints must be inequalities
  NETWORK: Network error
  JOB_REJECTED: Job rejected by Compute Server
  NOT_SUPPORTED: Requested operation is not supported
  EXCEED_2B_NONZEROS: Result too large for query routine
  INVALID_PIECEWISE_OBJ: Problem with specified piecewise-linear objective
  JOB_REJECTED: Job rejected by Compute Server
  NOT_SUPPORTED: Operation is not supported
  NOT_IN_MODEL: Variable/constraint not in model
  FAILED_TO_CREATE_MODEL: Failed to create the requested model
  CLOUD: Instant Cloud error
  MODEL_MODIFICATION: An error occurred during model modification or update
  CSWORKER: An error occurred on the Compute Server worker
  TUNE_MODEL_TYPES: Tried multi-model tuning on models of different types
  INTERNAL: Internal Gurobi error
    """
    OUT_OF_MEMORY: int = ...
    NULL_ARGUMENT: int = ...
    INVALID_ARGUMENT: int = ...
    UNKNOWN_ATTRIBUTE: int = ...
    DATA_NOT_AVAILABLE: int = ...
    INDEX_OUT_OF_RANGE: int = ...
    UNKNOWN_PARAMETER: int = ...
    VALUE_OUT_OF_RANGE: int = ...
    NO_LICENSE: int = ...
    SIZE_LIMIT_EXCEEDED: int = ...
    CALLBACK: int = ...
    FILE_READ: int = ...
    FILE_WRITE: int = ...
    NUMERIC: int = ...
    IIS_NOT_INFEASIBLE: int = ...
    NOT_FOR_MIP: int = ...
    OPTIMIZATION_IN_PROGRESS: int = ...
    DUPLICATES: int = ...
    NODEFILE: int = ...
    Q_NOT_PSD: int = ...
    QCP_EQUALITY_CONSTRAINT: int = ...
    NETWORK: int = ...
    JOB_REJECTED: int = ...
    NOT_SUPPORTED: int = ...
    EXCEED_2B_NONZEROS: int = ...
    INVALID_PIECEWISE_OBJ: int = ...
    UPDATEMODE_CHANGE: int = ...
    CLOUD: int = ...
    MODEL_MODIFICATION: int = ...
    CSWORKER: int = ...
    TUNE_MODEL_TYPES: int = ...
    NOT_IN_MODEL: int = ...
    FAILED_TO_CREATE_MODEL: int = ...
    INTERNAL: int = ...
class StatusConstClass(object):
    """
Gurobi optimization status codes (e.g., model.status == GRB.OPTIMAL):

  LOADED: Model loaded, but no solution information available
  OPTIMAL: Solve to optimality (subject to tolerances)
  INFEASIBLE: Model is infeasible
  INF_OR_UNBD: Model is either infeasible or unbounded
  UNBOUNDED: Model is unbounded
  CUTOFF: Objective is worse than specified cutoff value
  ITERATION_LIMIT: Optimization terminated due to iteration limit
  NODE_LIMIT: Optimization terminated due to node limit
  TIME_LIMIT: Optimization terminated due to time limit
  SOLUTION_LIMIT: Optimization terminated due to solution limit
  INTERRUPTED: User interrupted optimization
  NUMERIC: Optimization terminated due to numerical issues
  SUBOPTIMAL: Optimization terminated with a sub-optimal solution
  INPROGRESS: Optimization currently in progress
  USER_OBJ_LIMIT: Achieved user objective limit
    """
    def __setattr__(self, name, value):
        ...
    LOADED: int = ...
    OPTIMAL: int = ...
    INFEASIBLE: int = ...
    INF_OR_UNBD: int = ...
    UNBOUNDED: int = ...
    CUTOFF: int = ...
    ITERATION_LIMIT: int = ...
    NODE_LIMIT: int = ...
    TIME_LIMIT: int = ...
    SOLUTION_LIMIT: int = ...
    INTERRUPTED: int = ...
    NUMERIC: int = ...
    SUBOPTIMAL: int = ...
    INPROGRESS: int = ...
    USER_OBJ_LIMIT: int = ...
class tupledict(dict):
    """
Custom Gurobi class: tupledict is a subclass of dict where
the keys are a tuplelist.
    """
    def __init__(self, *args, **kwargs):
        ...
    def clean(self):
        ...
    def setord(self, ord):
        ...
    def keys(self):
        ...
    def iteritems(self, *vals):
        ...
    def iterkeys(self):
        ...
    def itervalues(self):
        ...
    def values(self):
        ...
    def items(self):
        ...
    def __iter__(self):
        ...
    def subset(self, *vals):
        ...
    def select(self, *vals):
        ...
    def sum(self, *vals):
        ...
    def prod(self, d, *vals):
        ...
    def __delitem__(self, *args, **kwargs):
        ...
    def __setitem__(self, *args, **kwargs):
        ...
    def clear(self, *args, **kwargs):
        ...
    def pop(self, *args):
        ...
    def popitem(self, *args):
        ...
    def update(self, *args):
        ...
class izip(object):
    """
zip(iter1 [,iter2 [...]]) --> zip object

Return a zip object whose .__next__() method returns a tuple where
the i-th element comes from the i-th iterable argument.  The .__next__()
method continues until the shortest iterable in the argument sequence
is exhausted and then it raises StopIteration.
    """
    def __getattribute__(self, name):
        """
Return getattr(self, name).
        """
        ...
    def __iter__(self):
        """
Implement iter(self).
        """
        ...
    def __next__(self):
        """
Implement next(self).
        """
        ...
    def __new__(*args, **kwargs):
        """
Create and return a new object.  See help(type) for accurate signature.
        """
        ...
    def __reduce__(self, *args, **kwargs) -> Any:
        """
Return state information for pickling.
        """
        ...
class tuplelist(list):
    """
Custom Gurobi class: tuplelist is a subclass of list that is
designed to work with lists of tuples.  Using the select()
method, this class allows you to efficiently select sub-lists of
tuples by matching specific values in specific fields of the
member tuples.

For example:
  > l = tuplelist([(1, 2), (1, 3), (2, 3), (2, 4)])
  > print l.select('*', '*')
  [(1, 2), (1, 3), (2, 3), (2, 4)]
  > print l.select('*', 3)
  [(1, 3), (2, 3)]
  > print l.select(1, '*')
  [(1, 2), (1, 3)]
    """
    @staticmethod
    def _tuplelist__repl(*args, **kwargs) -> Any:
        ...
    def __init__(self, data=[], wild='*'):
        ...
    def prev(self, v):
        ...
    def prevc(self, v):
        ...
    def next(self, v):
        ...
    def nextc(self, v):
        ...
    def _tuplelist__scalardelcheck(self):
        ...
    def _tuplelist__scalaraddcheck(self, x):
        ...
    def __repr__(self):
        ...
    def clean(self):
        """
ROUTINE:
  clean()

PURPOSE:
  The tuplelist class achieves it efficiency by building
  indices.  These indices are stored inside tuplelist
  objects, and they consume memory.  Call clean()
  if you wish to reclaim this memory.

ARGUMENTS:
  None

RETURN VALUE:
  None.

EXAMPLE:
  l.clean()
        """
        ...
    def select(self, *vals):
        """
ROUTINE:
  select(value1, value2, ...)

PURPOSE:
  Selects a sub-list from a tuplelist.  All tuples that
  match the specified arguments in the corresponding fields
  are returned.  You can pass the string '*' (with the quotes)
  to indicate that any value is acceptable in the corresponding
  field.

ARGUMENTS:
  value1: Value to match with first tuple member.
  value2: Value to match with second tuple member.
  ...

RETURN VALUE:
  The matching sub-list.

EXAMPLE:
  m = l.select('*', 1, '*', 'a')
        """
        ...
    def __contains__(self, val):
        """
ROUTINE:
  __contains__(val)

PURPOSE:
  Determines if the specified value is contained in the tuplelist.
  This is faster than the parent method when calling "in" within
  a loop.

ARGUMENTS:
  val: Value to match.

RETURN VALUE:
  True if the values are in the list.

EXAMPLE:
  if (1,2,3) in l
        """
        ...
    def _tuplelist__makeindex(self, getkey):
        ...
    def append(self, x):
        ...
    def extend(self, L):
        ...
    def insert(self, i, x):
        ...
    def pop(self, i=-1):
        ...
    def remove(self, x):
        ...
    def __delitem__(self, i):
        ...
    def __delslice__(self, i, j):
        ...
    def __add__(self, other):
        ...
    def __iadd__(self, other):
        ...
    def __getslice__(self, b, c):
        ...
class GRB(object):
    """
Gurobi constants.  Constants defined in this class are as follows:

  Basis status (e.g., var.vBasis == GRB.BASIC):

    BASIC: Variable is basic
    NONBASIC_LOWER: Variable is non-basic at lower bound
    NONBASIC_UPPER: Variable is non-basic at upper bound
    SUPERBASIC: Variable is superbasic

  Constraint sense (e.g., constr.sense = GRB.LESS_EQUAL):

    LESS_EQUAL, GREATER_EQUAL, EQUAL

  Variable types (e.g., var.vType = GRB.INTEGER):

    CONTINUOUS, BINARY, INTEGER, SEMICONT, SEMIINT

  SOS types:

    SOS_TYPE1, SOS_TYPE2

  General constraint types:

    GENCONSTR_MAX, GENCONSTR_MIN, GENCONSTR_ABS, GENCONSTR_AND, GENCONSTR_OR, GENCONSTR_INDICATOR

The GRB class also includes definitions for attributes (GRB.attr),
errors (GRB.error), parameters (GRB.param), status codes (GRB.status),
and callbacks (GRB.callback).  You can ask for help on any of these
(e.g., "help(GRB.attr)").
    """
    attr: AttrConstClass = ...
    Attr: AttrConstClass = ...
    param: ParamConstClass = ...
    Param: ParamConstClass = ...
    callback: CallbackClass = ...
    Callback: CallbackClass = ...
    error: ErrorConstClass = ...
    Error: ErrorConstClass = ...
    status: StatusConstClass = ...
    Status: StatusConstClass = ...
    LOADED: int = ...
    OPTIMAL: int = ...
    INFEASIBLE: int = ...
    INF_OR_UNBD: int = ...
    UNBOUNDED: int = ...
    CUTOFF: int = ...
    ITERATION_LIMIT: int = ...
    NODE_LIMIT: int = ...
    TIME_LIMIT: int = ...
    SOLUTION_LIMIT: int = ...
    INTERRUPTED: int = ...
    NUMERIC: int = ...
    SUBOPTIMAL: int = ...
    INPROGRESS: int = ...
    USER_OBJ_LIMIT: int = ...
    VERSION_MAJOR: int = ...
    VERSION_MINOR: int = ...
    VERSION_TECHNICAL: int = ...
    BASIC: int = ...
    NONBASIC_LOWER: int = ...
    NONBASIC_UPPER: int = ...
    SUPERBASIC: int = ...
    LESS_EQUAL: str = ...
    GREATER_EQUAL: str = ...
    EQUAL: str = ...
    CONTINUOUS: str = ...
    BINARY: str = ...
    INTEGER: str = ...
    SEMICONT: str = ...
    SEMIINT: str = ...
    MINIMIZE: int = ...
    MAXIMIZE: int = ...
    SOS_TYPE1: int = ...
    SOS_TYPE2: int = ...
    GENCONSTR_MAX: int = ...
    GENCONSTR_MIN: int = ...
    GENCONSTR_ABS: int = ...
    GENCONSTR_AND: int = ...
    GENCONSTR_OR: int = ...
    GENCONSTR_INDICATOR: int = ...
    INFINITY: float = ...
    UNDEFINED: float = ...
    DEFAULT_CS_PORT: int = ...
    ERROR_OUT_OF_MEMORY: int = ...
    ERROR_NULL_ARGUMENT: int = ...
    ERROR_INVALID_ARGUMENT: int = ...
    ERROR_UNKNOWN_ATTRIBUTE: int = ...
    ERROR_DATA_NOT_AVAILABLE: int = ...
    ERROR_INDEX_OUT_OF_RANGE: int = ...
    ERROR_UNKNOWN_PARAMETER: int = ...
    ERROR_VALUE_OUT_OF_RANGE: int = ...
    ERROR_NO_LICENSE: int = ...
    ERROR_SIZE_LIMIT_EXCEEDED: int = ...
    ERROR_CALLBACK: int = ...
    ERROR_FILE_READ: int = ...
    ERROR_FILE_WRITE: int = ...
    ERROR_NUMERIC: int = ...
    ERROR_IIS_NOT_INFEASIBLE: int = ...
    ERROR_NOT_FOR_MIP: int = ...
    ERROR_OPTIMIZATION_IN_PROGRESS: int = ...
    ERROR_DUPLICATES: int = ...
    ERROR_NODEFILE: int = ...
    ERROR_Q_NOT_PSD: int = ...
    ERROR_QCP_EQUALITY_CONSTRAINT: int = ...
    ERROR_NETWORK: int = ...
    ERROR_JOB_REJECTED: int = ...
    ERROR_NOT_SUPPORTED: int = ...
    ERROR_EXCEED_2B_NONZEROS: int = ...
    ERROR_INVALID_PIECEWISE_OBJ: int = ...
    ERROR_UPDATEMODE_CHANGE: int = ...
    ERROR_CLOUD: int = ...
    ERROR_MODEL_MODIFICATION: int = ...
    ERROR_CSWORKER: int = ...
    ERROR_TUNE_MODEL_TYPES: int = ...
    ERROR_NOT_IN_MODEL: int = ...
    ERROR_FAILED_TO_CREATE_MODEL: int = ...
    ERROR_INTERNAL: int = ...
class Iterable(object):
    __slots__: tuple = ...
    def __iter__(self):
        ...
    @classmethod
    def __subclasshook__(cls, *args, **kwargs) -> Any:
        ...
    __abstractmethods__: frozenset = ...
class gurobi(object):
    _exiting: bool = ...
    @classmethod
    def _getdefaultenv(cls, *args, **kwargs) -> Any:
        ...
    @classmethod
    def _getmodels(cls, *args, **kwargs) -> Any:
        ...
    def _cleanup():
        ...
    @classmethod
    def version(cls, *args, **kwargs) -> Any:
        ...
    @classmethod
    def platform(cls, *args, **kwargs) -> Any:
        ...
    @classmethod
    def read(cls, *args, **kwargs) -> Any:
        ...
    @classmethod
    def models(cls, *args, **kwargs) -> Any:
        ...
    @classmethod
    def disposeDefaultEnv(cls, *args, **kwargs) -> Any:
        ...
def help(*args, **kwargs) -> Any:
    ...
def paramHelp(paramname):
    """
ROUTINE:
  paramHelp(paramname)

PURPOSE:
  Obtain help on a Gurobi parameter.

ARGUMENTS:
  paramname (string): The name of the parameter for which help is desired.

EXAMPLE:
  paramHelp()
  paramHelp("NodeLimit")
  paramHelp("Heu*")

NOTES:
  The parameter name may contain '*' and '?' wildcards.
    """
    ...
def system(command):
    """
ROUTINE:
  system(command)

PURPOSE:
  Issue a system shell command.

ARGUMENTS:
  command (string): The command to pass to the system shell.

EXAMPLE:
  system("ls")
  system("rm junk")
    """
    ...
def read(filename):
    """
ROUTINE:
  read(filename)

PURPOSE:
  Read an optimization model from a file.

ARGUMENTS:
  filename (string): Path to a valid MPS or LP format input file.

RETURN VALUE:
  A Model object.

EXAMPLE:
  m = read("examples/model.mps.gz")
  m.optimize()

NOTES:
  The file type is determined from the file name suffix, which must be
  one of .lp, .mps, .rew, or .rlp.  This routine can read files that have
  been compressed with either gzip or bzip2, so additional suffixes of
  .gz or .bz2 are accepted.

  The file name may contain the '*' and '?' wildcard characters.  If
  more than one file matches, this routine will read the first match.
    """
    ...
def models():
    """
ROUTINE:
  models()

PURPOSE:
  Provide a list of currently loaded models.

ARGUMENTS:
  None.

EXAMPLE:
  models()
    """
    ...
def disposeDefaultEnv():
    """
ROUTINE:
  disposeDefaultEnv()

PURPOSE:
  Release default Gurobi environment.

ARGUMENTS:
  None.

EXAMPLE:
  disposeDefaultEnv()
    """
    ...
def quicksum(list):
    """
ROUTINE:
  quicksum(list)

PURPOSE:
  A quicker version of the Python built-in 'sum' function for building
  Gurobi expressions.

ARGUMENTS:
  list: A list of terms.

RETURN VALUE:
  An expression that represents the sum of the input arguments.

EXAMPLE:
  expr = quicksum([x, y, z])
  expr = quicksum([1.0, 2*y, 3*z*z])
    """
    ...
def setParam(paramname, newvalue):
    """
ROUTINE:
  setParam(paramname, newvalue)

PURPOSE:
  Set a parameter to a new value.

ARGUMENTS:
  paramname (string): The name of the parameter.
  newvalue: The desired new value.  The type of the value should be
            compatible with the parameter type (e.g., an integer parameter
            takes an integer value).  One important exception: the string
            "default" will revert the specified parameter to its
            default value.

EXAMPLE:
  setParam("NodeLimit", 100)
  setParam("TimeLimit", "default")

NOTES:
  The parameter name may contain the '*' and '?' wildcards.

  To change a parameter setting for a single model, use Model.setParam().

  paramHelp() provides additional information on the available parameters.
    """
    ...
def resetParams():
    """
ROUTINE:
  resetParams()

PURPOSE:
  Reset all parameters to their default values.

ARGUMENTS:
  None.

EXAMPLE:
  resetParams()
    """
    ...
def readParams(filename):
    """
ROUTINE:
  readParams(filename)

PURPOSE:
  Read a set of parameter settings from a file.

ARGUMENTS:
  filename (string): Path to a file containing a list of parameter settings.

EXAMPLE:
  readParams("gurobi.prm")

NOTES:
  The parameter file should contain name-value pairs, each on its own line.
  A hash symbol at the beginning of a line indicates that the line should be
  ignored.  Here is an example of a valid parameter file:

    # List of changed parameters
    TimeLimit      100
    IterationLimit 1000
    """
    ...
def writeParams(filename):
    """
ROUTINE:
  writeParams(filename)

PURPOSE:
  Write non-default parameter settings to a file.

ARGUMENTS:
  filename (string): The name of the file to which non-default parameter
                     settings should be written.

EXAMPLE:
  writeParams("changed.prm")

NOTES:
  Upon completion, the specified file will contain a set of name-value
  pairs, one per line, that indicates the set of parameters with
  non-default values.
    """
    ...