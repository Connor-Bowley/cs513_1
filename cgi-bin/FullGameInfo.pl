use CGI;

$query = new CGI;

$cmd = "/usr/bin/java -Djava.security.egd=file:/dev/./urandom FullGameInfo \"" . $query->url_param('asin') . "\"";
system($cmd);
