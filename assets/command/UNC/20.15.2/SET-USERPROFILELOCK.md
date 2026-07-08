---
id: UNC@20.15.2@MMLCommand@SET USERPROFILELOCK
type: MMLCommand
name: SET USERPROFILELOCK（设置用户模板的锁定）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: USERPROFILELOCK
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板
status: active
---

# SET USERPROFILELOCK（设置用户模板的锁定）

## 功能

**适用NF：PGW-C、SMF**

该命令用于设置用户模板的锁定。当运营商需要按照用户模板去活用户时，需先锁定该用户模板。

## 注意事项

- 该命令执行后立即生效。
- 此命令用来设置UserProfile是否锁定，在锁定UserProfile后，禁止使用UserProfile。当需要按照UserProfile去活用户时，需先锁定该UserProfile。由ENABLE状态设置为DISABLE状态，需要判断是否已经将UserProfile下用户都去活成功，如果正在去活用户，则禁止修改。
- 对于每个UserProfile，初始的锁定标记为DISABLE。
- 该命令设定后的数据，需要通过LST USERPROFILE命令进行查看。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |
| LOCKFLAG | 锁定标记 | 可选必选说明：必选参数<br>参数含义：指定锁定标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：<br>- 如果运营商不希望按照用户模板去活用户时，则配置该参数为DISABLE。<br>- 如果运营商希望按照用户模板去活用户时，则配置该参数为ENABLE。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USERPROFILELOCK]] · 用户模板的锁定（USERPROFILELOCK）

## 使用实例

假如运营商需要锁定名称为“testuserprofilename”的用户模板：

```
SET USERPROFILELOCK:USERPROFILENAME="testuserprofilename",LOCKFLAG=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置用户模板的锁定（SET-USERPROFILELOCK）_09897208.md`
