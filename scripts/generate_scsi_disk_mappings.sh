chars=( {a..z} )
for ((i = 0; i <= 255; i += 1)); do 
	if [ $(( $i % 16 )) = 0 ]; then
		echo 8:$i sd${chars[i/16]}; 
	else
		echo 8:$i sd${chars[$(($(($i - $(($i % 16)) ))/16))]}$((i%16))
	fi
 done
