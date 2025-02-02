#!/bin/bash

source ./scripts/install/common.sh

./scripts/install/install_base_python_dependencies.sh
# ./scripts/install/download_base_models.sh
./scripts/install/install_llama_cpp.sh
# ./scripts/install/launch_main.sh

echo -e "${BOLDGREEN}Installation completed!${ENDCOLOR}"

read -p "Press enter to exit..."
echo
