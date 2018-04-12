#swagger code gen path
SWAGGER_CODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
SPEC_FILE=compute-storage.yml
DESTDIR=cloudmesh
CONFIG=$(DESTDIR)/config

help: ## show this help
	@echo 'usage: make [target] ...'
	@echo 'Make file sequence - startdb, service, test, stop'
	@echo 'targets:'
	@egrep '^(.+)\:\ .*##\ (.+)' ${MAKEFILE_LIST} | sed 's/:.*##/#/' | column -t -c 2 -s '#'

.PHONY : init clean

init:
	mkdir $(DESTDIR)

service: clean init ## generate service and start the swagger server
	echo "Generating swagger code"
	$(SWAGGER_CODEGEN) generate \
		-i $(SPEC_FILE) \
		-l python-flask \
		-o $(DESTDIR) \
		-D supportPython2=true
	cp -r aws/*.* $(DESTDIR)/swagger_server/controllers/
	if ! [ -d $(CONFIG) ]; then mkdir $(CONFIG); fi
	cp aws/*.yml $(CONFIG)
	pip install boto3
	pip install apache-libcloud
	echo "Installing Swagger server"
	cd $(DESTDIR) && pip install -r requirements.txt && python setup.py install 

start:
	echo "Starting Swagger Server"
	cd $(DESTDIR) && python -m swagger_server


test: ## Test swagger service
	echo "Create VM -->"
	curl -X POST "http://localhost:8080/cloudmesh/compute/aws/ec2" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"vmId\": \"NA\",  \"name\": \"myVM\",  \"image\": \"ami-25615740\",  \"region\": \"us-east-2\",  \"size\": \"t2.micro\",  \"status\": \"NA\"}"
	echo "Get VM List by region-->"
	curl -X GET "http://localhost:8080/cloudmesh/compute/aws/ec2/findByRegion?region=us-east-2" -H  "accept: application/json"
	#http://localhost:8080/cloudmesh/compute/aws/ec2/findByRegion?region=us-east-2
	echo "Get VM by Name-->"
	curl -X GET "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM?region=us-east-2" -H  "accept: application/json"
	#http://localhost:8080/cloudmesh/compute/aws/ec2/myVM?region=us-east-2
	echo "Start VM-->"
	curl -X POST "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM/start" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "region=us-east-2"	
	echo "Stop VM-->"	
	curl -X POST "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM/stop" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "region=us-east-2"
	echo "Terminate VM-->"	
	curl -X DELETE "http://localhost:8080/cloudmesh/compute/aws/ec2/myVM/terminate" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "region=us-east-2"
	

stop: ## Stop swagger server
	echo "Stopping swagger serevr"
	ps -ef | grep 'swagger_server' | grep -v grep | awk '{print $$2}' | xargs kill

clean: ## Clean generated directories
	echo "Removing directories"
	rm -rf $(DESTDIR)
	

