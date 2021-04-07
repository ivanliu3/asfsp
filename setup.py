from setuptools import setup

setup(name = "asfsp",
      version = '0.1',
      description = 'A package for claculating popgen statistics based on SFS and operating on SFS.',
      author = 'Xiaodong Liu',
      author_email = 'liuxiaodong.uu@gmail.com',
      license = 'MIT',
      packages = ['sfs'],
      python_requires = '>3.0.1', 
      install_requires = ['numpy','pandas','matplotlib','seaborn'])
