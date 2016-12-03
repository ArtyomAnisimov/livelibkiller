#!/bin/bash
cd ..
project_root=$(pwd)

echo "Project root is $project_root"

echo "Please type the name of your project:"

read project_name

echo "Creating virtual envinronment.."
virtualenv --no-site-packages --prompt="($project_name)" venv
echo "Success.."

echo "Installing dependencies.."
source ./venv/bin/activate
pip install -r req.txt
echo "Success.."

echo "Installing models.."
python manage.py migrate

echo "Setup is done. Don't forget to tune your conf/dev/project_settings.py file."
