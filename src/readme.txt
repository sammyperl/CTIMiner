Contact information
- dgkim0803@{korea.ac.kr || hksecurity.net || gmail.com}

1. Requirements
	a. Data storage: MISP (http://www.misp-project.org/)
	b. Data storage API: pymisp (https://github.com/MISP/PyMISP) - provided in this project data as a package
	c. IoC extractor: ioc_parser (https://github.com/armbues/ioc_parser) - provided in this project data as a package
	d. Cyber threat report repository
	    - APT reports (https://github.com/aptnotes/data)
	    - APT & CyberCriminal Campaign Collection (https://github.com/CyberMonitor/APT_CyberCriminal_Campagin_Collections)
	e. Malware repository: malwares.com API license(key)
	f. additional python libraries: xlrd, pdfminer, requests, joblib, dicttoxml, pefile (for data exporting)
	g. the configuration file including the root directory of reports, the file of report list, MISP server URL and the API key, and the malware repository key. 
	
2. ReportList_format.csv
This file should be located in the directory that 'ReportList' indicates in the 'config.xml' file.
The neccesary items to execute CTIMiner are 1st and 6th item, filename and Date. Others can be ignored.

