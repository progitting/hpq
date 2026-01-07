Intro
=
Is it possible to make an operating system in 6 months?

# Parts of an operating system

* bootloader; finds operating system, loads kernel into memory and starts it

* kernel is the operating system

# What does an kernel /operating system do?

* bridge SW and HW (e.g. program can play music)
* process scheduling and isolation (e.g. game can run without freezing computer)
* memory management (i.e. all programs have enough memory to run)
* filesystem management (e.g. programs can save & load from disk)

# Process scheduling

* decides which process gets to run on the CPU
* switches between processes very quickly (multitasking)
* prevents one program from blocking the whole system
* gives higher priority tasks more CPU time
* saves and restores process state during context switches
* ensures fairness so all programs make progress

# Memory management
* gives each program its own isolated memory space
* keeps track of which memory regions are free or used
* loads program code and data into RAM when needed
* uses virtual memory so programs can use more memory than physically available
* swaps memory pages to disk when RAM is full
* protects memory so programs cannot overwrite each other

# Filesystem management
* organizes data into files and folders
* maps file names to actual data blocks on disk
* stores metadata like size, permissions, timestamps
* allocates and frees disk blocks as files grow or shrink
* provides APIs for reading, writing, creating, deleting files

# What is the complexity of real OS (linux)
![image](https://makelinux.github.io/kernel/map/LKM63_512.png)

URL: https://makelinux.github.io/kernel/map/

# How many lines of code does each subsystem have
![image](https://raw.githubusercontent.com/satoru-takeuchi/linux-kernel-statistics/refs/heads/master/image/number_of_lines_of_each_subsystem_for_each_release.png)

URL: https://github.com/satoru-takeuchi/linux-kernel-statistics

# What I've done
* I made reasearch into the topic of operating systems
* understood subsystems and what they do
* I chose to implement a trivial file system in python that allows you to manage files and directories

# Details about small problem chosen to code

* directories have name and can contain other directories and files
* files have a name, content, and size
* each file or directory links to an inode storing metadata (size, creation time) and content reference
* support creating, reading, writing, and listing files and directories

# Code at github, details
URL: https://github.com/progitting/hpq

# Additional resources
* Modern Operating Systems, Global Edition, 5th edition
* https://www.minix3.org/
