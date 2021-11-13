from setuptools import setup

def readme_file_contents():
    with open('README.rst') as readme_file:
        data = readme_file.read()
    return data

setup(
    name='PotX',
    version='1.0.0',
    description='TCP honeypot',
    long_description=readme_file_contents(),
    author='Dhruvil',
    author_email='dhruvilpatel2372002@gmail.com',
    license='MIT',
    packages=['potx'],
    zip_safe=False,
    install_requires=[]
)