

value=$(ip addr show | grep -v LOOPBACK | grep -c mtu)

if [ $value -eq 1 ]
then
	echo "Found 1 network adapter active."
elif [ $value -gt 1 ]
then
	echo "Found multiple network adapter active."
else
	echo "No active adapters found."
fi

echo "Script execution completed!"
