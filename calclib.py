"""
    Library quick math calculation
"""

__all__ = []

class __Calclib:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b    
    
    @staticmethod
    def sub(a: int, b: int) -> int:
        return a - b    
    
    
    @staticmethod
    def subFloat(a: float, b: float) -> float:
        if not isinstance(a, float):
            a = float(a)
        
        if not isinstance(b, float):
            b = float(b)
        
        return a - b

        
    @staticmethod
    def addFloat(a: float, b: float) -> float:
        if not isinstance(a, float):
            a = float(a)
        
        if not isinstance(b, float):
            b = float(b)
        
        print(a, b)
        
        return a + b

    
    @staticmethod
    def help() -> None:
        """
            For printing out help, returns None
        """
        
        print("""
            A lib for math
        """)
    
    
    @staticmethod
    def internal():
        if __name__ == "__main__":
            print("this is a library to be called")       


__Calclib.internal()