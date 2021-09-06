# Python Environment Outline #

### Use a virtual environment!! ###

For us to be able to work on this together and correctly edit and run the same code we will need to have all our project environments in a similar state.

This means working with the same version of python (I want to do 3.10-dev :P) and running of the same requirements.txt with matching module versions. If you want you can keep your virtual environment files in project root directory however it will/should be ignored in the GitHub repository.

My current setup is simply using pyenv and pyenv-virtualenv however there are a multitude of ways to achieve this. Using virtualenv directly rather than with a pyenv wrapper may be easier and much more documented. Ask for help though.

### Updating requirements.txt

I don't know/ have not used any automated way of keeping this in line other than being sure to have an up to date requirements.txt included with any commit that requires the new modules. During testing I advise any time that requires pip installing something should be added as a new feature branch - i.e create a branch, rebase during development when needed, and merge into main once completed.

To quickly save the current python environments installed modules run the following at the project root directory:

    pip freeze -r requirements.txt

And then ensure the requirements file is added to a commit bringing in the feature:

    git add requirements.txt
