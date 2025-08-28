curl -L -o chromadb.tar.gz https://github.com/halean/donkhieunai/releases/download/prebuiltdb/chromadb.tar.gz
mkdir -p ./chromadb_all_f
tar --overwrite -xzf chromadb.tar.gz -C ./chromadb_all_f/
curl -L -o txts.gz https://github.com/halean/donkhieunai/releases/download/prebuiltdb/txts.gz
mkdir -p ./txts
tar --overwrite -xzf txts.gz  -C ./txts/
