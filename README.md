# queuecom
A program to queue commands to be executed in order.

## Usage
Suppose you have a file of commands named ``tasks.txt``.

```
# Copying large directory over SSH via rsync
rsync -rvz --info=progress2 directory1/ user@192.168.1.15:/home/directory2

# Remove contents of source directory and mount /dev/sda1 onto it
# Then copy another directory from SSH server
rm -rf directory1/*
mount /dev/sda1 directory1
rsync -rvz --info=progress2 user@192.168.1.15:/home/directory3 directory1/

# Display termination message
echo "Task done!"
```
By running ``queuecom.py tasks.txt``, the following tasks are run, one after one.
```
1 rsync -rvz --info=progress2 directory1/ user@192.168.1.15:/home/directory2
2 rm -rf directory1/*
3 mount /dev/sda1 directory1
4 rsync -rvz --info=progress2 user@192.168.1.15:/home/directory3 directory1/
5 echo "Task done!"
```
Note that command 1 and command 4 (rsync) are likely to take a long time.

As soon as command 1 runs, ``tasks.txt`` would remove the first command.
With your favorite text editor, you could edit subsequent commands.

The program ends when all the lines in the ``tasks.txt`` file are removed.