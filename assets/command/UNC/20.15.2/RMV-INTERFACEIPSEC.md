---
id: UNC@20.15.2@MMLCommand@RMV INTERFACEIPSEC
type: MMLCommand
name: RMV INTERFACEIPSEC（删除接口）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: INTERFACEIPSEC
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- 接口配置
status: active
---

# RMV INTERFACEIPSEC（删除接口）

## 功能

该命令用来删除已增加的逻辑接口并清除该接口的相关配置。逻辑接口是指能够实现数据交换功能但物理上不存在、需要通过配置建立的接口。

## 注意事项

- 该命令执行后立即生效。

- 为了保证该接口能够删除，必须确保该接口在设备上已经存在。
- 该命令在版本升级过程中禁止执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/INTERFACEIPSEC]] · 接口（INTERFACEIPSEC）

## 使用实例

删除逻辑接口LoopBack4：

```
RMV INTERFACEIPSEC: IFNAME="LoopBack4";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除接口（RMV-INTERFACEIPSEC）_80432536.md`
