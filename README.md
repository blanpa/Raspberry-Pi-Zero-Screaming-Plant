# Raspberry-Pi-Zero-Screaming-Plant

work in progress

Goal: Create a talking plant that tells you when it wants water and a pinch of Big Data.

A Raspberry Pi Zero combined with Seeed Grove Temperature and Moisture Sensor. Maybe more Sensors later, currently expensive.

Postgresql Database for storing the Data.

Grafana Web Dashboard which is connected to the Database, to display the current and historic data.







![Grafana Dashboard](./media/pictures/screenshot.png?raw=true "Grafana Dashboard")



## Setup the PostgreSQL Database

```
sudo apt install postgresql
```

## Setup Grafana

```
sudo apt-get install -y grafana
sudo /bin/systemctl enable grafana-server
sudo /bin/systemctl start grafana-server
```
## Setup the Script as a Service in Raspberry Pi


Now we're going to define the service to run this script:

```Shell
cd /lib/systemd/system/
sudo nano plant.service
```

The service definition must be on the /lib/systemd/system folder. Our service is going to be called "plant.service":

```text
[Unit]
Description=Plant
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python /home/pi/app.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
```
Here we are creating a very simple service that runs our  script and if by any means is aborted is going to be restarted automatically. You can check more on service's options in the next wiki: https://wiki.archlinux.org/index.php/systemd.

Now that we have our service we need to activate it:

```Shell
sudo chmod 644 /lib/systemd/system/plant.service
chmod +x /home/pi/app.py
sudo systemctl daemon-reload
sudo systemctl enable plant.service
sudo systemctl start plant.service
```

## Service Tasks
For every change that we do on the /lib/systemd/system folder we need to execute a daemon-reload (third line of previous code). If we want to check the status of our service, you can execute:

`sudo systemctl status plant.service`

In general:

### Check status
`sudo systemctl status plant.service`

### Start service
`sudo systemctl start plant.service`

### Stop service
`sudo systemctl stop plant.service`

### Check service's log
`sudo journalctl -f -u plant.service`


## REFERENCES
https://gist.github.com/emxsys/a507f3cad928e66f6410e7ac28e2990f#service-for-the-script