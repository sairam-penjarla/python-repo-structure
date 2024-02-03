from code.logging import logger

class CommonUtils:
    def __init__(self) -> None:
        pass
    
    def adder(self, a:int, b:int) -> int:
        logger.info(f"Value of a: {a}")
        logger.info(f"Value of b: {b}")
        return a+b
    
    def multiply(self, a:int, b:int) -> list:
        return [a*b]