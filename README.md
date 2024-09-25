# atcoder
acc session
oj login https://beta.atcoder.jp/

cd ~/workspace/github/atcoder/python

target="adt_easy_20240919_1"
acc new $target
cd $target;acc contest;

code ./a/main.py 

oj test -c "python3 ./main.py" -d ./tests/
acc s main.py -- --guess-python-interpreter pypy

acc task

# 
echo "alias acpy3='python3 your_script.py'" >> ~/.bashrc

<!-- echo 'oj test -c "python3 ./main.py" -d ./tests/'  >> ~/.bashrc -->