from gazpacho import get, Soup
import time

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
        time.sleep(0)
        print(link)
        html = get(base_url + link)
        soup = Soup(html)
        title_element = soup.find('h1')
        if isinstance(title_element, list):
            title = title_element[0].text
        else:
            title = title_element.text

        text_elements = soup.find('article', {'class': 'l-main'}).find('p')
        if isinstance(text_elements, list):
            text = '\n'.join([e.text for e in text_elements])
        else:
            text = text_elements.text
        if text is None or text == '':
            continue

        # テキストを保存する
        with open(title + '.txt', 'w') as f:
            f.write(text)

# python -m llama_index_sample.create_sample
if __name__ == '__main__':
    handle()
