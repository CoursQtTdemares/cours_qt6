# Prérequis Matériel - Formation Qt Programming avec Python

## 1. Objectifs de l'environnement de développement

Pour participer efficacement à cette formation, chaque participant doit disposer d'un environnement de développement complet et fonctionnel comprenant :

### Exigences essentielles :
- **Système d'exploitation** : Linux (Ubuntu/Debian recommandé) ou Windows 10/11
- **Droits administrateur** : Accès root/sudo (Linux) ou administrateur (Windows)
- **Python 3.10+** : Installation complète avec pip fonctionnel
- **IDE moderne** : VSCode ou Cursor avec extensions Python, ruff et mypy
- **Gestionnaire de paquets** : UV (Astral) pour la gestion des dépendances
- **Contrôle de version** : Git configuré avec accès GitHub

### Pourquoi ces prérequis sont-ils critiques ?
- **PyQt6** nécessite des dépendances système (bibliothèques Qt)
- **Installation de paquets** requise tout au long de la formation
- **Extensions VSCode** essentielles pour l'auto-complétion et le debugging
- **UV** pour une gestion moderne et rapide des environnements virtuels
- **Git/GitHub** pour les exercices collaboratifs et le partage de code

## 2. Configuration technique détaillée

### 2.1. Configuration Linux (Ubuntu/Debian)

#### Prérequis système :
```bash
# Mise à jour du système
sudo apt update && sudo apt upgrade -y

# Installation des dépendances système pour Qt
sudo apt install -y build-essential python3-dev python3-pip python3-venv
sudo apt install -y qt6-base-dev qt6-tools-dev-tools
sudo apt install -y libgl1-mesa-dev libxkbcommon-x11-0
```

#### Installation de Python :
```bash
# Vérifier la version Python (3.10+ requis)
python3 --version

# Si version insuffisante, installer Python moderne
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-dev
```

#### Installation d'UV :
```bash
# Méthode recommandée (officielle)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Ou via pip si curl non disponible
pip3 install uv

# Redémarrer le terminal ou sourcer le profile
source ~/.bashrc
```

#### Installation de Git :
```bash
sudo apt install git
```

#### Installation de VSCode :
```bash
# Télécharger et installer VSCode
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code
```

### 2.2. Configuration Windows

#### Prérequis système :
- **Windows 10/11** avec droits administrateur
- **Windows Terminal** (recommandé) ou PowerShell 5.1+

#### Installation de Python :
1. Télécharger Python 3.11+ depuis [python.org](https://www.python.org/downloads/)
2. **IMPORTANT** : Cocher "Add Python to PATH" lors de l'installation
3. Choisir "Install for all users" si possible
4. Vérifier l'installation dans PowerShell : `python --version`

#### Installation d'UV :
```powershell
# Méthode 1 : PowerShell (recommandée)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Méthode 2 : Via pip si la première échoue
pip install uv

# Redémarrer PowerShell après installation
```

#### Installation de Git :
1. Télécharger Git pour Windows : [git-scm.com](https://git-scm.com/download/win)
2. Installer avec les options par défaut
3. Configurer Git Bash comme terminal par défaut (optionnel)

#### Installation de VSCode :
1. Télécharger VSCode : [code.visualstudio.com](https://code.visualstudio.com/)
2. Installer avec les droits administrateur
3. Cocher "Add to PATH" lors de l'installation

### 2.3. Configuration commune (Linux/Windows)

#### Extensions VSCode obligatoires :
```bash
# Installation via ligne de commande
code --install-extension ms-python.python
code --install-extension charliermarsh.ruff
code --install-extension ms-vscode.vscode-git
```

#### Configuration Git et GitHub :
```bash
# Configuration utilisateur
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@exemple.com"

# Génération clé SSH
ssh-keygen -t ed25519 -C "votre.email@exemple.com"

# Afficher la clé publique (à ajouter sur GitHub)
cat ~/.ssh/id_ed25519.pub  # Linux
type %USERPROFILE%\.ssh\id_ed25519.pub  # Windows
```

## 3. Tests de validation de l'environnement

### 3.1. Vérification des versions

Exécuter les commandes suivantes dans un terminal :

```bash
# Versions des outils principaux
python --version          # Doit afficher 3.10+ 
pip --version             # Doit fonctionner sans erreur
uv --version              # Doit afficher la version d'UV
git --version             # Doit afficher la version de Git
code --version            # Doit afficher la version de VSCode
```

### 3.2. Test d'un projet Python simple

#### Créer un projet test :
```bash
# Créer un dossier de test
mkdir test-formation-qt
cd test-formation-qt

# Initialiser un projet UV
uv init
```

#### Créer un fichier `hello.py` :
```python
print("Hello, World!")
```

#### Tests de fonctionnement :
```bash
# Exécuter le script
uv run hello.py

# Tester l'installation de PyQt6
uv add pyqt6
python -c "import PyQt6.QtWidgets; print('PyQt6 OK')"
```

### 3.3. Test de VSCode et Git

```bash
# Ouvrir le projet dans VSCode
code .

# Initialiser Git
git init
git add .
git commit -m "Test initial environnement"

# Tester la connexion SSH GitHub
ssh -T git@github.com
```

### 3.4. Checklist finale de validation

- [ ] Python 3.10+ installé et fonctionnel
- [ ] UV installé et opérationnel
- [ ] Git configuré avec clé SSH GitHub
- [ ] VSCode ouvert avec extensions Python
- [ ] PyQt6 installable via UV
- [ ] Droits d'installation de paquets
- [ ] Terminal/PowerShell fonctionnel

## 4. Résolution des problèmes courants

### 4.1. Problèmes Linux
- **"Permission denied"** : Vérifier les droits sudo
- **Bibliothèques Qt manquantes** : Installer `qt6-base-dev`
- **Python non trouvé** : Utiliser `python3` au lieu de `python`

### 4.2. Problèmes Windows
- **"Python not found"** : Vérifier l'ajout au PATH
- **Execution Policy** : Exécuter `Set-ExecutionPolicy RemoteSigned`
- **UV non reconnu** : Redémarrer PowerShell après installation

### 4.3. Problèmes VSCode
- **Extensions non installées** : Vérifier les droits utilisateur
- **Python interpreter** : Ctrl+Shift+P → "Python: Select Interpreter"
- **Terminal intégré** : Configurer le bon shell par défaut

## 5. Recommandations organisateurs

### Configuration idéale pour la formation :
1. **Machines virtuelles** avec Ubuntu 22.04 LTS + tous les outils pré-installés
2. **Connexion internet stable** pour téléchargements et GitHub
3. **Droits administrateur** temporaires pendant la formation
4. **Support technique** disponible pour résolution rapide des problèmes

---

**Contact support** : Pour tout problème de configuration, prévoir une session de 30 minutes avant le début de la formation pour valider les environnements.
