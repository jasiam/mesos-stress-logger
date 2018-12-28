import datetime
import os
import time
import click


@click.command()
@click.argument('lines_to_add')
@click.option('--num_files','-n')
@click.option('--keyword','-k')
@click.option('--interval','-i')
def main(lines_to_add,num_files,keyword, interval):
    print("Starting stresslogger")
    for i in range(int(num_files)):
        path = "/mnt/mesos/sandbox/folder"+str(i)
        os.makedirs(path,exist_ok=True)

    while True:
        print("Writing log lines")
        for i in range(int(num_files)):
            now = datetime.datetime.now()
            log_line = "{0} This is a log line including {1} written by stresslogger tool {2}".format(str(now),keyword,i)
            path = "/mnt/mesos/sandbox/folder" + str(i)
            for j in range(int(lines_to_add)):
                f = open(path + "/stdout", 'a+')
                f.write(log_line + str(j)+"\n")
                f.close()
        time.sleep(int(interval))


if __name__ == "__main__":
    main()


