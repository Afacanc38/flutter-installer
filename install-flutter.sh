#!/bin/bash

# Flutter Installer
# Copyright (C) 2021  Alperen İsa Nalbant

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

echo "Dependencies are being established..."
sudo apt-get install bash curl file git unzip xz-utils zip dialog -y>>/dev/null

echo "Downloading Flutter..."
curl https://storage.googleapis.com/flutter_infra/releases/stable/linux/flutter_linux_2.0.5-stable.tar.xz --output flutter-stable.tar.xz

echo "Archive extracting..."
tar xf ./flutter-stable.tar.xz>>/dev/null

echo "Changing filename to .flutter and moving to home directory..."
mv flutter .flutter
mv .flutter ~/

echo "Adding PATH..."
echo 'export PATH="$PATH:~/.flutter/bin"'>>~/.bashrc
export PATH="$PATH:~/.flutter/bin"
source ~/.bashrc

echo "Completing the setup..."
flutter precache>>/dev/null

echo "Flutter automatically sends multiplication reports and feature usage statistics to Google."
echo "For details, visit https://k.yapboz.ml/flutter-reporları."
echo "To do this, restart the terminal and type 'flutter config --no-analytics && dart --disable-analytics' to close."

echo "Setup is complete!"
