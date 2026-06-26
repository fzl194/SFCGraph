# ConfigTask/builder/verify/object_family.py
"""对象族核查：命令按对象关键字分组。"""

_FAMILY_MAP = {
    "URR": "URR", "URRGROUP": "URR", "PCCPOLICYGRP": "URR", "PCCACTIONPROP": "URR",
    "URRGRPBINDING": "URR", "SPECURRGRPLIST": "URR", "URRFAILACTION": "URR",
    "FILTER": "FILTER", "FILTERIPV6": "FILTER", "L7FILTER": "FILTER",
    "FLOWFILTER": "FILTER", "FLOWFILTERGRP": "FILTER",
    "FLTBINDFLOWF": "FILTER", "PROTBINDFLOWF": "FILTER",
    "RULE": "RULE", "RULEBINDING": "RULE",
    "USERPROFILE": "PROFILE",
    "POOL": "POOL", "SECTION": "POOL", "POOLGROUP": "POOL",
    "POOLBINDGROUP": "POOL", "POOLGRPMAP": "POOL",
    "VPNINST": "VPN", "L3VPNINST": "VPN", "VPNINSTAF": "VPN", "IPBINDVPN": "VPN",
    "OSPF": "OSPF", "OSPFAREA": "OSPF", "OSPFNETWORK": "OSPF",
    "OSPFV3": "OSPF", "OSPFV3AREA": "OSPF", "OSPFV3INTERFACE": "OSPF",
    "OSPFV3IMPORTROUTE": "OSPF", "OSPFIMPORTROUTE": "OSPF",
    "BWMCONTROLLER": "BWM", "BWMRULE": "BWM", "BWMUSERGROUP": "BWM",
    "BWMSERVICE": "BWM", "BWMRULEGLOBAL": "BWM",
    "LICENSESWITCH": "LICENSE", "REFRESHSRV": "REFRESH",
}
_IGNORE_FAMILIES = {"LICENSE", "REFRESH"}


def classify_family(command):
    """命令名 → 对象族。"""
    parts = command.split(None, 1)
    if len(parts) < 2:
        return "OTHER"
    obj = parts[1].strip()
    return _FAMILY_MAP.get(obj, "OTHER")


def verify_family_coherence(commands):
    """检查命令是否主要属于同一族（忽略 LICENSE/REFRESH）。

    Returns:
        list[str]: 警告消息（空 = 一致）
    """
    from collections import Counter
    families = Counter()
    for cmd in commands:
        fam = classify_family(cmd)
        if fam not in _IGNORE_FAMILIES:
            families[fam] += 1

    total = sum(families.values())
    if total == 0:
        return []

    max_family, max_count = families.most_common(1)[0]
    ratio = max_count / total

    if ratio <= 0.5:
        return [f"对象族分散: 最大族 {max_family} 占比 {ratio:.0%}, 族分布 {dict(families)}"]
    return []
