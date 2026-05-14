# Stage 1: Сборка
FROM maven:3.9-eclipse-temurin-21-alpine AS builder

WORKDIR /app

# Копируем манифест зависимостей и исходный код
COPY pom.xml .
COPY src ./src

# Собираем проект, пропуская тесты
RUN mvn clean package -DskipTests

# Stage 2: Запуск
FROM eclipse-temurin:21-jre-alpine

WORKDIR /app

# Копируем только готовый JAR из стадии сборки
COPY --from=builder /app/target/*.jar app.jar

EXPOSE 8080

# JVM флаги для корректной работы в контейнере
ENV JAVA_OPTS="-XX:+UseContainerSupport -XX:MaxRAMPercentage=75.0"

ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]
