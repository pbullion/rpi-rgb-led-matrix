#!/bin/bash
################
# Uncomment if you want the script to always use the scripts
# directory as the folder to look through
#REPOSITORIES="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
i=1
while [ "$i" -ne 0 ]
do
  then
    echo "Updating at `date`"
    then
      git status
      echo "Fetching"
      git fetch
      echo "Pulling"
      git pull
    else
      echo "Skipping because it doesn't look like it has a .git folder."
    fi
    echo "Done at `date`"
    echo
  fi
done
sleep 120
done