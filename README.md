# llama-exp
Experiments with AI using llama index library

This is a very simple setup of using llama-index to ingest data as index and to query your data using OpenAI as LLM.

### Notes (on data):
- You can change you input data which can be indexed and queried upon
- The program is using `UnstructuredReader` which reads unstructured data and converts it into text document
- You can change the data files in backend/data/uploaded folder and update `SOURCE_FILE_PATH` in the `ingest_data.py` to your file path

### Pre-requisite
1. You should have `OPENAI_API_KEY` in your environment, if you already do not have the key you can setup an account [OpenAI](https://openai.com/)
2. Create a `.env` file in the `backend` folder and add the `OPENAI_API_KEY` to the file
```
OPENAI_API_KEY=<your_key>
```


### Setup :

1. Create a python virtualenv on your system
```
virtualenv -p python3 llama-env

# Activate the environment
source ./llama-env/bin/activate
```
2. Install depdencies
```
pip install -r requirements.txt
```
3. Ingest data
```
cd backend
python src/ingest_data.py
```
4. Query data
```
cd backend
python src/query.py What is this document about?
```