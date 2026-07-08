---
id: UNC@20.15.2@MMLCommand@ADD POOLBINDAPN
type: MMLCommand
name: ADD POOLBINDAPN（增加APN实例与地址池绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: POOLBINDAPN
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址池绑定APN
status: active
---

# ADD POOLBINDAPN（增加APN实例与地址池绑定关系）

## 功能

**适用NF：SMF**

该命令用来配置指定APN实例与地址池的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 如果关联的APN和ADDRPOOL都绑定了VPN实例，那么这两个实例需要一致。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN/DNN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址池优先级，值越小优先级越高。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~16。<br>默认值：16<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/POOLBINDAPN]] · APN实例与地址池绑定关系（POOLBINDAPN）

## 使用实例

增加APN与地址池的绑定，“APN”为“huawei.com”，“POOLNAME”为“lap”：

```
ADD POOLBINDAPN:APN="huawei.com",POOLNAME="lap";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加APN实例与地址池绑定关系（ADD-POOLBINDAPN）_09653789.md`
