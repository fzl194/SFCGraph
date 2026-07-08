---
id: UNC@20.15.2@MMLCommand@LST UEDNSBINDAPN
type: MMLCommand
name: LST UEDNSBINDAPN（查询APN的DNS属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UEDNSBINDAPN
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- DNS选择管理
- APN DNS域名策略
status: active
---

# LST UEDNSBINDAPN（查询APN的DNS属性）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用来查询指定APN实例的DNS属性信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UEDNSBINDAPN]] · APN的DNS属性（UEDNSBINDAPN）

## 使用实例

显示APN实例huawei.com的DNS配置：

```
LST UEDNSBINDAPN: APN="huawei.com";
RETCODE = 0  操作成功。

APN的DNS配置信息
----------------
                  APN名称  =  huawei.com
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

- 原始手册：`evidence/UNC/20.15.2/查询APN的DNS属性（LST-UEDNSBINDAPN）_09652680.md`
