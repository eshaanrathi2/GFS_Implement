 ## Implementation similar to: https://github.com/Bereket-G/Google-File-System-Implementation-with-Python

# Demonstration  -->
	
(launch the python files with separeate terminal)

	1. >>> python primary_BackUp_server.py
	2. >>> python Master_Server.py
	3. >>> python Chunks.py

	4. >>> python Client.py put ~/file_to_be_uploaded.txt myFileName 
	5. >>> python Client.py list
	lists all files uploaded.

	6. >>> python Client.py get myFileName
		-Here it will get the metadata from the chunk and finally it will combine the chunks and it will print it here.

	7. >>> python Client.py put ~/new/file oldFileName
		-It will overwrite the old file.

	8. >>> python Client.py delete myFileName
		-It will delete the from the metadata and also delete all chunks from respective chunk servers.