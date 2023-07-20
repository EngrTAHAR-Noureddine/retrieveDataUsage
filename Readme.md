# Install requirements
run setup.sh to install the packages
`./setup.sh`

# RUN Main
this main file contains the functions that are in seperated files
`python3 main.py`

# RUN run_in_one_file
this like main file but the functions in one file 
`python3 run_in_one_file.py`

# Install Package to record Usgaes every day
`sudo apt-get install sysstat`
<br /><br />
Then enable data collecting:
<br />
`$ sudo vi /etc/default/sysstat`
<br />
`change ENABLED="false" to ENABLED="true"`
<br />
`save the file`
<br /><br />
Last, restart the sysstat service:
<br />
`$ sudo service sysstat restart`
