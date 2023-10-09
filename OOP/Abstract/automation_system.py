from abc import *
class CollegeAutomationSystem(ABC):
    @abstractmethod
    def getStudentMarks(self):
        pass
    @abstractmethod
    def updateStudentMarks(self):
        pass

class Software(CollegeAutomationSystem):
    def getStudentMarks(self):
        print('getStudentMarks executing....')

    def updateStudentMarks(self):
        print('updateStudentMarks executing....')

s = Software()
s.getStudentMarks()
s.updateStudentMarks()