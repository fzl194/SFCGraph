---
id: UNC@20.15.2@MMLCommand@RMV PSCSHSS
type: MMLCommand
name: RMV PSCSHSS（删除联合接入HSS白名单）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PSCSHSS
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

# RMV PSCSHSS（删除联合接入HSS白名单）

## 功能

**适用网元：MME**

该命令用于删除联合接入HSS白名单。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HSSHOST | HSS主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于标识HSS的主机名。<br>数据来源：全网规划<br>取值范围：1~127位字符串。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“.”，其他均为非法字符。<br>默认值：无<br>说明：参数“HSS主机名”大小写不敏感，录入后均转换成大写字母存储和使用。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PSCSHSS]] · 联合接入HSS白名单（PSCSHSS）

## 使用实例

删除主机名为HUAWEI的联合接入HSS白名单:

```
RMV PSCSHSS: HSSHOST="HUAWEI";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除联合接入HSS白名单(RMV-PSCSHSS)_86553345.md`
