# Based off of http://mnaoumov.wordpress.com/2013/08/21/powershell-resolve-path-safe/
function Resolve-FullPath{
    [cmdletbinding()]
    param
    (
        [Parameter(
            Mandatory=$true,
            Position=0,
            ValueFromPipeline=$true)]
        [string] $path
    )
     
    $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($path)
}

$pathToLibs = "..\..\finstat_libs"

$pathToLibs = Resolve-FullPath -path $pathToLibs
$Env:PYTHONPATH = $Env:PYTHONPATH + ";" + $pathToLibs
python manage.py runserver
