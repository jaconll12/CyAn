$results = Get-ChildItem C:\reports\ -Recurse -Include "*" 
$b = Get-Date -format M
$key = "Upload $b"
echo $key

foreach ($path in $results) {
    Write-Host $path
    $filename = [System.IO.Path]::GetFileName($path)
    Write-S3Object -BucketName ssdlc-scanning -File $path -Key $key/$filename -AccessKey ##### -SecretKey ####
}