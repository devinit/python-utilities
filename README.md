# Python Utility Functions

A home for useful python functions with cross-cutting potential across projects

## Modules

### 'google-docs.py'

A function to extract data from both google sheets and google docs. Here you can find a function for sheets - pull_sheet_data_values - and docs - pull_doc_values.

In the code, you can see a brief explanation on how to create your own credentials to allow these functions to work. 
Requirements (google-auth==2.6.0 and google-api-python-client==2.40.0) are specified in 'requirements.txt'.

## Contribution

Before adding a new function, please check to make sure there isn't an existing module in which the function could belong.
If there is none, create a new module with as generic a name as possible e.g. if you're adding a function that splits strings,
create a module called `strings.py` and add the function there.

Document your utility functions, clearly explaining their parameters and usage - do this both in the code and this read me under `modules`
