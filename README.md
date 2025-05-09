# 💱 Currency Converter – Centralized vs Distributed Architecture

This project demonstrates the key differences between a **centralized** and a **distributed** system using a simple **currency converter** application.

---

## 📌 Project Structure

currency-converter/
├── centralized/ # All logic (frontend + backend) in a single service
├── distributed/ # Separated frontend and backend services (via API)
└── README.md
---

## 🏗️ Centralized Architecture

In the `centralized/` folder, you will find a monolithic application built with **Python Flask** and **Jinja2 templates**.

- The frontend and backend are tightly coupled.
- All business logic and presentation are handled within a single service.
- It runs as a standalone container.

### ➕ Pros
- Simple to develop and deploy.
- Fewer moving parts.

### ➖ Cons
- Hard to scale individual components.
- Tightly coupled: any change in logic affects the whole system.

---

## 🌐 Distributed Architecture

In the `distributed/` folder, the application is divided into two services:
- A **frontend** (`HTML + JS`) that calls...
- A **backend API** (`Flask`) that performs the currency conversion.

They communicate via **HTTP (fetch)** using a `docker-compose` setup.

### ➕ Pros
- Better separation of concerns.
- Scalable and more maintainable.
- More realistic to how modern web systems operate.

### ➖ Cons
- Slightly more complex setup.
- Requires inter-service communication management.

---

## 🚀 How to Run

### Centralized Version

```bash
cd centralized
docker build -t centralized-currency .
docker run -p 5000:5000 centralized-currency

cd distributed
docker-compose up --build

| Feature       | Centralized      | Distributed                          |
| ------------- | ---------------- | ------------------------------------ |
| Architecture  | Monolithic       | Microservices-style                  |
| Coupling      | Tightly coupled  | Loosely coupled                      |
| Scalability   | Low              | High                                 |
| Communication | Internal         | Via HTTP (REST API)                  |
| Deployment    | Single container | Multiple containers (Docker Compose) |



🧠 Educational Value
This project is perfect for:

Understanding basic system architecture differences.

Practicing Docker and containerization.

Seeing how separation of concerns improves scalability.

🛠️ Technologies Used
Python 3

Flask

HTML/CSS/JavaScript

Docker & Docker Compose

📄 License
MIT License. Free to use and modify for educational purposes.

---

Este es el archivo completo, listo para ser utilizado en tu repositorio. ¿Te gustaría proceder con el contenido de los archivos principales de los sistemas centralizados o distribuidos?
