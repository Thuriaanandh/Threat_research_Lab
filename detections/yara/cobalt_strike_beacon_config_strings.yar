rule Cobalt_Strike_Beacon_Config_Indicators {
    meta:
        description = "Identifies configuration artifacts and strings typical of Cobalt Strike malleable C2 profiles"
        author = "Threat Research Lab"
        date = "2026-10-03"
        score = 90
        mitre_technique = "T1071.001"
    strings:
        $pipe_pattern = "\\\\.\\pipe\\msagent_" ascii
        $default_ua = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)" ascii
        $c2_uri = "/activity" ascii
        $beacon_loader = "ReflectiveLoader" ascii
    condition:
        2 of them
}
