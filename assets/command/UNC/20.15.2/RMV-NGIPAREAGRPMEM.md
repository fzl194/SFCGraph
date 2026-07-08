---
id: UNC@20.15.2@MMLCommand@RMV NGIPAREAGRPMEM
type: MMLCommand
name: RMV NGIPAREAGRPMEM（删除5G IP区域群成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGIPAREAGRPMEM
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- IP细分管理
- 5G IP细分区域组成员管理
status: active
---

# RMV NGIPAREAGRPMEM（删除5G IP区域群成员）

## 功能

**适用NF：AMF**

该命令用于删除5G IP区域群成员。

## 注意事项

命令执行后只对新接入用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域群标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定区域群标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~64。此AREAID要与NGIPAREAGRP中的AREAID保持一致，受NGIPAREAGRP中的IPAREASW开关控制。<br>默认值：无<br>配置原则：无 |
| TAC | 跟踪区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区域码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGIPAREAGRPMEM]] · 5G IP区域群成员（NGIPAREAGRPMEM）

## 使用实例

删除一条IP区域群成员记录，区域群标识为SomeCity，跟踪区域码为0x123456，执行如下命令：

```
RMV NGIPAREAGRPMEM: AREAID="SomeCity", TAC="123456";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGIPAREAGRPMEM.md`
