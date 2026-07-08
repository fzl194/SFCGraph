---
id: UNC@20.15.2@MMLCommand@SET CHARGECHARCHK
type: MMLCommand
name: SET CHARGECHARCHK（设置是否检查Serving Node携带的CC）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CHARGECHARCHK
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 计费参数
status: active
---

# SET CHARGECHARCHK（设置是否检查Serving Node携带的CC）

## 功能

**适用NF：PGW-C、SMF**

该命令用于设置是否检查Serving Node携带的charge-characteristic。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 本地用户：指本PLMN网络上签约，未漫游到其他PLMN且在本UNC激活的用户。
- 漫游用户：指本PLMN网络上签约，漫游到其他PLMN且仍在本UNC激活的用户。
- 拜访用户：指其他PLMN网络上签约，漫游到本PLMN内使用本UNC激活的用户。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CHARGECHARCHK |
| --- | --- |
| 初始值 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHARGECHARCHK | 检查Serving Node携带的charge-characteristic | 可选必选说明：可选参数<br>参数含义：设置是否检查Serving Node携带的对本地用户、漫游用户、拜访用户所采用的计费属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：是。<br>- DISABLE：否。<br>默认值：无<br>配置原则：<br>- DISABLE：直接使用Serving Node携带的charge-characteristic。<br>- ENABLE：检查Serving Node携带的charge-characteristic的第一个字节的低4bit是不是1、2、4、8这4个值中的一个。如果是则使用Serving Node携带的charge-characteristic，并将协商的cc值高4位置0；如果不是，则使用本地配置的charge-characteristic。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHARGECHARCHK]] · 是否检查Serving Node携带的CC（CHARGECHARCHK）

## 使用实例

设置检查Serving Node携带的对本地用户、漫游用户、拜访用户所采用的计费属性：

```
SET CHARGECHARCHK:CHARGECHARCHK=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CHARGECHARCHK.md`
