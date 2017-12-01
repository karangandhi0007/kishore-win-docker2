FROM python:3-windowsservercore

CMD ["python"]
# invoke python script to change env variables
WORKDIR C:\\kishore\\kishore-win-docker2
ADD read.py read.py
ADD test1.json test1.json
RUN pip install pystrich
# CMD ["python", "read.py", "-f", "test1.json"]
