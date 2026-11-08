FROM python:3.12-slim
WORKDIR /app
COPY td_alerts.py .
ENV STATE_FILE=/data/td_state.json PYTHONUNBUFFERED=1
VOLUME /data
CMD ["python", "td_alerts.py"]
