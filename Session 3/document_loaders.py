from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders.image import UnstructuredImageLoader
from langchain_community.document_loaders import json_loader
from langchain_community.document_loaders import email
import json
from pathlib import Path

class documentLoaders:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_pdf_using_pypdf(self):
        """
        This function will take the pdf file path and return the file content and metadata in
        response, where metadata includes the source and page no.
        """
        try:
            loader = PyPDFLoader(self.file_path)
            pages = loader.load()
            return pages
        
        except Exception as e:
            print(f"Error: {e}")    
    
    def load_pdf_using_pymupdf(self):
        """
        This function will take the pdf file path and return the file content and metadata in
        response, where metadata includes the source and page no.
        """
        try:
            loader = PyMuPDFLoader(self.file_path)
            data = loader.load()
            return data
        
        except Exception as e:
            print(f"Error: {e}")

    def load_csv(self):
        """
        This function will take the csv file path and return the file content and metadata in
        response. Metadata contains source file and row number in it.

        Return parameter: 
            data : {'page_content': "", "metadata": {"source": "", "row": ""}}
        """
        try:
            loader = CSVLoader(file_path = self.file_path)
            data = loader.load()
            return data
        
        except Exception as e:
            print(f"Error: {e}")

    def load_image(self):
        """
        This function will take the image file path and return the file content and metadata in
        response. Metadata contains source file and row number in it.

        Return parameter: 
            data : {'page_content': "", "metadata": {"source": "", "row": ""}}
        """
        try:
            loader = UnstructuredImageLoader(self.file_path)
            data = loader.load()
            return data
        
        except Exception as e:
            print(f"Error: {e}")

    def load_json(self):
        # loader=json_loader.JSONLoader(
        #     file_path=self.file_path,
        #     jq_schema='.articles[].title',
        #     text_content=False
        # )

        # data=loader.load()

        data = json.loads(Path(self.file_path).read_text(encoding='utf-8'))
        return data
    
    def loade_email(self):
        loader=email.UnstructuredEmailLoader(
            file_path=self.file_path
        )

        data=loader.load()
        return data

