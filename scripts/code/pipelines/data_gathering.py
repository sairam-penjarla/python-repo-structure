from code.logging import logger
from code.utilities.common_utils import CommonUtils

class DataGathering:
    def __init__(self, config: dict) -> None:
        self.common_utils = CommonUtils()
        self.config = config

    def run(self):
        num_1 = self.config['values']['a']
        num_2 = self.config['values']['b']
        result = num_1 + num_2
        logger.info("Succesfully added two numbers")
        logger.info(f"Result: {result}")
        return result