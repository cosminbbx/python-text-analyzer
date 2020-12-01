import sys
import FileManager, ErrorHandler

try:
    fileText = FileManager.getText(sys.argv[1])
    print(fileText)
except IndexError:
    ErrorHandler.handleError("IndexError")
except FileNotFoundError:
    ErrorHandler.handleError("FileNotFoundError")
except:
    ErrorHandler.handleError("GenericError")

# f = open(filePath, "r")

#fileText = FileManager.getText(sys.argv[1])

# for i in range(0,len(fileText)):
#     if fileText[i] == "\n":
#         print(True)

#print(fileText)

#print(path)