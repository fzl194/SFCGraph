---
id: UNC@20.15.2@MMLCommand@RMV AGFCDRCHLMAP
type: MMLCommand
name: RMV AGFCDRCHLMAP（删除话单通道一级目录映射表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AGFCDRCHLMAP
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 话单通道映射表
status: active
---

# RMV AGFCDRCHLMAP（删除话单通道一级目录映射表）

## 功能

**适用NF：NCG**

该命令用于删除OCS NFINSTANCEID与话单通道一级目录映射关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | OCS的NFINSTANCEID值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定OCS的NFINSTANCEID值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。NFINSTANCEID必须来源于PNFPROFILE命令中NFINSTANCEID参数。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AGFCDRCHLMAP]] · 话单通道一级目录映射表（AGFCDRCHLMAP）

## 使用实例

删除NFINSTANCEID为"00000000-0000-0000-c000-000000000046"的话单通道一级目录映射关系：

```
RMV AGFCDRCHLMAP: NFINSTANCEID="00000000-0000-0000-c000-000000000046";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-AGFCDRCHLMAP.md`
