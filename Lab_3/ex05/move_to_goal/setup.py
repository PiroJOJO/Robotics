from setuptools import find_packages, setup

package_name = 'move_to_goal'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sofia',
    maintainer_email='s.volodina@g.nsu.ru',
    description='Lab_3_Task_5',
    license='License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['move_to_goal = move_to_goal.move_to_goal:main',
        ],
    },
)
