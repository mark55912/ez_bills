from setuptools import setup

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(name='bills',
      version='1.0',
      description='Setup a bills list, DEB package',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Maclinunix',
      author_email='maxlinunix@gmail.com',
      license='MIT',
      packages=['bills'],
      package_dir={'bills': 'bills/'},
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Environmanet :: Console",
          "Operating System :: POSIX :: Linux"],
      entry_points={'console_scripts': ['bills=bills.bills:main']},
      data_files=[('share/applications/', ['bills.desktop'])],
      keywords="bills list create",
      python_requires=">=3.10")
