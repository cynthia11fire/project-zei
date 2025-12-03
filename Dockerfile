# 使用官方 Python 輕量版映像檔
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製依賴套件清單並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製所有程式碼到容器中
COPY . .

# 設定環境變數 (請在執行時注入 API Key，不要寫死在這裡)
ENV PORT=8080

# 宣告容器執行的指令 (假設 main.py 是您的啟動檔)
CMD ["python", "main.py"]
