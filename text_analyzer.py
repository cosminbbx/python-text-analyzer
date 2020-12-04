import sys
import FileManager, ErrorHandler, TextParser , OutputHelper

def main():
    try:
        fileText = FileManager.getText(sys.argv[1])

        information = TextParser.parse(fileText)

        OutputHelper.format(information)
    except IndexError:
        ErrorHandler.handleError("IndexError")
    except FileNotFoundError:
        ErrorHandler.handleError("FileNotFoundError")
    except:
        ErrorHandler.handleError("GenericError")

main()

