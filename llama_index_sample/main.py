from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.indices.base import BaseQueryEngine

def handle():
    # `create_sample_data.py`で作成したsample_dataを読み込む
    documents = SimpleDirectoryReader('sample_data').load_data()

    # VectorStoreIndexを作成する
    index = VectorStoreIndex.from_documents(documents)

    # クエリを投げる
    query_engine: BaseQueryEngine = index.as_query_engine()
    response = query_engine.query("いいねとストックの違いを教えて")

    # 結果を表示する
    print(response.response) # 解答
    print(response.source_nodes) #解答を生成するための材料になった文書

if __name__ == '__main__':
    handle()
