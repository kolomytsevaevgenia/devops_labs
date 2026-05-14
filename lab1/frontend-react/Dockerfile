# Stage 1: Сборка
FROM node:20-alpine AS builder

WORKDIR /app

# Копируем манифесты зависимостей (кэширование слоёв)
COPY package.json package-lock.json* ./
RUN npm install

# Копируем исходный код и собираем production-бандл
COPY . .
RUN npm run build

# Stage 2: Раздача статики
FROM nginx:alpine

# Удаляем дефолтную страницу приветствия Nginx
RUN rm -rf /usr/share/nginx/html/*

# Копируем собранные файлы из стадии builder
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

# Запуск Nginx в foreground-режиме (обязательно для Docker)
CMD ["nginx", "-g", "daemon off;"]
