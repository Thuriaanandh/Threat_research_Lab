FROM python:3.11-slim
WORKDIR /workspace
RUN pip install --no-cache-dir jupyterlab pandas duckdb pyyaml rich requests scapy
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
