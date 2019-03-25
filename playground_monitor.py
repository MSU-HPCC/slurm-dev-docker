#!/usr/bin/python3
import os
import time
import pyslurm
# pyslurm to submit JOB -- pyslurm.job().submit_batch_job({'script': BashScriptName}) OR
#   sbatch bashFile - Submit a batch script to Slurm. and returns ID I believe
# something like ""
# pyslurm to store job Id of job to get exit_code later

test_duration_minutes = 5
test_duration_secs = test_duration_minutes * 60
os.system("cd /playground")

output = os.popen("sbatch Bash.sb").read()
jobid = output.strip().split()[-1]
print("job id should be {}".format(jobid))
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
        job_dict = pyslurm.job().get()

        if(jobid in job_dict.keys()):
            print("printing status: {}".format(job_dict[jobid]['job_state']))
            print("printing error code: ".format(job_dict[jobid]['exit_code']))
            job_state = job_dict[jobid]['job_state']
            exit_code = job_dict[jobid]['exit_code']
        else:
            print(" okay that job id is no longer found...")
            print(job_dict.keys())

        if (job_state == 'RUNNING'):#job is running
            next_checkin_time += 30
            print("monitor is running test...")
            continue
        else: #job is not running
            break
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

# 5 minutes have ellapsed, clean up and return result
print("exiting monitor: should return result.")
# sleeping to give time to finish....
time.sleep(60)
job_dict = pyslurm.job().get()
print("rewriting state and error code, now that playground test has finished.")
job_state = job_dict[jobid]['job_state']
exit_code = job_dict[jobid]['exit_code']

if(jobid in job_dict.keys()):
    print("printing status: {}".format(job_dict[jobid]['job_state']))

pgResultFile = open("playground_result.txt","w+")
pgResultFile.write(job_state + "\n")
pgResultFile.write(exit_code + "\n")
pgResultFile.close()
