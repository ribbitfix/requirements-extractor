Requirements Extractor
======================
One small piece of a friend's larger project, in which I learned about working on the command line, parsing YAML and JSON, writing tests, and using Git and GitHub. Good times! Below are my notes from the process.

### 7/26/11
Tried to set TextMate as the default editor for git, using git config --global core.editor mate -w (the 3rd answer here: http://stackoverflow.com/questions/3539594/change-the-default-editor-for-files-opened-in-the-terminal-e-g-set-it-to-texte )

When I typed "git commit" it would open TextMate, but it would automatically abort the commit.

Using nano instead, it worked fine. (git config --global core.editor nano)

### 7/27
Installed Swampy and started working on Think Python chap 9 exercises.
NEXT TASK: finish Ex. 9.2.

### 8/1
NEXT: finish Ex. 9.6, p. 103

### 8/5
NEXT: finish Ex. 11.3, p. 126

### 8/6
Copied cpangloss directory to dropbox using the command line. Might need to change path to git repository?

NEXT: try to make something of a META.yml file.

### 8/7
Downloaded and installed pyYAML.
Both Terminal and Idle can find the yaml module, but TextMate can't. WHY?

Useful stuff in pyYAML:
- yaml.load(fin) converts a YAML document into a Python object. See also load_all() and safe_load()
- yaml.dump() accepts a Python object and produces a YAML document.
	- optional 2nd argument: an open text or binary file in which to write the document (which is otherwise returned by the function)

### 8/8
Wrote "extract_requirements" function:
- takes a yaml file
- converts it to a python dict
- searches the dict for keys containing "requires" and stores them in a new dict
- converts the new dict into JSON and returns it.

NEXT: figure out how to commit it to git?

### 8/9
Created cpanglossProject dir to put git stuff in (NEXT: move files there)

Researched tar format

### 8/10
JEFF SEZ:

Error handling:
```python
try:
    json.loads('blah blah')
except ValueError:
    print("Wasn't json!")
try:
    open('blah blah')
except IOError:
    print("Wasn't a file!")
```
Except do something useful instead of printing an error message.

Also: write a test involving a fake yaml file that doesn't include requirements - make sure the reqextractor can handle this situation.

Also: rewrite the function to output the "expected_json_dict" in the test. BUT FIRST, write the test to check for the things that aren't there yet: name and version.
Check whether the value of 'data' is of type dict; check for the number of keys, etc.

### 8/11
TO DO: learn about the following python libraries:
- ipdb
- unittest (not covered in Think Python)
- cStringIO

### 8/12
- to assert that dicts are equal, use a for loop to compare each key.
- if a string/file without the necessary data is passed to extract_requirements, the function should return {success : false, errors : [ 'error message', 'more different error message' ] }
- 5 is a magic number. Instead, use len(useful_data)
- add optional argument to allow for different data types

NEXT: look at the additions Jeff made to last test

### 8/13
QUESTION FOR JEFF: does it still make sense to split extract_requirements into multiple functions?
- GitHub for Mac requires a 64-bit processor. (Raebot has a 32.)
- Pushed my local repository to GitHub.
