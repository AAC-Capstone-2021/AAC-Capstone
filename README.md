## AAC-Capstone

AAC-Capstone is our capstone project that provides a web application for the Academic Assessment Committee at the University of Nebraska at Omaha.

Currently, the AAC has a member of different degree programs at UNO fill out an assessment of their respective program once every year or couple of years.  They fill this report out on a word document and send it back and forth between the AAC and the faculty member.  This process is tiresome and lengthy.

This web application will make filling out the form more accessible and a smoother process in general.  As a faculty member, they can log in and then access their forms from the past or fill out their form this year if one is required of them.  While filling the form, they will go step by step through the different major sections (SLOs, Assessments, Subassessments, and Analysis).  They are allowed to import old SLOs and old Assessments to make the process faster.  At the end, they can view their work and also see past forms.

As an AAC member, you can look at all of the departments past reports and also grade the completed reports that have been completed this year.  The member logs in and is taken to the home page where they can begin assessing the different forms or go to the archive and search for old forms.

## Basic Departmental Operation
As a department, to begin or continue filling out the form, click Start next to a report listed under To-Dos on the home page. Below the uncompleted reports will be reports with feedback from this year. Click through the pages to fill out the form, following buttons like "Add" and "Import" as appropriate. From home, you can also go to "Your Reports" and click view to see old reports.

## Basic AAC Operation
To access AAC functionality, click Administrative Home. Follow buttons to add or see departments, colleges, rubrics, and reports. To assign a new report, go to departments, find the right department, then click "Assign Report." The Generate Reports button will also create reports for the year, but does not create new reports for degree programs which have already been assigned one this year.
Once reports are submitted, return to the AAC reports list to see the option to view or review in place of the old options. Click review and complete each of the sections to review the report.

## Data Analysis
To see graphs or download CSV files, navigate to Your Reports or AAC Reports and click the relevant button in the upper-right hand corner. Follow the drop-down prompts and click the generate button to see or download the relevant file.

## Installation

In order to run this application, one needs to install the latest version of Python, Django, and also everything listed in requirements.txt. To run the application from your terminal, type 'python3 manage.py runserver' and go to localhost:8000 on your browser. The computer must be connected to the internet to reach the database and file server.

## Documentation Pages
https://aac-capstone-2021.github.io/AAC-Capstone/ 
## Release Notes
[P1] Finer-Grained approach for reporting by accredited programs
* Created Accrediting body programs text box to specify further information on what accrediting body looks for
* Added Accrediting body options for SLOs and Assessments
* Filtered data collection results for assessments when accrediting body option is selected

[P1] Stressing the important role of communication
* Created date option field in results communication 
* Created stakeholder options for internal and external stakeholders. 

[P2, P3] Enhance UI for textboxes
* Created word count for all summernote text boxes
* Created URL warning for all summernote text boxes

[P2] Simplify import
* Included origin of original SLO or assment when importing or editing 
* Ability to pull up previous report

[P4]Support for Reviewing
* Ability to assign multiple reviewers to a report

[P3] Enhanced UI
* Added UNO themed UI accross entire application. 
>>>>>>> be1f4f1d5b9b904e61d33c0f9a5e09724f500b40
