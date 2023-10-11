#!/bin/bash

# Menu
show_menu() {
    echo
    echo "- MENU -"
    echo "1. Shutdown Cool Servers."
    echo "2. Update Cool Servers."
    echo "3. Upgrade Cool Servers."
    echo "4. Exit"
}

# Function 1
option1() {
    echo "You have selected option 1: Shutdown Cool Servers !!!"
    echo

    # Good night babies !!!
    ansible-playbook ./playbooks/goodnight.yaml -i inventory.yaml --ask-become-pass
}

# Function 2
option2() {
    echo "You have selected option 2: Update Cool Servers !!!"
    echo

    # Use Ansible and B Happy !!!
    ansible-playbook ./playbooks/update.yaml -i inventory.yaml --ask-become-pass
}

# Function 3
option3() {
    echo "You have selected option 2. Upgrade Cool Servers !!!"
    echo
    
    # Anaconda is bigger than Python !!!
    ansible-playbook ./playbooks/upgrade.yaml -i inventory.yaml --ask-become-pass
}

# Loop principal
while true; do
    show_menu
    read -p "Select an option: " choice

    case $choice in
        1) option1 ;;
        2) option2 ;;
        3) option3 ;;
        4) echo -e "Exiting the script.\n "; break ;;
        *) echo "Invalid option. Try again..." ;;
    esac
done




