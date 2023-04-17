
# Simple Endless Loop
# Don't forget to use:
# $ chmod +x bash_example.sh
while :
do
echo "git pull";
cd rpi-rgb-led-matrix
git pull
sleep 15;
done