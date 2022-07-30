@echo off
echo DotCS - Uploading files to Github.
git config --global core.autocrlf false
set /p branch=Please enter your branch name: 
set /p commit=Please enter your commit info: 
echo Loading files.
git update-index --add --chmod=+x .\build\upx\Linux_amd64\upx
git update-index --add --chmod=+x .\build\upx\Linux_aarchc64\upx
git add .
echo Setting commit.
git commit -m "%commit%"
echo Setting branch.
git branch -M "%branch%"
echo Pushing.
git push -f -u DotCS "%branch%"
echo Finished.
pause