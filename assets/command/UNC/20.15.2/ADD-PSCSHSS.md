---
id: UNC@20.15.2@MMLCommand@ADD PSCSHSS
type: MMLCommand
name: ADD PSCSHSS（增加联合接入HSS白名单）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PSCSHSS
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- 联合接入管理
status: active
---

# ADD PSCSHSS（增加联合接入HSS白名单）

## 功能

**适用网元：MME**

该命令用于增加联合接入HSS白名单。当 [SET PSCSPLCY](设置联合接入策略(SET PSCSPLCY)_31833948.md) 中SUBPLCY参数设置为HSS_IDENT时需要通过本命令添加白名单中的用户。

## 注意事项

- 本表最大记录数为2048条。
- 当[SET PSCSPLCY](设置联合接入策略(SET PSCSPLCY)_31833948.md)中SUBPLCY参数设置为HSS_IDENT时生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HSSHOST | HSS主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于标识HSS的主机名。<br>数据来源：全网规划<br>取值范围：1~127位字符串。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“.”，其他均为非法字符。<br>默认值：无<br>说明：参数“HSS主机名”大小写不敏感，录入后均转换成大写字母存储和使用。 |

## 操作的配置对象

- [联合接入HSS白名单（PSCSHSS）](configobject/UNC/20.15.2/PSCSHSS.md)

## 使用实例

增加主机名为HUAWEI的联合接入HSS白名单:

```
ADD PSCSHSS: HSSHOST="HUAWEI";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加联合接入HSS白名单(ADD-PSCSHSS)_35873478.md`
