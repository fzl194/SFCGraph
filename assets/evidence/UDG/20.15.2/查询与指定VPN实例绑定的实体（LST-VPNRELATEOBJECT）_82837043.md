# 查询与指定VPN实例绑定的实体（LST VPNRELATEOBJECT）

- [命令功能](#ZH-CN_CONCEPT_0182837043__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837043__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837043__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837043__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837043__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837043__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837043)

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询与指定VPN实例绑定的实体。包括绑定指定VPN的APN、地址池、L2TP组、DNAI。

#### [注意事项](#ZH-CN_CONCEPT_0182837043)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837043)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837043)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | VPN名称 | 可选必选说明：必选参数<br>参数含义：VPN实例的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |
| DSPTYPE | 类型 | 可选必选说明：可选参数<br>参数含义：指定查询类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- APN：绑定指定VPN的APN。<br>- IPPOOL：绑定指定VPN的地址池。<br>- L2TP：绑定指定VPN的L2TP组。<br>- ALL：所有与指定VPN实例绑定的实体。<br>- DNAI：绑定指定VPN的DNAI。<br>默认值：ALL<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837043)

查询绑定指定VPN的实体：

```
LST VPNRELATEOBJECT: VPNNAME=" vpn1";
```

```

RETCODE = 0  操作成功。

VPN关联对象
-----------
Result  =  
APN list
--------
          [INFO]:APN do not bind with VPN!
Pool Information
----------------
          [INFO]:IPPool do not bind with VPN!
DNAI list
---------
          [INFO]:DNAI do not bind with VPN!
L2TP Group Information
----------------------
          [INFO]:L2tpGroup do not bind with VPN!
------------------------------

(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837043)

| 输出项名称 | 输出项解释 |
| --- | --- |
| APN | APN列表。 |
| Pool Name | 地址池信息。 |
| L2TP Group ID | L2TP组信息。 |
| DNAI list | DNAI信息。 |
