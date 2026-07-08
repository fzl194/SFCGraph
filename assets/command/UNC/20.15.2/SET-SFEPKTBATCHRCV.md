---
id: UNC@20.15.2@MMLCommand@SET SFEPKTBATCHRCV
type: MMLCommand
name: SET SFEPKTBATCHRCV（设置SFE批量收取的报文数量）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SFEPKTBATCHRCV
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE批量收取报文数量
status: active
---

# SET SFEPKTBATCHRCV（设置SFE批量收取的报文数量）

## 功能

![](设置SFE批量收取的报文数量（SET SFEPKTBATCHRCV）_40875977.assets/notice_3.0-zh-cn_2.png)

如果设置的批量收取的报文数量不合理，可能会导致VNRS侧转发性能下降。

该命令用来设置SFE批量收取的报文数量。

## 注意事项

- 该命令仅适用于非池化场景。
- 该命令存在系统初始记录，参数的初始设置值如下表：
  | PKTNUM |
  | --- |
  | 128 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PKTNUM | 批量收取报文数量 | 可选必选说明：必选参数<br>参数含义：该参数用于表示SFE批量收取的报文数量信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SFEPKTBATCHRCV]] · SFE批量收取的报文数量（SFEPKTBATCHRCV）

## 使用实例

```
设置SFE批量收取的报文数量为16：
SET SFEPKTBATCHRCV: PKTNUM=16;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SFEPKTBATCHRCV.md`
