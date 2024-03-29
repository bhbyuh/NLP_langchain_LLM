from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader 
from langchain_community.document_loaders import OnlinePDFLoader
from langchain_community.document_loaders import MathpixPDFLoader
import time

class document_loaders:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_pdf_using_pypdf(self):
        try:
            loader = PyPDFLoader(self.file_path)
            pages = loader.load()
            return pages
        
        except Exception as e:
            print(f"Error: {e}")    
    
    def load_pdf_using_pymupdf(self):
        try:
            loader = PyMuPDFLoader(self.file_path)
            data = loader.load()
            return data
        
        except Exception as e:
            print(f"Error: {e}")

    def load_pdf_using_Unstructured(self):
        try:
            loader = UnstructuredPDFLoader(self.file_path)
            pages = loader.load()
            return pages
        
        except Exception as e:
            print(f"Error aya: {e}")    
    
    def load_pdf_using_OnlinePDFLoader(self):
        try:
            loader = OnlinePDFLoader(self.file_path)
            data = loader.load()
            return data
        
        except Exception as e:
            print(f"Error: {e}")

    def load_pdf_using_MathpixPDFLoader(self):
        try:
            loader = MathpixPDFLoader(self.file_path)
            data = loader.load()
            return data
        
        except Exception as e:
            print(f"Error: {e}")

dl = document_loaders(r"C:\Users\muaaz\OneDrive\Desktop\Mentorship\sensors-22-08281-v3.pdf")

start_time = time.time()
pypdf_results = dl.load_pdf_using_pypdf()
end_time = time.time()
execution_time = end_time - start_time
print("pypdf_results Execution time:", execution_time, "seconds")

start_time = time.time()
pymupdf_results = dl.load_pdf_using_pymupdf()
end_time = time.time()
execution_time = end_time - start_time
print("pymupdf_results Execution time:", execution_time, "seconds")

start_time = time.time()
Unstructured_results = dl.load_pdf_using_Unstructured()
end_time = time.time()
execution_time = end_time - start_time
print(" Unstructured_results Execution time:", execution_time, "seconds")

start_time = time.time()
OnlinePDFLoader_results = dl.load_pdf_using_OnlinePDFLoader()
end_time = time.time()
execution_time = end_time - start_time
print("OnlinePDFLoader_results Execution time:", execution_time, "seconds")

#MathpixPDFLoader_results = dl.load_pdf_using_MathpixPDFLoader()
