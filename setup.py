from setuptools import setup, find_packages

from pathlib import Path
current_dir = Path(__file__).parent
long_description = (current_dir / "README.md").read_text()
setup(
    name='galsen_game_of_life',
    version='0.1',
    packages=find_packages(),
    license='GPLv3',
    description='Game of life version galsen',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='abdoufermat',
    keywords=['game of life', 'game', 'python', 'algorithm'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment :: Simulation',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.8',
    ],
    url="https://github.com/abdoufermat5/conway-game-of-life"
)
