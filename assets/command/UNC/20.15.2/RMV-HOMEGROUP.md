---
id: UNC@20.15.2@MMLCommand@RMV HOMEGROUP
type: MMLCommand
name: RMV HOMEGROUP（删除Home Group）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: HOMEGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- Home Group
status: active
---

# RMV HOMEGROUP（删除Home Group）

## 功能

![](删除Home Group（RMV HOMEGROUP）_88733227.assets/notice_3.0-zh-cn_2.png)

执行不当会导致系统异常。

**适用NF：PGW-C、GGSN**

该命令用于删除Home Group配置。

## 注意事项

- 该命令执行后立即生效。

- HOEMNGROUPINDX不输入时表示删除所有的记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOMEGROUPINDX | Home Group编号 | 可选必选说明：必选参数<br>参数含义：该参数用于设置Home Group的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HOMEGROUP]] · Home Group（HOMEGROUP）

## 使用实例

删除“Home Group编号”为“2”的Home Group配置：

```
RMV HOMEGROUP: HOMEGROUPINDX=2, CONFIRM=Y;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-HOMEGROUP.md`
