FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
# MAINTAINER boyi.zhang

COPY ./app /app/app
COPY requirement.txt /app/app/
RUN pip install -r /app/app/requirement.txt

EXPOSE 8090
EXPOSE 80
EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
#RUN uvicorn app.main:app --port 8090