# CSV追加する
df = pd.DataFrame()
df['年齢'] = agelist
df['肌状態'] = skinlist
df['ブランド'] = brands
df['商品名'] = items
df['レビュー評価'] = stars
df['投稿文'] = reviews

df.to_csv('Cosme.csv', index=False)