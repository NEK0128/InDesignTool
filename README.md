# InDesignTool

## 環境構築
HomeBrewのインストール
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
python3のインストール
```
brew install python3
```
packageのインストール
```
pip install -r requirements.txt
```

## 実行方法
ファイルの確認
```
ls
10-12月新商品画像       README.md               attach_image.py         code.txt                requirements.txt        result.txt
```
実行
```
python3 attach_image.py execute --img_path='10-12月新商品画像' --code_path='code.txt'
``` 
