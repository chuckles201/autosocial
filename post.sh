# go to get github password
cd .. 
username=$(cat user.txt)
password=$(cat pass.txt)

# posts automatically to github
cd auto-post/
git add .
# commiting
msg="autosocial-deployment $(date)"
git commit -m "$msg"

# sending usernmae and password
expect <<EOF
    spawn git push origin
    expect "Username for 'https://github.com':"
    send "$username\r" 
    expect "Password for 'https://$username@github.com':"
    send "$password\r"
    expect eof
EOF

echo Succesfully Pushed!