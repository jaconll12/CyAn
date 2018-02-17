#zipping up Burp Report file
$source = "C:\r.xml"

$destination = ".zip"

 If(Test-path $destination) {Remove-item $destination}


#Add-Type -assembly "system.io.compression.filesystem"
#[io.compression.zipfile]::CreateFromDirectory($source, $destination) 



#Connection Details
$smtpServer = “
$msg = new-object Net.Mail.MailMessage

#Change port number for SSL to 587
$smtp = New-Object Net.Mail.SmtpClient($SmtpServer, 587) 

#Uncomment Next line for SSL  
$smtp.EnableSsl = $true

$pw = Get-Content \MailPW2.txt | ConvertTo-SecureString
#$cred = New-Object System.Management.Automation.PSCredential "james.lloyd@ensighten.com", $pw

$smtp.Credentials = New-Object System.Management.Automation.PSCredential "ens-gsc", $pw

#From Address
$msg.From = "security@ensighten.com"
#To Address, Copy the below line for multiple recipients
$msg.To.Add("james.lloyd@ensighten.com")

#Message Body
$msg.Body=”Web Instepct, Burp, Nessus, and SSLLabs Scans on have Run. The reports are attached”

#Message Subject
$msg.Subject = “Cybernetic Analyzer Report”

#your file location
$files=Get-ChildItem “C:\Reports\”

Foreach($file in $files)
{
Write-Host “Attaching File :- ” $file
$attachment = New-Object System.Net.Mail.Attachment –ArgumentList C:\Reports\$file
$msg.Attachments.Add($attachment)

}
$smtp.Send($msg)
$attachment.Dispose();
$msg.Dispose();
#Comments



#$From = """
#$To = ""
#$Attachment = ""

#$Subject = "Cybernetic Analyzer Reports"
#$Body = " Web Instepct, Burp, Nessus, and SSLLabs Scans on Pre-Prod have Run. The reports are attached"
#$SMTPServer = ""
#$SMTPPort = ""



#Send-MailMessage -From $From -to $To  -Subject $Subject -Body $Body -SmtpServer $SMTPServer -port $SMTPPort -UseSsl -Credential