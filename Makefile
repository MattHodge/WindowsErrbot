clean:
	rm -rf data
	find . -name __pycache__ | xargs rm -rf
	rm -rf .vagrant
