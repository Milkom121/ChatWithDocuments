from setuptools import setup, find_packages

setup(
    name="ChatWithDocuments",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Aggiungi qui le dipendenze necessarie, ad esempio:
        # 'langchain_community',
        # 'fitz',
        # 'python-dotenv',
        # 'requests',
    ],
    entry_points={
        'console_scripts': [
            'main-script=scripts.main:main',
            'prompt-script=scripts.prompt:main',
        ],
    },
)
