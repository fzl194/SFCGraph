---
id: UNC@20.15.2@MMLCommand@LST IMSIAPNBINDUP
type: MMLCommand
name: LST IMSIAPNBINDUP（查询APN下用户和UPF的绑定关系配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSIAPNBINDUP
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 用户APN绑定UPF
status: active
---

# LST IMSIAPNBINDUP（查询APN下用户和UPF的绑定关系配置）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于查询APN下用户和UPF的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 起始IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI号段的起始IMSI，当ENDIMSI没有值时，起始IMSI和终止IMSI相同。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。该参数每一位只能是数字0-9。<br>默认值：无<br>配置原则：无 |
| ACCESSTYPE | 接入类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的接入类型。<br>数据来源：本端规划<br>取值范围：<br>- GUL（2/3/4G接入）<br>- NG（5G接入）<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入APN需要在ADD APN命令中配置。<br>输入的APN名称需要符合APN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSIAPNBINDUP]] · APN下用户和UPF的绑定关系配置（IMSIAPNBINDUP）

## 使用实例

显示所有用户UPF的绑定关系： LST IMSIAPNBINDUP:;

```
%%LST IMSIAPNBINDUP:;%%
RETCODE = 0  操作成功。

结果如下
------------------------
起始IMSI         终止IMSI           接入类型  APN            主锚点UPF实例名称    N3/S1-U口UPF实例名称   辅锚点UPF实例名称  ULCL部署模式      

111111000000000  111111999999999    5G接入    huawei.com     up1                  up2                   up3               优先使用辅锚点分流
211111000000000  211119999999999    5G接入    huawei.com     up1                  up2                   up3               只使用主锚点分流  
(结果个数 = 2)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN下用户和UPF的绑定关系配置（LST-IMSIAPNBINDUP）_75982844.md`
