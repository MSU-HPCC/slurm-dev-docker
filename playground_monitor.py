# enter shabang here
import os
import time
#import pyslurm

#os.system("docker run stuffs")
#test if this drops you into a container automatically
# or if I now have to run:
# docker exec -it <container name> /bin/bash to get a bash shell in the container

# to run shell commands inside of docker container

# pyslurm to submit JOB -- pyslurm.job().submit_batch_job({'script': BashScriptName}) OR
#   sbatch bashFile - Submit a batch script to Slurm. and returns ID I believe
# something like ""
# pyslurm to store job Id of job to get exit_code later

test_duration_minutes = 5
test_duration_secs = test_duration_minutes * 60
start = time.time()
target_time = start + test_duration_secs # where 60 sec * 5 = 5 minutes from now.
next_checkin_time = start + 30
while(time.time() < target_time):
    # Occasionally need to check in with pyslurm to see if job is done or running
    # output file? -- yes
        # if job not running during this loop, it is good.
        # if job is done, has 0 exit_code, assume no source code errors
    # output file? -- no
        # if job is still running when this loop finished, it is good.
        # if job not running... assume reaped? -- Bad bash file
        # if job not running, has non-zero exit_code, assume Bad source code.
    if (next_checkin_time < time.time()):
        # pyslurm command to check if job is running

        if (1):#job is running
            next_checkin_time += 30
            continue
        else: #job is not running
            # os.system("call to check for output files")

            # if output file exists:
                # playground test returns GOOD JOB
            # else:
                # pyslurm to get exit code of job
                # if exit_code != 0:
                    # assume bad source code; can tell error
                # else:  ASSUME JOB WAS REAPED -- tell bad bash file
    else:
        # have not hit checkin time... sleep for 5 seconds
        time.sleep(5)
