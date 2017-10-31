<!DOCTYPE html>
<html>
<head>
<title>My Blog</title>
</head>
<body>

%if (username != None):
Welcome {{username}}        <a href="/logout">Logout</a> | <a href="/newpost">New Post</a><p>
%end
%if (username == None):
<a href="/signup">Sign Up</a> <a href="/login">Login</a>

<h1>My Blog</h1>


This is a placeholder for the blog

</body>
</html>


