rule Suspicious_PowerShell_Download_Cradle {
    meta:
        description = "Detects obfuscated PowerShell download cradles utilizing WebClient or BITS"
        author = "Threat Research Lab"
        date = "2026-10-03"
        score = 80
        mitre_technique = "T1059.001"
    strings:
        $net_webclient = "Net.WebClient" nocase
        $download_string = "DownloadString" nocase
        $download_file = "DownloadFile" nocase
        $iex = "IEX" nocase
        $invoke_expr = "Invoke-Expression" nocase
        $hidden = "-w hidden" nocase
    condition:
        ($net_webclient and ($download_string or $download_file) and ($iex or $invoke_expr)) or
        ($hidden and $invoke_expr and $net_webclient)
}
