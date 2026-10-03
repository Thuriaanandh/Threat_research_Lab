rule Mimikatz_Credential_Dump_Strings {
    meta:
        description = "Detects common plaintext strings and commands associated with Mimikatz credential dumping tool"
        author = "Threat Research Lab"
        date = "2026-10-03"
        score = 95
        mitre_technique = "T1003.001"
    strings:
        $mimi_1 = "sekurlsa::logonpasswords" nocase ascii wide
        $mimi_2 = "lsadump::sam" nocase ascii wide
        $mimi_3 = "privilege::debug" nocase ascii wide
        $mimi_4 = "sekurlsa::minidump" nocase ascii wide
        $author = "gentilkiwi" nocase ascii wide
    condition:
        2 of ($mimi_*) or ($author and 1 of ($mimi_*))
}
