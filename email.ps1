#zipping up Burp Report file
$source = "zip_source"

$destination = "report_folder"

 If(Test-path $destination) {Remove-item $destination}

#Add-Type -assembly "system.io.compression.filesystem"
#[io.compression.zipfile]::CreateFromDirectory($source, $destination)

#Connection Details
$smtpServer = “smtp_server”
$msg = new-object Net.Mail.MailMessage

#Change port number for SSL to 587
$smtp = New-Object Net.Mail.SmtpClient($SmtpServer, 587)

#Uncomment Next line for SSL
$smtp.EnableSsl = $true

$pw = Get-Content "Path_To_password_file" | ConvertTo-SecureString

$smtp.Credentials = New-Object System.Management.Automation.PSCredential "account", $pw

#From Address
$msg.From = "from@mail.com"
#To Address, Copy the below line for multiple recipients
$msg.To.Add("to@mail.com")

#Message Body
$msg.Body=”Web Instepct, Burp, Nessus, and SSLLabs Scans have Run. The reports are attached”

#Message Subject
$msg.Subject = "Cybernetic Analyzer Report"

#your file location
$files=Get-ChildItem “localfilelocation”

Foreach($file in $files)
{
Write-Host “Attaching File :- ” $file
$attachment = New-Object System.Net.Mail.Attachment –ArgumentList $localfile\$file
$msg.Attachments.Add($attachment)

}
$smtp.Send($msg)
$attachment.Dispose();
$msg.Dispose();
#Comments
