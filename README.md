# slurm-dev-docker

This container runs the following processes:

* slurmd (The compute node daemon for Slurm)
* slurmctld (The central management daemon of Slurm)
* slurmdbd (Slurm database daemon)
* munged (Authentication service for creating and validating credentials)
* mariadb (MySQL compatible database)
* supervisord (A process control system)

## usage

You must have configured and setup your CentOS 7 Virtual Machine.
Once in your CentOS VM clone our web repository.
```
cd
mkdir hpcc_project
cd hpcc_project
git clone https://github.com/MSU-HPCC/Backend.git
```

Now Build and run the docker image. You will end up in a shell with Slurm 17.11.10, Pyslurm, and the pip dependencies associated with the requirements.txt file at root directory level.
```
docker build -t slurm-dev .
docker run -v /home/$USER/hpcc_project:/web --net=host -it -h ernie slurm-dev
```

If you would like to run one command to drop yourself into the shell, run:
```
echo "alias slurmup='sudo service docker restart;sudo docker run -v /home/$USER/hpcc_project:web --net=host -it -h ernie slurm-dev'" >> ~/.bashrc
source ~/.bashrc
```

From now on you can lanuch your slurm environment by typing 'slurmup' in shell.

You will see our web project files inside the docker container at /web
Changes in ~/hpcc_project will reflect real time in the docker container at /web

Once inside the docker container please run supervisorctl status
You can use supervisorctl to restart the processes that drive slurm.
For more insight into supervisorctl please run:
```
supervisorctl -h
```


Majority of files from: https://github.com/giovtorres/docker-centos7-slurm/tree/17.11.10

Please see that page for more documentation.
