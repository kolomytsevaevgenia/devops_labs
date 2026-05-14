# Stage 1: Build
FROM golang:1.22-alpine AS builder

WORKDIR /app

# Копируем go.mod и go.sum для кэширования зависимостей
COPY go.mod go.sum ./
RUN go mod download

# Копируем исходный код
COPY . .

# Собираем статический бинарник
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o auth-service ./cmd/auth-service

# Stage 2: Runtime
FROM alpine:3.19

# Устанавливаем базовые пакеты (ca-certificates для HTTPS)
RUN apk --no-cache add ca-certificates

WORKDIR /root/

# Копируем бинарник из builder-стадии
COPY --from=builder /app/auth-service .

# Копируем дефолтный конфиг (можно переопределить через env)
COPY --from=builder /app/config.yml .

# Порт, который слушает сервис
EXPOSE 8081

# Запуск через env-переменные для конфигурации
CMD ["./auth-service"]
