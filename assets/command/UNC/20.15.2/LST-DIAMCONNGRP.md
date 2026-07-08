---
id: UNC@20.15.2@MMLCommand@LST DIAMCONNGRP
type: MMLCommand
name: LST DIAMCONNGRP（查询Diameter链路组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DIAMCONNGRP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- Diameter链路组
status: active
---

# LST DIAMCONNGRP（查询Diameter链路组）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询所有Diameter链路组配置信息，或者查询指定名称、本端主机名或对端主机名的Diameter链路组配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONNGROUPNAME | Diameter链路组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCALHOSTNAME | 本端主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组的本端主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD DIAMLOCINFO命令配置生成。 |
| PEERHOSTNAME | 对端主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组的对端主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD PCRF、ADD OCS、ADD DIAMETERAAA或ADD DRA命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIAMCONNGRP]] · Diameter链路组（DIAMCONNGRP）

## 使用实例

查询diameter链路组gxconngrp的配置信息：

```
LST DIAMCONNGRP:CONNGROUPNAME="gxconngrp";
```

```

RETCODE = 0  操作成功

Diameter链路组
--------------
Diameter链路组名  =  gxconngrp
      本端主机名  =  gxlocalhost
      对端主机名  =  pcrfhost
    Diameter应用  =  Gx应用
    链路选择模式  =  基于会话（Session-id）轮询
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DIAMCONNGRP.md`
