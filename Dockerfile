# ベースとなるPythonの軽量イメージを指定
FROM python:3.10-slim

# 作業ディレクトリを設定
WORKDIR /app

# システム依存関係をインストール（例: PostgreSQLライブラリなど）
RUN apt-get update && apt-get install -y gcc libpq-dev

# 依存関係をインストールするために requirements.txt をコピー
COPY requirements.txt .

# 必要なPythonパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをすべてコピー
COPY . .

# サーバーを起動するコマンドを指定
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
