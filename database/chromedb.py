import chromadb
import pymupdf 
import re 
import uuid


class ChromaStorage: 
    def __init__(self, path="database/vectorstore"):
        self.client = chromadb.PersistentClient(path="database/vectorstore")
        self.chroma_client = chromadb.Client()
        collection_name = "xchat"
        existing_collections = self.chroma_client.list_collections()  # Returns list of names (strings)

        if collection_name in existing_collections:
            self.collection = self.chroma_client.get_collection(name=collection_name)  # Updated method
        else:
            self.collection = self.chroma_client.create_collection(name=collection_name)

    def add_documents(self, documents, ids):
        self.collection.add(documents= documents, ids= ids ) 

    def split_into_sentences(self, document):
        """Splits text into sentences using regex for better segmentation."""
        sentences = re.split(r'(?<=[.!?])\s+', document)  # Split on '.', '!', '?' followed by a space
        return sentences 
    
    def chunk_text(self, text: str, chunk_size: int, chunk_overlap: int):

        sentences = self.split_into_sentences(text)
        chunks = []
        current_chunk = []
        current_length = 0

        for sentence in sentences:
            sentence_length = len(sentence)

            # If adding this sentence exceeds chunk size, finalize the current chunk
            if current_length + sentence_length > chunk_size:
                if current_chunk:
                    chunk_text = " ".join(current_chunk)
                    chunk_id = str(uuid.uuid4())  # Generate unique ID
                    chunks.append((chunk_id, chunk_text))

                # Create an overlap by adding the last few sentences to the next chunk
                overlap_text = current_chunk[-chunk_overlap:] if chunk_overlap else []
                current_chunk = overlap_text
                current_length = sum(len(s) for s in overlap_text)

            # Add the sentence to the chunk
            current_chunk.append(sentence)
            current_length += sentence_length

        # Add the last chunk if not empty
        if current_chunk:
            chunk_text = " ".join(current_chunk)
            chunk_id = str(uuid.uuid4())  # Generate unique ID
            chunks.append((chunk_id, chunk_text))

        return chunks


    def query(self, query, top_k):
        return self.collection.query(query_texts=query, n_results=top_k)
    
    def read_documents(self, document_path): 
        filetype = document_path.split('.')[-1] 
        if filetype == "pdf": 
            doc = pymupdf.open(document_path) # open a document
            pages = [] 
            for page in doc: # iterate the document pages
                # text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
                text = page.get_text() # get plain text (is in UTF-8)

                pages.append(text)
            return " ".join(pages)


if __name__ == "__main__" : 
    vectorstore = ChromaStorage("/mnt/c/Users/sapko/OneDrive/Documents/chatbot/database/vector_store") 
    documents = vectorstore.read_documents("/mnt/c/Users/sapko/OneDrive/Documents/chatbot/data/Hateful_Sentiment_Detection_in_Real-Time_Tweets_An_LSTM-Based_Comparative_Approach.pdf")
    chunks = vectorstore.chunk_text(documents, 1000, 100)
    ids = [chunk[0] for chunk in chunks] 
    documents = [chunk[1] for chunk in chunks] 
    vectorstore.add_documents(documents, ids) 
    print(vectorstore.query("hate speech", 5))

    



