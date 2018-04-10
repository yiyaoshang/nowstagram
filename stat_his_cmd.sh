#!bin/bash
#设置history为可显示
HISTFILE=~/.bash_history
set -o history
#统计使用率前十命令
cmd=`history |awk '{cmd[$2]++;count++} END {for (i in cmd) print i,cmd[i]/count*100"%"}'|sort -nr -k2,2|head -10`
sysdate=`date +%Y%m%d`
echo $sysdate
echo $cmd
