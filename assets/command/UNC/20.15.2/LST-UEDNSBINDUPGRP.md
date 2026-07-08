---
id: UNC@20.15.2@MMLCommand@LST UEDNSBINDUPGRP
type: MMLCommand
name: LST UEDNSBINDUPGRP（查询UPF组的DNS属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UEDNSBINDUPGRP
command_category: 查询类
applicable_nf:
- GGSN
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- DNS选择管理
- UPF组DNS域名策略
status: active
---

# LST UEDNSBINDUPGRP（查询UPF组的DNS属性）

## 功能

**适用NF：GGSN、PGW-C、SMF**

该命令用于查询指定UPF组的DNS属性和DNS64属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD UEDNSUPGROUP命令生成。 |
| APNTYPE | APN类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL_APN（所有APN）<br>- APN_GROUP（APN组）<br>- SPECIAL_APN（指定APN）<br>默认值：无<br>配置原则：<br>优先级从高到低：“SPECIAL_APN”、“APN_GROUP”、“ALL_APN”。 |
| APNGRPNAME | APN组名 | 可选必选说明：该参数在"APNTYPE"配置为"APN_GROUP"时为条件可选参数。<br>参数含义：该参数用于指定APN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：<br>该参数使用ADD SMFAPNGRP命令配置生成。<br>该参数在“APNTYPE”参数配置为“APN_GROUP”后生效。 |
| APN | APN名称 | 可选必选说明：该参数在"APNTYPE"配置为"SPECIAL_APN"时为条件可选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。<br>该参数在“APNTYPE”参数配置为“SPECIAL_APN”后生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UEDNSBINDUPGRP]] · UPF组的DNS属性（UEDNSBINDUPGRP）

## 使用实例

查询UPF组upfgrp1的DNS属性和DNS64属性：

```
LST UEDNSBINDUPGRP: UPFGRPNAME="upfgrp1";
RETCODE = 0  操作成功。

结果如下
----------------
                UPF组名称  =  upfgrp1
        IPv4主DNS服务器IP  =  10.1.1.1
        IPv4备DNS服务器IP  =  10.2.2.2
IPv4 第一优先级服务器属性  =  dhcp
IPv4 第二优先级服务器属性  =  radius
        IPv6主DNS服务器IP  =  2001:0DB8:0:1::
        IPv6备DNS服务器IP  =  2001:0DB8:0:2::
IPv6 第一优先级服务器属性  =  dhcp
IPv6 第二优先级服务器属性  =  radius
      IPv6主DNS64服务器IP  =  2001:0DB8:0:3::
      IPv6备DNS64服务器IP  =  2001:0DB8:0:4::
 IPv4第三优先级服务器属性  =  local
IPv4 第四优先级服务器属性  =  pcrf
IPv6 第三优先级服务器属性  =  local
IPv6 第四优先级服务器属性  =  pcrf
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UEDNSBINDUPGRP.md`
