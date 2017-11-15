FROM django
RUN mkdir scripts
ADD . scripts/
WORKDIR scripts/rango/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py","runserver", "0:8000"]
