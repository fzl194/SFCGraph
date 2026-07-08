---
id: UDG@20.15.2@MMLCommand@ADD DFSRPAIRMEM
type: MMLCommand
name: ADD DFSRPAIRMEM（增加双发选收结对成员配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: DFSRPAIRMEM
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 4096
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN双发选收配置
- 双发选收结对成员配置
status: active
---

# ADD DFSRPAIRMEM（增加双发选收结对成员配置）

## 功能

**适用NF：UPF**

该命令用于新增双发选收结对成员IMSI。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4096。
- 双发选收结对存在。
- 双发选收结对下成员数量最多2个。
- 如果此IMSI以IMSI方式配置在ADD MULTICASTSOURCE中，那么IMSI就不能配置为结对成员。
- IMSI绑定到双发选收结对时，如果结对已经绑定到了静态组播组，且绑定到双发选收结对中的IMSI和静态组播组中已绑定的IMSI重复，绑定失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DFSRPAIRID | 双发选收结对ID | 可选必选说明：必选参数<br>参数含义：该参数用于配置双发选收结对ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1-2048。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：双发选收结对成员IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15，每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DFSRPAIRMEM]] · 双发选收结对成员配置（DFSRPAIRMEM）

## 使用实例

向双发选收结对1中添加结对成员，imsi为460111111111111：

```
ADD DFSRPAIRMEM: DFSRPAIRID=1, IMSI="460111111111111";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加双发选收结对成员配置（ADD-DFSRPAIRMEM）_26352685.md`
