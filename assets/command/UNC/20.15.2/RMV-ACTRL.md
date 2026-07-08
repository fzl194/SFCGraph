---
id: UNC@20.15.2@MMLCommand@RMV ACTRL
type: MMLCommand
name: RMV ACTRL（删除接入控制）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ACTRL
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 接入控制
status: active
---

# RMV ACTRL（删除接入控制）

## 功能

![](删除接入控制（RMV ACTRL）_51174233.assets/notice_3.0-zh-cn_2.png)

此命令不能动态生效，需要执行“RST VNFC”重启服务，并且删除接入控制可能导致话单业务不可用。

**适用NF：NCG**

该命令用于删除当前接入网元分组上已添加的用于接入控制模块的IP地址和端口号。

## 注意事项

- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”命令重新启动系统才能生效。
- 执行此命令删除IP地址及端口号属于危险操作，会导致NCG业务不可用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACID | 接入控制标识 | 可选必选说明：必选参数<br>参数含义：用于在NCG中定义一条接入控制的数据记录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ACTRL]] · 接入控制（ACTRL）

## 使用实例

如果已存在接入控制“ps_actrl”，删除该接入控制对象示例如下：

```
RMV ACTRL:ACID="ps_actrl";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ACTRL.md`
