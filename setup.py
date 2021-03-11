from setuptools import setup

setup(
    name="ijq",
    version="0.1.0",
    py_modules=["ijq"],
    author="Aleksei Piskunov",
    author_email="piskunov.alesha@gmail.com",
    description="display json beautifully among text",
    install_requires=["pygments"],
    entry_points=dict(console_scripts=['ijq = ijq:main']),
)
