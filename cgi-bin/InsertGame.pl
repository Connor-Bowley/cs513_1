use CGI;

$query = new CGI;
$asin = "" ;
$title = "";
$price = "";
$cmd = "/usr/bin/java -Djava.security.egd=file:/dev/./urandom InsertGame ";
foreach $key ($query->param()) {
	$value = $query->param($key);
	if($key eq "asin") {
		$asin = $value;
	}
	elsif($key eq "title") {
		$title = $value;
	}
	elsif($key eq "price") {
		$price = $value;
	}
}
@devs = $query->param("developers");
$cmd .= "\"" . $asin . "\" \"" . $title . "\" \"" . $price . "\" ";
foreach $dev (@devs) {
	$cmd .= $dev . " ";
}
#print '\n' . $cmd;
system($cmd);
my $referrer = $ENV{HTTP_REFERER};
print $query->redirect($referrer);
