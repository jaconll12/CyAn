#Copy-Item C:\Users\Administrator\Desktop\*.html C:\reports

$a = Get-Date
$Day = + $a.Day
$Month = + $a.Month
$year = + $a.Year
$now=Get-Date -format "MM-dd-yyyy"
$filename= "c:\reports\$Month/$Day/$year.pdf"

cd "C:\Program Files\HP\HP WebInspect"
./WI.exe -u -n  -x -ps 1 -am .pdf -gp

