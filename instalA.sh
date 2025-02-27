<<<<<<< HEAD
#!/bin/bash

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

echo "${YELLOW}Indentificando dependências... | Identifying dependencies...${NC}"
sleep 1.5

# Função para verificar e instalar um pacote
verificar_e_instalar() {
  local gerenciador=$1
  local pacote=$2
  local comando_verificacao=$3
  local comando_instalacao=$4

  if ! eval "$comando_verificacao"; then
    echo "${YELLOW}Pacote '$pacote' não encontrado. Tentando instalar com $gerenciador... | Package '$pacote' not found. Trying to install with $gerenciador...${NC}"
    if sudo eval "$comando_instalacao"; then
      echo "${GREEN}Pacote '$pacote' instalado com sucesso usando $gerenciador! | Package '$pacote' installed successfully using $gerenciador!${NC}"
      return 0 # Sucesso
    else
      echo "${RED}Falha ao instalar '$pacote' usando $gerenciador! | Failed to install '$pacote' using $gerenciador!${NC}"
      return 1 # Falha
    fi
  else
    echo "${GREEN}Pacote '$pacote' já está instalado. | Package '$pacote' is already installed.${NC}"
    return 0 # Sucesso
  fi
}

# Atualizar listas de pacotes (tentativa para as principais distribuições)
echo "${YELLOW}Atualizando listas de pacotes... | Updating package lists...${NC}"
sudo pacman -Syy 2>/dev/null
sudo apt update 2>/dev/null
sudo yum update -y 2>/dev/null
sudo zypper refresh 2>/dev/null
echo "${YELLOW}Atualização das listas de pacotes concluída. | Package list update completed.${NC}"
sleep 1

# Verificar e instalar Python
echo "${YELLOW}Verificando e instalando Python... | Checking and installing Python...${NC}"
if verificar_e_instalar "python3" "python3" "command -v python3 >/dev/null 2>&1" "apt-get install -y python3"; then
  PYTHON="python3"
elif verificar_e_instalar "python" "python" "command -v python >/dev/null 2>&1" "apt-get install -y python"; then
  PYTHON="python"
else
    echo "${RED}Python não encontrado e falha ao instalar! O script não pode continuar. | Python not found and failed to install! The script cannot continue.${NC}"
    exit 1
fi

echo "${YELLOW}Python está instalado e configurado. | Python is installed and configured.${NC}"

# Verificar e instalar Git
echo "${YELLOW}Verificando e instalando Git... | Checking and installing Git...${NC}"
if verificar_e_instalar "pacman" "git" "command -v git >/dev/null 2>&1" "pacman -S --noconfirm git"; then
  : # Sucesso já tratado dentro da função
elif verificar_e_instalar "apt-get" "git" "command -v git >/dev/null 2>&1" "apt-get install -y git"; then
  : # Sucesso já tratado dentro da função
elif verificar_e_instalar "yum" "git" "command -v git >/dev/null 2>&1" "yum install -y git"; then
  : # Sucesso já tratado dentro da função
elif verificar_e_instalar "zypper" "git" "command -v git >/dev/null 2>&1" "zypper install -y git"; then
  : # Sucesso já tratado dentro da função
else
  echo "${RED}Git não encontrado e falha ao instalar! O script não pode continuar sem Git. | Git not found and failed to install! The script cannot continue without Git.${NC}"
  exit 1
fi

echo "${GREEN}Git está instalado e configurado. | Git is installed and configured.${NC}"

# Obter o diretório home do usuário
HOME_DIR="$HOME"

# Definir o diretório de destino para o clone
TARGET_DIR="$HOME_DIR/EnglishTerminal"

# Clonar o repositório
echo "${YELLOW}Clonando o repositório EnglishTerminal para $TARGET_DIR... | Cloning the EnglishTerminal repository to $TARGET_DIR...${NC}"
if git clone https://github.com/xvierdev/EnglishTerminal "$TARGET_DIR"; then
  echo "${GREEN}Repositório clonado com sucesso! | Repository cloned successfully!${NC}"
else
  echo "${RED}Falha ao clonar o repositório! | Failed to clone the repository!${NC}"
  exit 1
fi

# Executar o script
echo "${YELLOW}Executando EnglishTerminal... | Running EnglishTerminal...${NC}"
sleep 2

# Verificar se o arquivo terminal.py existe antes de executar
if [ -f "$TARGET_DIR/source/terminal.py" ]; then
  "$PYTHON" "$TARGET_DIR/source/terminal.py"
else
  echo "${RED}Erro: Arquivo 'terminal.py' não encontrado em '$TARGET_DIR/source/'.  Verifique a instalação. | Error: 'terminal.py' file not found in '$TARGET_DIR/source/'. Check the installation.${NC}"
  exit 1
fi

echo "${GREEN}Fim do script. | End of script.${NC}"
exit 0
=======
echo "Indentificando depedências... | Identifying dependencies..."
sleep 1,5
echo "Instalando o pacote Python... | Installing the Python package...\n"

echo "Aperte enter para continuar a instalação | Press enter to continue the installation\n"

echo "A instalação funciona testando vários gerenciadores de pacotes de cada distribuição então pode aparecer alguns erros no arquivo que você esta vendo" > Installationlogs.txt

sudo pacman -Syu > Installationlogs.txt
sudo apt update > Installationlogs.txt
sudo yum update > Installationlogs.txt
sudo zypper refresh > Installationlogs.txt

sudo pacman -S python > Installationlogs.txt
sudo apt-get install python > Installationlogs.txt
sudo yum install python > Installationlogs.txt
sudo zypper install python > Installationlogs.txt

echo "Caso queira mais detalhes sobre a instalção automática, basta abrir o arquivo installationlogs.txt | If you want more details about the automatic installation, just open the file installationlogs.txt\n"
sleep 2
echo "Executando EnglishTerminal... | Running EnglishTerminal..."

echo -ne "\r5"
sleep 0.5
echo -ne "\r5."
sleep 0.5
echo -ne "\r5.."
sleep 0.5
echo -ne "\r5..."
sleep 0.5
echo -ne "\r5...4"
sleep 0.5
echo -ne "\r5...4."
sleep 0.5
echo -ne "\r5...4.."
sleep 0.5
echo -ne "\r5...4..."
sleep 0.5
echo -ne "\r5...4...3"
sleep 0.5
echo -ne "\r5...4...3."
sleep 0.5
echo -ne "\r5...4...3.."
sleep 0.5
echo -ne "\r5...4...3..."
sleep 0.5
echo -ne "\r5...4...3...2"
sleep 0.5
echo -ne "\r5...4...3...2."
sleep 0.5
echo -ne "\r5...4...3...2.."
sleep 0.5
echo -ne "\r5...4...3...2..."
sleep 0.5
echo -ne "\r5...4...3...2...1"
sleep 0.1
python source/terminal.py

>>>>>>> origin/new_feats
