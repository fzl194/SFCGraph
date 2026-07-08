---
id: UDG@20.15.2@MMLCommand@LST UPDIAMCONNGRP
type: MMLCommand
name: LST UPDIAMCONNGRP（查询Diameter链路组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPDIAMCONNGRP
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter管理
- Diameter连接
- Diameter链路组
status: active
---

# LST UPDIAMCONNGRP（查询Diameter链路组）

## 功能

**适用NF：UPF**

该命令用于查询所有Diameter链路组配置信息，或者查询指定名称、本端主机名或对端主机名的Diameter链路组配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONNGROUPNAME | Diameter链路组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCALHOSTNAME | 本端主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组的本端主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMLOCINFO命令配置生成。 |
| PEERHOSTNAME | 对端主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组的对端主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMETERAAA或ADD UPDRA命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMCONNGRP]] · Diameter链路组（UPDIAMCONNGRP）

## 使用实例

查询diameter链路组swmconngrp的配置信息：

```
LST UPDIAMCONNGRP:CONNGROUPNAME="swmconngrp";
```

```

RETCODE = 0  操作成功
Diameter链路组
--------------
Diameter链路组名  =  swmconngrp
      本端主机名  =  swmlocalhost
      对端主机名  =  drahost
    Diameter应用  =  SWM
    链路选择模式  =  基于会话（Session-id）轮询
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Diameter链路组（LST-UPDIAMCONNGRP）_45432690.md`
