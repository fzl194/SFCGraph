---
id: UNC@20.15.2@MMLCommand@RMV PSCSIMSI
type: MMLCommand
name: RMV PSCSIMSI（删除联合接入IMSI白名单）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PSCSIMSI
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- 联合接入管理
status: active
---

# RMV PSCSIMSI（删除联合接入IMSI白名单）

## 功能

**适用网元：MME**

该命令用于删除联合接入IMSI白名单。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>数据来源：整网规划<br>取值范围：1~15位十进制数字<br>默认值：无<br>配置原则：IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PSCSIMSI]] · 联合接入IMSI白名单（PSCSIMSI）

## 使用实例

删除联合接入IMSI白名单：

```
RMV PSCSIMSI: IMSIPRE="12345";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除联合接入IMSI白名单(RMV-PSCSIMSI)_86673117.md`
