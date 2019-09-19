FROM python:3-onbuild
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 4000
ENTRYPOINT ["python"]
CMD ["app.py"]