use CGI;

$query = new CGI;

$cmd = "/usr/bin/java -Djava.security.egd=file:/dev/./urandom FullDevInfo \"" . $query->url_param('did') . "\"";
system($cmd);
