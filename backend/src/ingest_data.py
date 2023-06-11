
import argparse

from llama_index import download_loader, GPTVectorStoreIndex
from llama_index import ServiceContext
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

from pathlib import Path

from utils.logger import getLogger

logger = getLogger('ingest_data')

doc_set = {}
all_docs = []

parser = argparse.ArgumentParser(description='Process messages.')
parser.add_argument('message', metavar='m', type=str, help='A message prompt')
args = parser.parse_args()

service_context = ServiceContext.from_defaults(chunk_size_limit=512)

DATA_DIR = './data'
UPLOAD_DIR = './data/uploaded'
INDEX_DIR = './data/indexed'

SOURCE_FILE_PATH = 'WIKIPEDIA/Bermuda_Triangle_Wikipedia.html'

def get_all_docs():
    logger.info('---- Preparing documents -----')
    try:
        UnstructuredReader = download_loader("UnstructuredReader", refresh_cache=True)
        loader = UnstructuredReader()
        wiki_data = loader.load_data(file=Path(f'{UPLOAD_DIR}/{SOURCE_FILE_PATH}'), split_documents=False)
        return wiki_data
    except Exception as e:
        logger.error(f'Error in getting documents {e}')


'''
We setup a separate vector index for each SEC filing from 2019-2022.
We also optionally initialize a "global" index by dumping all files into the vector store.
'''
def make_index(input_documents, params):
    logger.info('---- Make Index From Data -----')
    # NOTE: this global index is a single vector store containing all documents
    if params and params['generate']:
        global_index = GPTVectorStoreIndex.from_documents(input_documents, service_context=service_context)
        global_index.storage_context.persist(persist_dir=INDEX_DIR)
    else:
        logger.info('Not generating new index from the document')
    


if __name__ == '__main__':
    input_documents = get_all_docs()
    make_index(input_documents, {'generate': True })
    logger.info('Indexing data completed')
