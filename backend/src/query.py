import os
import argparse
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

from llama_index import ServiceContext, StorageContext, load_index_from_storage

from utils.logger import getLogger
logger = getLogger('query_data')

parser = argparse.ArgumentParser(description='Process messages.')
parser.add_argument('message', metavar='m', type=str, help='A message prompt')
args = parser.parse_args()

service_context = ServiceContext.from_defaults(chunk_size_limit=512)

INDEX_DIR = './data/indexed'

def make_query(prompt):
    try:
        # rebuild storage context
        storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
        logger.info(f'---- Query the data: {prompt}')
        # load index, you can also pass index id if you have already stored it and want to query a single index
        global_index = load_index_from_storage(storage_context, service_context=service_context)
        query_engine = global_index.as_query_engine()
        response = query_engine.query(prompt)
        return response
    except Exception as e:
        logger.error('Something went wrong, perhaps you have not indexed the data? Run: python src/ingest_data.py')
        exit(0)


if __name__ == '__main__':
    response = make_query(args.message or 'What is this document about?')
    logger.info(f' Response: {response}')
