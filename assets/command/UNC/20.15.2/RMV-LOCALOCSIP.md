---
id: UNC@20.15.2@MMLCommand@RMV LOCALOCSIP
type: MMLCommand
name: RMV LOCALOCSIP（删除本省OCS的IP号段）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LOCALOCSIP
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 本省OCS的IP号段
status: active
---

# RMV LOCALOCSIP（删除本省OCS的IP号段）

## 功能

![](删除本省OCS的IP号段（RMV LOCALOCSIP）_45110932.assets/notice_3.0-zh-cn_2.png)

该命令用于删除指定本省OCS的IP号段。若删除，在有SCP组网条件下可能导致话单处理流程异常。

**适用NF：NCG**

该命令用于删除本省OCS的IP号段。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSID | OCS标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定OCS标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。只允许输入字母，数字和中划线。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [本省OCS的IP号段（LOCALOCSIP）](configobject/UNC/20.15.2/LOCALOCSIP.md)

## 使用实例

删除OCS标识为“ocsid001”的本省OCS的IP号段：

```
RMV LOCALOCSIP:OCSID="ocsid001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除本省OCS的IP号段（RMV-LOCALOCSIP）_45110932.md`
