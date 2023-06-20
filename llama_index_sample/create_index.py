from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.indices.base import BaseQueryEngine


def handle():
    # `create_sample_data.py`で作成したsample_dataを読み込む
    documents = SimpleDirectoryReader('sample_data').load_data()

    # VectorStoreIndexを作成する
    index = VectorStoreIndex.from_documents(documents)

    # ./storageにindexを保存
    index.storage_context.persist()

if __name__ == '__main__':
    handle()
