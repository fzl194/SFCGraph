---
id: UNC@20.15.2@MMLCommand@RMV CDRMONITOR
type: MMLCommand
name: RMV CDRMONITOR（删除话单监控）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CDRMONITOR
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
- 话单监控
status: active
---

# RMV CDRMONITOR（删除话单监控）

## 功能

![](删除话单监控（RMV CDRMONITOR）_51174260.assets/notice_3.0-zh-cn_2.png)

删除话单监控任务会导致话单采集提醒功能失效。

**适用NF：NCG**

该命令用于删除长时间未取话单监控任务。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MONITORID | 话单监控标识 | 可选必选说明：必选参数<br>参数含义：监控任务标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRMONITOR]] · 话单监控（CDRMONITOR）

## 使用实例

删除一个非自定义目录的话单监控任务示例：

```
RMV CDRMONITOR: MONITORID="MON_1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CDRMONITOR.md`
