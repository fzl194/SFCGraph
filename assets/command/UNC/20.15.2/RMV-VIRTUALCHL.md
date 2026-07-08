---
id: UNC@20.15.2@MMLCommand@RMV VIRTUALCHL
type: MMLCommand
name: RMV VIRTUALCHL（删除虚拟通道映射）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: VIRTUALCHL
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 虚拟通道映射
status: active
---

# RMV VIRTUALCHL（删除虚拟通道映射）

## 功能

![](删除虚拟通道映射（RMV VIRTUALCHL）_21982309.assets/notice_3.0-zh-cn_2.png)

删除虚拟通道映射会导致话单备份分发到源通道。

**适用NF：NCG**

该命令用于删除虚拟通道映射。

## 注意事项

- 该命令执行后立即生效。
- 删除虚拟通道后，本地备份和本地分发的目的路径的虚拟通道目录下如果存在话单文件，不会自动删除，会占用NCG的磁盘空间。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SOURCECHL | 源通道名称 | 可选必选说明：必选参数<br>参数含义：需要映射的通道名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| AGID | 接入网元分组标识 | 可选必选说明：必选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VIRTUALCHL]] · 虚拟通道映射（VIRTUALCHL）

## 使用实例

删除接入分组PS1的"98/OFFLINE"通道的虚拟通道映射，配置举例如下：

```
RMV VIRTUALCHL: SOURCECHL="98/OFFLINE", AGID="PS1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除虚拟通道映射（RMV-VIRTUALCHL）_21982309.md`
