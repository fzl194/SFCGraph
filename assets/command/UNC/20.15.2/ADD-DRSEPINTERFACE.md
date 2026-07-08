---
id: UNC@20.15.2@MMLCommand@ADD DRSEPINTERFACE
type: MMLCommand
name: ADD DRSEPINTERFACE（增加接口故障隔离）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DRSEPINTERFACE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# ADD DRSEPINTERFACE（增加接口故障隔离）

## 功能

该命令用于在免交换组网下组成热备容灾关系的网元间DCI通道变化时，添加需要关闭/开启的逻辑接口。

## 注意事项

- 该命令执行后立即生效。

- 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。
- 该命令执行时，请确保配置接口名称正确。如果配置错误，请先执行[**RMV DRSEPINTERFACE**](删除故障隔离接口（RMV DRSEPINTERFACE）_35390226.md)命令，再执行此命令添加正确的接口。

- 最多可输入65535条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRGROUPID | 容灾组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于配置容灾组标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：无 |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于配置接口名称。可通过<br>[**LST DRSEPINTERFACE**](查询快速隔离接口（LST DRSEPINTERFACE）_86255389.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DRSEPINTERFACE]] · 故障隔离接口（DRSEPINTERFACE）

## 使用实例

新增故障隔离接口。

```
ADD DRSEPINTERFACE: DRGROUPID=1, IFNAME="itf1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DRSEPINTERFACE.md`
