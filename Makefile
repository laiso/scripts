test:
	find * -type d -name '.git' -prune -o -type d -exec make -C {} \;
