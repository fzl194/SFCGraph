---
id: UNC@20.15.2@MMLCommand@LST ADDRPOOLGRP
type: MMLCommand
name: LST ADDRPOOLGRP（查询地址池组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ADDRPOOLGRP
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
- UE地址管理
- UE地址池管理
- 地址池组管理
status: active
---

# LST ADDRPOOLGRP（查询地址池组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询所有地址池组的信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGRPNAME | 地址池组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址池组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ADDRPOOLGRP]] · 地址池组（ADDRPOOLGRP）

## 使用实例

查询所有地址池组的信息：

```
LST ADDRPOOLGRP:;
RETCODE = 0  操作成功。

结果如下
------------------------
                    地址池组名称  =  spoolgrp1
                    地址池组类型  =  UDM
IPv4基于地址池优先级分配地址算法  =  去使能
IPv6基于地址池优先级分配地址算法  =  去使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ADDRPOOLGRP.md`
