var1=`awk 'NR==1{print $1}' $1`
var2=`sed -n 1p $1 | awk '{print $NF}'`
sed "s/$var2/$3/" $1 | head -n $var1 >$2
echo "***********CT Error Handled and File Generated.***********"
