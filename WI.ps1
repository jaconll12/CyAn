

$a = Get-Date
$Day = + $a.Day
$Month = + $a.Month
$year = + $a.Year
$now=Get-Date -format "MM-dd-yyyy"
$filename= "c:\reports\$Month/$Day/$year.pdf"

cd "C:\Program Files\HP\HP WebInspect"
./WI.exe -u URL -n WI_Cli -x -ps 1 -am Path_to_Macro/name.webmacro -v -r Vulnerability -y Standard -eb c:\reports\$Environment_$now.xml -f  c:\reports\$Environemt_$now.pdf -gp
