#!/bin/sh -e

function usage() {
  cat <<EOF
Prerequisites.
* Atom installed
* sshfs installed
* EC2 external IP address is known ie cloudformation template has been run

$0 '<AWS EC2 External IP Address>' '/path/to/ssh_pem_file'

For example:
$0 35.166.122.127 ~/.ssh/streamlit.pem
EOF
  exit 1
}

function copy_ssh_private_key() {
  # If the key is in ${HOME}/.ssh then don't do anything
  if [[ "${KEY}" =~ .*/${USER}/.ssh/.*$ ]] && [ -f ${SSH_KEY} ] ; then
      echo "Key ${KEYNAME} is in ${HOME}/.ssh, not copying"
      return
  fi

  cp -v "${KEY}" "${SSH_KEY}"
  chmod 600 "${SSH_KEY}"

  # Needed to fix race condition
  touch "${SSH_DIR}/config"
}

function create_ssh_config() {
  cat <<EOF >> "${SSH_DIR}/config"

Host streamlit-aws
  Hostname ${IP}
  User ubuntu
  IdentityFile ${SSH_KEY}
  # For remote-atom
  RemoteForward 52698 localhost:52698
EOF
}

function install_streamlit_atom() {
  apm list --installed --bare | grep -q streamlit-atom || apm install streamlit-atom
}

function install_remote_atom() {
  apm list --installed --bare | grep -q remote-atom || apm install remote-atom
}

function configure_streamlit_atom() {
  # Not ideal but it works right now.
  sed -i -e "s|http://.*:8501|http://${IP}:8501|g" "${HOME}/.atom/packages/streamlit-atom/lib/streamlit-atom.js"
}

function next_steps() {
  cat <<EOF
Next steps:

sshfs streamlit-aws:src ~/remote-src

atom ~/remote-src/verify.py
Save file.

ssh streamlit-aws
python ~/src/verify.py

In Atom, Ctrl-Alt-O
EOF
}

IP=$1
KEY=$2

if [ -z $IP -o -z $KEY ] ; then
  usage
fi

SSH_DIR="${HOME}/.ssh"
KEYNAME="$(basename ${KEY})"
SSH_KEY="${SSH_DIR}/${KEYNAME}"

mkdir -p "${SSH_DIR}" "${HOME}/remote-src"

install_streamlit_atom
configure_streamlit_atom

install_remote_atom

copy_ssh_private_key
grep -q "${IP}" "${HOME}/.ssh/config" || create_ssh_config

next_steps
