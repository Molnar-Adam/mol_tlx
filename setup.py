from setuptools import setup
import os
from glob import glob

package_name = 'mol_tlx'

setup(
    name=package_name,
    version='0.0.0',
    packages=['ros2_py_mol_tlx'],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Molnar-Adam',
    maintainer_email='molnar.a2003@gmail.com',
    description='Your package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'car_draw = ros2_py_mol_tlx.car_draw:main',
            'car_publisher = ros2_py_mol_tlx.car_publisher:main',
        ],
    },
    
)
