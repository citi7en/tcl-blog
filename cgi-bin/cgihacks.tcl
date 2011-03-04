proc Cgi_Header {title {body {bgcolor=white text=black}}} {
  puts stdout "Content-Type: text/html

<html>
  <head>
    <title>$title</title>
  </head>

  <body $body>
    <h1>$title</h1>"
}
