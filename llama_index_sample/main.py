from llama_index import StorageContext, load_index_from_storage

# rebuild storage context
from llama_index.indices.base import BaseQueryEngine

def handle():
    # ./storageからindexを読み込む
    storage_context = StorageContext.from_defaults(persist_dir='./storage')
    index = load_index_from_storage(storage_context)

    # クエリを投げる
    query_engine: BaseQueryEngine = index.as_query_engine()
    response = query_engine.query("いいねとストックの違いを教えて")
    # response = query_engine.query("アドベントカレンダーの記事を書きたい")

    # 結果を表示する
    print(response.response) # 解答
    # print(response.source_nodes) #解答を生成するための材料になった文書

if __name__ == '__main__':
    handle()
