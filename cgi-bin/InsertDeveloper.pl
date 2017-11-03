use CGI;

$query = new CGI;

$cmd = "/usr/bin/java -Djava.security.egd=file:/dev/./urandom InsertDeveloper \"" . $query->param('dev_name') . "\"";
system($cmd);
my $referrer = $ENV{HTTP_REFERER};
print $query->redirect($referrer);
