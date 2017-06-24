import os

class Services():
    @staticmethod
    def getAuditoryCortex():
        return os.getenv('SERVICES_AUDITORY_CORTEX')

    @staticmethod
    def getBrocasArea():
        return os.getenv('SERVICES_BROCAS_AREA')

    @staticmethod
    def getCerebrum():
        return os.getenv('SERVICES_CEREBRUM')
    