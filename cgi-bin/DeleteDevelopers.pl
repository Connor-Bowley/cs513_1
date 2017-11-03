#!/usr/bin/perl
use CGI;
#print "hello";
$query = new CGI;
$act = $query->param( 'act' );
if($act eq "Submit")
{
	#print "here";
	$cmd = "/usr/bin/java -Djava.security.egd=file:/dev/./urandom DeleteDevelopers";
	foreach $key ($query->param())
	{
		if($key ne "act")
		{
			if($query->param($key) eq "on")
			{
				$cmd .= " " . $key;
			}
		}
	}
	#print $cmd;
	system($cmd);
}
my $referrer = $ENV{HTTP_REFERER};
print $query->redirect($referrer);
