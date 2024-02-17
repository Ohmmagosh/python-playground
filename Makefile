create-p:
	@read -p "Enter project name: " project_name; \
	poetry new $$project_name --name app; \
	echo "Project $$project_name created successfully";

del-p:
	@ls -la;
	@read -p "Enter project name to delete: " project_name;
	@read -p "Do you want to delete the $$project_name (y/n): "; reply
	if [ $$reply = "y" ]; then
	@echo "Deleting project $$project_name"; \
	rm -rf $$project_name; \
	echo "Project $$project_name deleted successfully";
	fi


