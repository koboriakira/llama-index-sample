from gazpacho import get, Soup
import time
import re
import os

def handle():
    base_url = 'https://help.qiita.com/'
    html = get(base_url)
    soup = Soup(html)

    # リンクページを集める
    links = []
    for link in soup.find('a'):
        if 'ja/articles' in link.attrs['href']:
            links.append(link.attrs['href'])

    # リンクページからタイトル、本文を集める
    for link in links:
        time.sleep(5)
        print(link)
        html = get(base_url + link)
        soup = Soup(html)
        title_element = soup.find('h1')
        if isinstance(title_element, list):
            title = title_element[0].text
        else:
            title = title_element.text

        article = soup.find('article', {'class': 'l-main'})
        if article is None:
            continue
        text = re.sub(re.compile('<.*?>'), '', article.html)

        # 保存する
        if not os.path.exists("sample_data"):
            os.makedirs("sample_data")
        with open("./sample_data/" + title + '.txt', 'w+') as f:
            f.write(text)

# python -m llama_index_sample.create_sample
if __name__ == '__main__':
    handle()
