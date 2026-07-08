---
id: UDG@20.15.2@MMLCommand@ADD TACGROUP
type: MMLCommand
name: ADD TACGROUP（添加一个新的TAC组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: TACGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 6000
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- TAC组
status: active
---

# ADD TACGROUP（添加一个新的TAC组）

## 功能

**适用NF：PGW-U、UPF**

该命令用来添加TAC组，当需要使用本地配置的TAC组时，使用此命令。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为6000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | 指定TAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| TACTYPE | TAC 类型 | 可选必选说明：可选参数<br>参数含义：指定TAC类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- S1TAC：S1TAC。<br>- N2TAC：N2TAC。<br>默认值：S1TAC<br>配置原则：无 |

## 操作的配置对象

- [指定的TAC组（TACGROUP）](configobject/UDG/20.15.2/TACGROUP.md)

## 使用实例

假设运营商需要去添加一个新的TAC组beijing：

```
ADD TACGROUP:TACGROUPNAME="beijing";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加一个新的TAC组（ADD-TACGROUP）_82837201.md`
