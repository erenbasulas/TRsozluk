chmod +rx sozluk.sh
mor="\033[0;35m"
pembe="\033[38;5;198m"
yesil="\033[1;32m"
beyaz="\033[97m"
mavi="\033[1;34m"

chromedriverfunc() {
printf '\n'
read -p "Halihazırda yüklü bir '`printf "$yesil"`chromedriver`printf "$beyaz"`'ınız bulunuyor mu? (E/H)`echo $'\n\n--->'`" chdrsorgu
printf '\n'

if [[ $chdrsorgu == 'E' || $chdrsorgu == 'e' ]]; then
chrdrVarFunc

elif [[ $chdrsorgu == 'H' || $chdrsorgu == 'h' ]]; then
chrdrYokFunc

else
printf '\nLütfen geçerli bir komut girin.\n\n'
chromedriverfunc
fi
}

chrdrVarFunc() {
printf '\n'
read -p "Lütfen '`printf "$yesil"`chromedriver`printf "$beyaz"`'ın dosya konumunu doğru bir şekilde girin. (Şekildeki gibi: /root/hebele/hübele/chromedriver)`echo $'\n\n--->'`" chdrkonum
printf '\n'

if [[ $chdrkonum != '' ]]; then
> gerekli/chr_drv_yol.txt
echo $chdrkonum >> gerekli/chr_drv_yol.txt
sed -i '/^$/d' gerekli/chr_drv_yol.txt

else
printf '\n'$pembe'Boş bıraktınız, iptal ediliyor...\n\n'
exit
fi
}

chrdrYokFunc() {
apt-get install npm
npm install chromedriver -g
node /usr/local/lib/node_modules/chromedriver/install.js
mv /usr/local/lib/node_modules/chromedriver/lib/chromedriver/chromedriver gerekli
rm -r /usr/local/lib/node_modules/chromedriver
> gerekli/chr_drv_yol.txt
echo gerekli/chromedriver >> gerekli/chr_drv_yol.txt
sed -i '/^$/d' gerekli/chr_drv_yol.txt
}
chromedriverfunc

apt install python3-pip
pip3 install -r requirements.txt