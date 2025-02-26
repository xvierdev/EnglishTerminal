echo "Indentificando depedências... | Identifying dependencies..."
sleep 1,5
echo "Instalando o pacote Python... | Installing the Python package...\n"

echo "Aperte enter para continuar a instalação | Press enter to continue the installation\n"

echo "A instalação funciona testando vários gerenciadores de pacotes de cada distribuição então pode aparecer alguns erros no arquivo que você esta vendo" > Installationlogs.txt

sudo pacman -Syu
sudo apt update
sudo yum update
sudo zypper refresh

sudo pacman -S python > Installationlogs.txt
sudo apt-get install python > Installationlogs.txt
sudo yum install python > Installationlogs.txt
sudo zypper install python > Installationlogs.txt

echo "Caso queira mais detalhes sobre a instalção automática, basta abrir o arquivo installationlogs.txt | If you want more details about the automatic installation, just open the file installationlogs.txt\n"
sleep 2
echo "Executando EnglishTerminal... | Running EnglishTerminal..."
sleep 5
python source/terminal.py

