#!/usr/bin/env python3

# Author ID: [161112214]

import subprocess

def free_space():
    p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == "__main__":
    print(free_space())
