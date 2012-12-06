from setuptools import setup

MODULE = 'mymodule'

# This exec adds to this module's global namespace the '__version__' variable
# set to mymodule.__version__, without actually loading the module

exec("c=__import__('compiler');a='__version__';l=[];g=lambda:[n.expr.value for"
        " n in l for o in n.nodes if o.name==a].pop();c.walk(c.parseFile('%s/_"
        "_init__.py'),type('v',(object,),{'visitAssign':lambda s,n:l.append(n)"
        "})());exec(a+'=g()');" % MODULE)

setup(
        name='mymodule',
        version=__version__,
        py_modules=['mymodule']
        )


