# Function to install Python packages
install_package() {
    package=$1
    if pip install "$package"; then
        echo "Successfully installed $package"
    else
        echo "Failed to install $package"
    fi
}

# List of packages to install
packages_to_install=(
    "termios"
    "atexit"
    "sys"
    "PYopenal"
    "time"
    "os"
    "datetime"
    # Add more packages here as needed
)

# Install each package
for package in "${packages_to_install[@]}"; do
    install_package "$package"
done
