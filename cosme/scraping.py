from selenium import webdriver
import pandas as pd

browser = webdriver.Chrome()
browser.get('https://www.cosme.net/item/item_id/900/reviews')
# ここでレビュー部分を指定し、余計なclassやタグを排除
review_list = browser.find_element_by_id('keyword-review-list')


# 完成版
# 投稿時間なし　
agelist = []
skinlist = []
brands = []
items = []
stars = []
reviews = []

# urllist = URL
# for category_url in urllist:


for page in range(0, 4):
    url = 'https://www.cosme.net/item/item_id/900/reviews/page/{}'.format(page)  # category_urlに書き換え
    browser.get(url)
    review_list = browser.find_element_by_id('keyword-review-list')

    # ブランド
    # 【課題】 〜からのお知らせがあります　←余分な言葉までもがスクレイピングされてしまう。　find_element構文で取り除くことは不可能？
    # if文の追加で余計な部分を取り除く
    elems_brand = review_list.find_elements_by_class_name('brand')
    for elem_brand in elems_brand:
        brand = elem_brand.text
        # if ~~~~
        brands.append(brand)

    # レビュー投稿者のステータス
    # 年齢、肌状態、口コミ数全体のスクレイピング
    elems_li = browser.find_elements_by_class_name('reviewer-info')
    for elem_li in elems_li:
        condition = elem_li.text.split('\n')[1]
        condition = condition.split('クチコミ投稿')[0]
        agelist.append(condition.split('歳')[0])
        skinlist.append(condition.split('歳')[1])

    # 商品名
    elems_item = review_list.find_elements_by_class_name('item')
    for elem_item in elems_item:
        item = elem_item.text
        items.append(item)

    # レビュー評価
    elems_star = review_list.find_elements_by_class_name('reviewer-rating')
    for elem_star in elems_star:
        star = elem_star.text
        star = star.split('購')[0]
        stars.append(star)

    # レビュー本文
    elems_review = review_list.find_elements_by_class_name('read')
    for elem_review in elems_review:
        review = elem_review.text.replace('\n', '')
        reviews.append(review)

    # カテゴリを追加する

