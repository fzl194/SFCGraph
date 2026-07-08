---
id: UNC@20.15.2@MMLCommand@ADD NGUSRGRP
type: MMLCommand
name: ADD NGUSRGRP（增加5G用户群）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NGUSRGRP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- 用户群组标识管理
status: active
---

# ADD NGUSRGRP（增加5G用户群）

## 功能

**适用NF：AMF**

此命令用于增加5G用户群记录，同一个用户群中的用户具有相同的策略。

当将需要采用相同策略的不同的IMSI号段用户进行划分，作为一个用户群统一进行控制时，需要执行此命令。

群组内的用户标识列表通过ADD NGUSRGRPMEM进行添加。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRGRPID | 用户群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G用户群标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数表示用户群标识的描述信息，在运维过程中起到助记的作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGUSRGRP]] · 5G用户群（NGUSRGRP）

## 使用实例

增加一条5G用户群管理记录，用户群标识为20，执行如下命令：

```
ADD NGUSRGRP: USRGRPID=20;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NGUSRGRP.md`
