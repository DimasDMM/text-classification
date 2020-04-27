from .SVMModel import SVMModel

class ModelFactory:
    def __init__(self, logging, artifacts_path):
        self.__logging = logging
        self.__artifacts_path = artifacts_path

    def make(self, name):
        # Add here any other model loader
        if name == 'svm':
            return SVMModel(self.__logging, self.__artifacts_path)
        else:
            raise ValueError(name)
