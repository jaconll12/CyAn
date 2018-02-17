#remote clean upp script

$a = Get-Date
$Day = + $a.Day
$Month = + $a.Month
$year = + $a.Year
$newFolder= "$Month-$Day-$year"
$local = New-Item -ItemType directory -Path C:\archives\$newfolder


Copy-Item C:\reports\* $local
Remove-Item C:\reports\*