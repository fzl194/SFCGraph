---
id: UNC@20.15.2@MMLCommand@RMV IMSIBINDUP
type: MMLCommand
name: RMV IMSIBINDUP（删除用户和UPF的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IMSIBINDUP
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 用户绑定UPF
status: active
---

# RMV IMSIBINDUP（删除用户和UPF的绑定关系）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于删除用户和UPF的绑定关系，支持删除一个用户和UPF的绑定，也支持删除连续IMSI号段的用户和UPF的绑定。

## 注意事项

如果REDIRECT属性为DISABLE，则只在会话建立流程有效；如果REDIRECT属性为ENABLE，则在会话建立和切换流程同时有效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 起始IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI号段的起始IMSI，当只有一个IMSI时，起始IMSI和末位IMSI相同。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~15。IMSI参数每一位只能是数字0-9；当IMSI长度不足15位时，会自动低位补0直到15位。<br>默认值：无<br>配置原则：无 |
| ACCESSTYPE | 接入类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的接入类型。<br>数据来源：本端规划<br>取值范围：<br>- GUL（2/3/4G接入）<br>- NG（5G接入）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSIBINDUP]] · 用户和UPF的绑定关系（IMSIBINDUP）

## 使用实例

删除用户“111111”在5G的UP绑定关系：

```
RMV IMSIBINDUP: IMSI="111111", ACCESSTYPE=NG;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IMSIBINDUP.md`
