#!/usr/bin/env python

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

#### GNU Genel Kamu Lisansı hakkında bilgilendirme
print("Flutter Yükleyici  Copyright (C) 2021  Alperen İsa Nalbant. \nBu program KESİNLİKLE HİÇBİR GARANTİSİ YOKTUR; ayrıntılar için LICENSE dosyasına bakın. \nBu bir özgür yazılımdır ve belirli koşullar altında yeniden dağıtabilirsiniz. Ayrıntılar için LICENSE dosyasına bakın.\n")
#### Kütüphaneler

# Sistem komutlarını çalıştırabilmesi için bu kütüphaneyi etkinleştirelim.
import os
import time

#### İndirme

# Flutter'ı wget kullanarak indirelim.
print('Flutter indiriliyor...')
os.system('wget -b https://storage.googleapis.com/flutter_infra/releases/stable/linux/flutter_linux_2.0.2-stable.tar.xz>>/dev/null')

#### Kurulum

# Bağımlılıkları yükleyelim
print('Bağımlılıklar kuruluyor...')
os.system('sudo apt-get install bash curl unzip zip xz-utils git -y>>/dev/null')

# Flutter'ı tar komutunu kullanarak çıkaralım.
print('Arşiv çıkarılıyor...')
os.system('tar xf ~/Downloads/flutter_linux_2.0.2-stable.tar.xz>>/dev/null')

# Flutter'ı ev dizinine taşıyalım ve gizleyelim.
print('Klasör taşınıyor...')
os.system('mv flutter_linux_2.0.2-stable .flutter && mv .flutter ~/')

# Flutter'ın yolunu .bashrc dosyasına ekleyelim.
print("Yol .bashrc dosyasına ekleniyor...")
os.system('echo "export \'PATH="$PATH:~/.flutter/flutter/bin\'">>~/.bashrc')
os.system('source ~/.bashrc')

# Anonim veri göndermeyi devre dışı bırakalım
veri = input('Flutter bazen (örneğin çöktüğünde) anonim veriler gönderebilir. Ayrıntılar için https://k.yapboz.ml/flutter-raporları adresini ziyaret edin. \nBu devre dışı bırakılsın mı? [e/H] ')
if "e" in veri:
    print('Devre dışı bırakılıyor...')
    os.system('flutter config --no-analytics>>/dev/null')
    print('Kurulum tamamlanıyor...')
    os.system('flutter precache>>/dev/null')
    print('Kurulum tamamlandı! Daha sonra ne yapacağınızı öğrenmek için "flutter doctor" komutunu çalıştırın.')
else:
    print('Atlandı.')
    print('Kurulum tamamlanıyor...')
    os.system('flutter precache>>/dev/null')
    print('Kurulum tamamlandı! Daha sonra ne yapacağınızı öğrenmek için "flutter doctor" komutunu çalıştırın.')
