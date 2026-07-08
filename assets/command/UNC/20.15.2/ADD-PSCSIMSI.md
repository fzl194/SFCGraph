---
id: UNC@20.15.2@MMLCommand@ADD PSCSIMSI
type: MMLCommand
name: ADD PSCSIMSI（增加联合接入IMSI白名单）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PSCSIMSI
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
max_records: 100
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- 联合接入管理
status: active
---

# ADD PSCSIMSI（增加联合接入IMSI白名单）

## 功能

**适用网元：MME**

该命令用于增加联合接入IMSI白名单。当 [SET PSCSPLCY](设置联合接入策略(SET PSCSPLCY)_31833948.md) 中SUBPLCY参数设置为IMSI_IDENT时需要通过本命令添加白名单中的用户。

## 注意事项

- 本表最大记录数为100条。
- 当[SET PSCSPLCY](设置联合接入策略(SET PSCSPLCY)_31833948.md)中SUBPLCY参数设置为IMSI_IDENT时生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>数据来源：整网规划<br>取值范围：1~15位十进制数字<br>默认值：无<br>配置原则：IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |

## 操作的配置对象

- [联合接入IMSI白名单（PSCSIMSI）](configobject/UNC/20.15.2/PSCSIMSI.md)

## 使用实例

增加联合接入IMSI白名单：

```
ADD PSCSIMSI: IMSIPRE="12345";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加联合接入IMSI白名单(ADD-PSCSIMSI)_36193194.md`
