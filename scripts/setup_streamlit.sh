#!/bin/sh -e

function usage() {
  cat <<EOF
Usage:
  $0 IP_ADDRESS IDENTITY_FILE

Where:
  IP_ADDRESS is the IP address of your EC2 instance.
  IDENTITY_FILE is the file containing your key pair for the EC2 instance.

Example:
  $0 4.3.2.1 ~/Downloads/insight-user.pem

Other prerequisites:
  - This assumes Atom is installed. You can check with:
    apm --version
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
  sed -i -e "s|123.456.789.10:8501|${IP}:8501|g" "${HOME}/.atom/packages/streamlit-atom/lib/ProfileManager.js"
  sed -i -e "s|123.456.789.10:22|streamlit-aws:22|g" "${HOME}/.atom/packages/streamlit-atom/lib/ProfileManager.js"
}

IP=$1
KEY=$2

if [ -z $IP -o -z $KEY ] ; then
  usage
fi

SSH_DIR="${HOME}/.ssh"
KEYNAME="$(basename ${KEY})"
SSH_KEY="${SSH_DIR}/${KEYNAME}"

mkdir -p "${SSH_DIR}" "${HOME}/remote"

install_streamlit_atom
configure_streamlit_atom

install_remote_atom

copy_ssh_private_key
grep -q "${IP}" "${HOME}/.ssh/config" || create_ssh_config

echo 'Done!'
