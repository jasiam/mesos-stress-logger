FROM python:3.6-alpine

ENV LINES_TO_ADD $LINES_TO_ADD
ENV NUM_FILES $NUM_FILES
ENV KEYWORD $KEYWORD
ENV INTERVAL $INTERVAL

COPY . /stresslogger
WORKDIR /stresslogger/stresslogger

RUN pip install -r ../requirements.txt

ENTRYPOINT ["sh","-c","python3 stresslogger.py --num_files ${NUM_FILES} --keyword ${KEYWORD} --interval ${INTERVAL} ${LINES_TO_ADD}"]

