from setuptools import setup
import os
from glob import glob

package_name = 'rover_sequence'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # instala todo lo que esté en launch/ con extensión .py
        (os.path.join('share', package_name, 'launch'),
         glob(os.path.join('launch', '*.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yehousa',
    maintainer_email='x@x.com',
    description='Nodo de secuencia para el rover',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rover_sequence = rover_sequence.rover_sequence:main',
        ],
    },
)
