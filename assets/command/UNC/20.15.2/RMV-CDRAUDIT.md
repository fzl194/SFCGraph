---
id: UNC@20.15.2@MMLCommand@RMV CDRAUDIT
type: MMLCommand
name: RMV CDRAUDIT（删除话单稽核）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CDRAUDIT
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
- 话单稽核
status: active
---

# RMV CDRAUDIT（删除话单稽核）

## 功能

![](删除话单稽核（RMV CDRAUDIT）_51174240.assets/notice_3.0-zh-cn_2.png)

删除话单稽核任务会导致相应通道下的稽核文件无法生成，请慎重使用此命令。

**适用NF：NCG**

该命令用于删除某通道或者全部通道下第二份最终话单的稽核任务。

## 注意事项

- 该命令执行后立即生效。
- 系统运行过程中删除话单稽核任务属高危险操作，删除任务后，通道下不再生成对应的稽核文件。执行该命令后，如果相应通道下还有稽核任务，则第二天按照最终的配置生成正式稽核文件，否则，该通道下不会生成稽核文件。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDRAUDITID | 稽核任务标识 | 可选必选说明：必选参数<br>参数含义：稽核任务标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRAUDIT]] · 话单稽核（CDRAUDIT）

## 使用实例

删除“稽核任务标识”为“Audit_2nd”的话单稽核任务。示例如下：

```
RMV CDRAUDIT: CDRAUDITID="Audit_2nd";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除话单稽核（RMV-CDRAUDIT）_51174240.md`
