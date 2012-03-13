from distutils.core import setup,Extension
tst_module = Extension('sdict/_tst',sources=['sdict/tst_wrap.c','sdict/tst.c'])

setup(name='sdict',
	version='0.1',
	author='Sun, Junyi',
	description='Sorted Dictionary Implementation',
	ext_modules=[tst_module],
	packages=['sdict'],
	package_dir={'sdict':'sdict'}	
)

