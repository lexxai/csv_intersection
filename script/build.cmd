python build-version.py

mkdir "../pyinstall"
ERASE "../pyinstall" /S/Q
PUSHD "../pyinstall"

SET NAME=csv_intersection
pyinstaller "../%NAME%/main.py" --clean --name %NAME%  --onefile --version-file "../versionfile.txt"
POPD
python build-version.py ../pyinstall/dist/%NAME%.exe