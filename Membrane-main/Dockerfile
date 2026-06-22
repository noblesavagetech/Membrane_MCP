# Stage 1: Build the React frontend
FROM node:20-alpine AS frontend-builder
WORKDIR /app

# Install dependencies first (better layer caching)
COPY package*.json ./
RUN npm install

# Copy rest of the frontend source and build
COPY tsconfig*.json vite.config.ts index.html postcss.config.js tailwind.config.js eslint.config.js ./
COPY public/ ./public/
COPY src/ ./src/
RUN npm run build

# Stage 2: Setup the Python backend
FROM python:3.12-slim
WORKDIR /app

# Install system dependencies for postgres and building extensions
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy backend code
COPY backend/ ./backend/

# Copy built frontend from Stage 1 into the /dist folder
COPY --from=frontend-builder /app/dist ./dist

# Railway provides PORT, default to 8000
ENV PORT=8000
EXPOSE ${PORT}

# Run the app. Notice the working directory changes to backend before running uvicorn
CMD ["sh", "-c", "cd backend && uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
