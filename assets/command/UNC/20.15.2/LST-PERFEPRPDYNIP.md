---
id: UNC@20.15.2@MMLCommand@LST PERFEPRPDYNIP
type: MMLCommand
name: LST PERFEPRPDYNIP（查询EpRpDyn对象的IP地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFEPRPDYNIP
command_category: 查询类
applicable_nf:
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# LST PERFEPRPDYNIP（查询EpRpDyn对象的IP地址）

## 功能

**适用NF：PGW-C、SGW-C、GGSN**

该命令用于查询EpRpDyn对象的本端IP地址和对端IP地址段。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EPRPDYNNAME | EpRpDyn对象名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定EpRpDyn对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD PERFEPRPDYN命令配置生成。 |
| IPVERSION | IP地址版本类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IP地址版本类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPV4（IPv4）”：表示地址类型为IPv4。<br>- “IPV6（IPv6）”：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| IPV4DIRECTION | IPv4方向 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于指定要配置的IPv4地址的方向。<br>数据来源：本端规划<br>取值范围：<br>- LOCAL_IP（本端IP地址）<br>- FAR_IP（对端IP地址段）<br>默认值：无<br>配置原则：无 |
| IPV6DIRECTION | IPv6方向 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于指定要配置的IPv6地址的方向。<br>数据来源：本端规划<br>取值范围：<br>- LOCAL_IP（本端IP地址）<br>- FAR_IP（对端IP地址段）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFEPRPDYNIP]] · EpRpDyn对象的IP地址（PERFEPRPDYNIP）

## 使用实例

查询EpRpDyn对象pgw1的所有本端IP地址和对端IP地址段，执行如下命令：

```
%%LST PERFEPRPDYNIP:;%%
RETCODE = 0  操作成功

结果如下
--------
EpRpDyn对象名称  IP地址版本类型  IPv4方向    IPv4地址  IPv4掩码长度       IPv6方向    IPv6地址       IPv6掩码长度

pgw1             IPv4            本端IP地址  10.0.0.0   32            本端IP地址  ::              0
pgw1             IPv6            本端IP地址  0.0.0.0   0              本端IP地址  2001:db8       32
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PERFEPRPDYNIP.md`
