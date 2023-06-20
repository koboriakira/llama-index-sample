# llama-index-sample

Qiitaのヘルプ文章をサンプルとさせていただき、llama-indexの挙動を確認するためのリポジトリです。

```
git@github.com:koboriakira/llama-index-sample.git
cd llama-index-sample
pip install -r requirements.txt
```

## 使い方

`OPENAI_API_KEY`を環境変数に定義する。

```
export OPENAI_API_KEY={YOUR_API_KEY}
```

Qiitaヘルプをスクレイピングして、必要なテキストデータを保存。  
(負荷軽減のため、5秒ごとにサイトにアクセスするようにしています。)

```
python -m llama_index_sample.create_sample
```

llama-indexを利用して、インデックスを作成・保存

```
python -m llama_index_sample.create_index
```

インデックスを利用してクエリを実行

```
python -m llama_index_sample.main
```

次のようなレスポンスが出てきます。

```
いいねとストックの違いは、いいねは記事を読んで気に入ったときに表示されるボタンで、記事を保存しておくことができません。一方、ストック機能を使うと、「あとでじっくり読みたい」「繰り返し読みたい」記事を保存しておくことができます。また、ストックを用いることで、記事の通知を受け取ることや、ストックした記事内での検索ができるなどの便利な機能があります。
```

## 参照

- [jerryjliu/llama_index: LlamaIndex (GPT Index) is a data framework for your LLM applications](https://github.com/jerryjliu/llama_index)
- [Qiita ヘルプ](https://help.qiita.com/)
