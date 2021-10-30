# pdf2csv

P.S. Ran into A LOT of trouble trying to do this with WSL.

# Setup
First, install Java. This was helpful for me: https://medium.com/@pierre.viara/install-java-on-windows-10-linux-subsystem-875f1f286ee8

Or you can do this to install Java:
```CMD
sudo apt update
sudo apt install openjdk-11-jdk
```

Check your Java installation with:
```CMD
java --version
```

Then install tabula-py (wrapper for the Java Tabula). 
Documentation: https://pypi.org/project/tabula-py/

```CMD
pip3 install tabula-py
```

Then run the program
```
./main.py
```