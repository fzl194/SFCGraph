---
id: UNC@20.15.2@MMLCommand@LST APNNBNS
type: MMLCommand
name: LST APNNBNS（查询APN的NBNS属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNNBNS
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- NBNS选择管理
- APN的NBNS属性
status: active
---

# LST APNNBNS（查询APN的NBNS属性）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用来查看指定APN实例的NBNS属性信息。如果指定可选参数APN，则该命令将显示该APN下NBNS属性信息，否则该命令将显示所有APN实例的NBNS属性信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNNBNS]] · APN的NBNS属性（APNNBNS）

## 使用实例

查询APN为“huawei.com”的NBNS属性：

```
%%LST APNNBNS: APN="huawei.com";%%
RETCODE = 0  操作成功

结果如下
--------
   APN名称  =  huawei.com
    主NBNS  =  10.1.1.1
    备NBNS  =  10.2.2.2
第一优先级  =  dhcp
第二优先级  =  radius
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNNBNS.md`
