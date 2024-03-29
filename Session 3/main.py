from document_loaders import documentLoaders
from config import *

def load_content(file_path, file_extension=None):
    loader = documentLoaders(file_path) # Create a document loader object
    if file_extension == "pdf":
        file_content = loader.load_pdf_using_pymupdf() #extract the content of pdf file from pymupdf loader
    elif file_extension == "csv":
        file_content = loader.load_csv() #extract the content of csv file from CSV loader
    elif file_extension == "png":
        file_content = loader.load_image()
    elif file_extension=="json":
        file_content=loader.load_json()
    elif file_extension=="eml":
        file_content=loader.loade_email()
    return file_content
    

def main():
    supported_files = ["pdf", "csv", "png","eml","json"]
    file_index = int(input("""\t\t\t\tEnter 1 to select a pdf file. \n
                              Enter 2 to select a csv file. \n
                              Enter 3 to select a image file.\n 
                              Enter 4 to select JSON file. \n 
                              Enter 5 to select email file. \n
                              Number: """)) 
    if file_index == 1:
        FILE_PATH = PDF_FILE_PATH
    elif file_index == 2:
        FILE_PATH = CSV_FILE_PATH
    elif file_index == 3:
        FILE_PATH = PNG_FILE_PATH 
    elif file_index==4:
        FILE_PATH=JSON_FILE_PATH
    elif file_index==5:
        FILE_PATH=EMAIL_FILE_PATH

    file_extension = FILE_PATH.split('\\')[-1].split(".")[-1] #extract the file extension e.g. pdf from the file path
    if file_extension not in supported_files: #if the file extension is not lie in supported files list, then return exception
        return("This file is not supported at the moment.")
    """
    Load the file content
    """
    file_content = load_content(FILE_PATH, file_extension)
    print(file_content)


if __name__ == "__main__":
    main()
