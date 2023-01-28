#!/usr/bin/env bash
# ex: set fdm=marker
# usage {{{1 
#/ Usage: 
#/    -h|-?|--help)
#/       show this help and exit
#/
# 1}}} 
# environment {{{1 
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PROJECT=${PROJECT:-"Generate Dummy Databases with Python"}
# 1}}} 
# functions {{{1 
banner() { # {{{2
  # make a static banner with embeded color codes
  # BANNER=$(cat <<EOF\n  EOF;
  # for a simple banner use
  # BANNER="The \n$PROJECT\n\t script"
  # or have a little funn
  # BANNER=$(figlet "$PROJECT" | cowsay)
  # or do some coloring
  BANNER="\\e[32m$PROJECT\\e[39m"
  echo -e "$BANNER"
} # 2}}} 
die() { # {{{2 
  echo -e "\\e[31mFAILURE:\\e[39m $1"
  exit 1
} # 2}}} 
warn() { # {{{2 
  echo -e "\\e[33mWARNING:\\e[39m $1"
} # 2}}}
info() { # {{{2
  echo -e "\\e[32mINFO:\\e[39m $1"
} # 2}}}
show_help() { # {{{2 
  grep '^#/' "${BASH_SOURCE[0]}" | cut -c4- || \
    die "Failed to display usage information"
} # 2}}}
install_pddb() { # {{{2
  pipenv lock --clear && \
    pipenv install --dev
} # 2}}}
verify() { # {{{2
  OLD_PYTHONPATH="$PYTHONPATH"
  PYTHONPATH="$(pwd)"
  pipenv run flake8 .
  pipenv run pylint "$(pwd)"
  pipenv run pytest tests/
  PYTHONPATH="$OLD_PYTHONPATH"
} # 2}}}
clean() { # {{{2
  find . -name "*.pyc" -delete -o -name "__pycache__" -delete
  find . -name "*.egg-info" -exec rm -rf {} +
  find . -name "build" -exec rm -rf {} +
} # 2}}}
# 1}}} 
# arguments {{{1 
while :; do
  case $1 in # check arguments {{{2 
    verify) # run the verify command {{{3
      verify
      shift
      ;; # 3}}}
    install) # install the package {{{3
      install_pddb
      exit
      ;; # 3}}}
    clean) # clean up compile and egg files {{{3
      clean
      exit
      ;; # 3}}}
    -h|-\?|--help) # help {{{3 
      banner
      show_help
      exit
      ;; # 3}}} 
    -?*) # unknown argument {{{3 
      warn "Unknown option (ignored): $1"
      shift
      ;; # 3}}} 
    *) # default {{{3 
      break # 3}}} 
  esac # 2}}} 
done
# 1}}} 
# logic {{{1 
banner
# 1}}} 
