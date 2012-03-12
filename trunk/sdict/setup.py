from distutils.core import setup,Extension
tst_module = Extension('_tst',sources=['tst_wrap.c','tst.c'])

setup(name='tst',
	version='0.1',
	author='Sun, Junyi',
	description='Ternary Search Tree Module',
	ext_modules=[tst_module],
	py_modules=['tst'],
)

