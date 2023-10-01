from setuptools import find_packages, setup

package_name = 'py_actions'

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
    description='Lab_2_Task_2',
    license='License 1.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['server = py_actions.action_server:main',
        'client = py_actions.action_client:main',
        ],
    },
)
