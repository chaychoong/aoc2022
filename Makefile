default:
	python main.py $(shell ls -d day* | sort -n | tail -n 1 | cut -d' ' -f1)
