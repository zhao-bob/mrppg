import os
import tarfile

with tarfile.open('sample.tar', 'w:gz') as tar:
    for name in [f for f in os.listdir('.') if f.endswith('.py')]:
        tar.add(name)

with tarfile.open('sample.tar', 'r:gz') as tar:
    tar.extractall(path='sample')
