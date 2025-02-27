from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'mol_tlx'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Molnar-Adam',
    maintainer_email='molnar.a2003@gmail.com',
    description='Molnar-Adam: Package description',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'control_vehicle = mol_tlx.control_vehicle:main',
        ],
    },
)
