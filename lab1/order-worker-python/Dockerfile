FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости и устанавливаем их (кэширование слоёв)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код и конфиг
COPY worker.py .
COPY config.yml .

# -u отключает буферизацию вывода, чтобы логи сразу попадали в docker logs
CMD ["python", "-u", "worker.py"]
