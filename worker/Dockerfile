# ============================
# Stage 1 — Build environment
# ============================
FROM python:3.10 as builder

WORKDIR /build

# Install build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libjpeg-dev \
    libpq-dev \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install pip packages into a virtual environment
COPY requirements.txt .
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

# ============================
# Stage 2 — Minimal runtime
# ============================
FROM python:3.10-slim as runtime

# Set working directory
WORKDIR /app

# Install runtime deps only
RUN apt-get update && apt-get install -y \
    libffi-dev \
    libssl-dev \
    libxml2 \
    libxslt1.1 \
    zlib1g \
    libjpeg62-turbo \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

# Copy app code
COPY . .

CMD ["bash"]