---
id: UNC@20.15.2@MMLCommand@RMV CDRBACKUP
type: MMLCommand
name: RMV CDRBACKUP（删除话单备份）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CDRBACKUP
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
- 话单备份
status: active
---

# RMV CDRBACKUP（删除话单备份）

## 功能

![](删除话单备份（RMV CDRBACKUP）_51174245.assets/notice_3.0-zh-cn_2.png)

删除话单备份会导致话单不能传送到第三方服务器。

**适用NF：NCG**

该命令用于删除已添加的话单备份任务。

执行任务之前，可执行 [**LST CDRBACKUP**](查询话单备份（LST CDRBACKUP）_51174247.md) 查询当前系统中需要删除的话单备份任务情况，找到对应的备份任务标识。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BACKUPID | 备份任务标识 | 可选必选说明：必选参数<br>参数含义：备份任务标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [上传SFTP密钥文件到第三方服务器（CDRBACKUP）](configobject/UNC/20.15.2/CDRBACKUP.md)

## 使用实例

删除话单标识为“1st_cdr_backup”的话单备份任务，示例如下：

```
RMV CDRBACKUP: BACKUPID="1st_cdr_backup";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除话单备份（RMV-CDRBACKUP）_51174245.md`
