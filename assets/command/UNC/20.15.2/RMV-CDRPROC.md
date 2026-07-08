---
id: UNC@20.15.2@MMLCommand@RMV CDRPROC
type: MMLCommand
name: RMV CDRPROC（删除话单处理）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CDRPROC
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
- 话单处理
status: active
---

# RMV CDRPROC（删除话单处理）

## 功能

![](删除话单处理（RMV CDRPROC）_51174273.assets/notice_3.0-zh-cn_2.png)

此命令不能动态生效，需要执行“RST VNFC”重启服务，并且删除话单处理可能导致话单业务不可用。

**适用NF：NCG**

该命令用于删除CG的话单处理规则。

## 注意事项

- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”命令重新启动系统才能生效。
- 该操作为危险操作，如果执行删除操作成功，会导致NCG整个系统瘫痪。
- 在执行删除操作之前，需确保CG所有的第二份最终话单已取走。
- 如果是配置了错误的格式引擎包，请不要执行删除话单处理操作。请执行[**MOD CDRPROC**](修改话单处理（MOD CDRPROC）_51174274.md)修改格式引擎包。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AGID | 接入网元分组标识 | 可选必选说明：必选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRPROC]] · 话单处理（CDRPROC）

## 使用实例

删除CG话单处理采用的格式引擎包，配置举例如下：

```
RMV CDRPROC: AGID="PS_GROUP_1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除话单处理（RMV-CDRPROC）_51174273.md`
