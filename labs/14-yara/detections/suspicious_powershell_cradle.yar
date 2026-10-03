rule Suspicious_PowerShell_Cradle {
    meta:
        description = "Detects WebClient download cradle patterns"
        author = "Threat Research Lab"
        date = "2026-10-03"
    strings:
        $wc = "Net.WebClient" nocase
        $df = "DownloadFile" nocase
        $ds = "DownloadString" nocase
    condition:
        $wc and ($df or $ds)
}
