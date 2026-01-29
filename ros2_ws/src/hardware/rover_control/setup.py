import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'rover_control'

setup(
    name=package_name,
    version='0.0.0',
    
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', '*.*'))),
        (os.path.join('share', package_name, 'resource'), glob(os.path.join('resource', '*.*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='humubuntu',
    maintainer_email='dragonoidhor@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rover_control = rover_control.rover_control:main',
            'rover_driver=rover_control.rover_driver:main'
        ],
    },
)