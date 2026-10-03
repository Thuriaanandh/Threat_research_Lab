rule Suspicious_PE_High_Entropy_Dropper {
    meta:
        description = "Detects small PE executables containing suspicious payload staging markers"
        author = "Threat Research Lab"
        date = "2026-10-03"
        score = 75
        mitre_technique = "T1027"
    strings:
        $mz = "MZ"
        $cmd_spawn = "cmd.exe /c" ascii
        $ps_spawn = "powershell -ExecutionPolicy Bypass" ascii
        $temp_path = "\AppData\Local\Temp\" ascii wide
    condition:
        uint16(0) == 0x5a4d and ($cmd_spawn or $ps_spawn) and $temp_path and filesize < 500KB
}
