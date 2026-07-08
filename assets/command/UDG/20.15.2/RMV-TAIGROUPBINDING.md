---
id: UDG@20.15.2@MMLCommand@RMV TAIGROUPBINDING
type: MMLCommand
name: RMV TAIGROUPBINDING（删除TAC号段与TAI组的绑定关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TAIGROUPBINDING
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- TAI组与TAI号段绑定关系
status: active
---

# RMV TAIGROUPBINDING（删除TAC号段与TAI组的绑定关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除TAC号段与TAI组的绑定关系。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAIGROUPNAME | 指定TAI组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAI组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD TAIGROUP命令配置生成。 |
| TACSECNUM | TAC 段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～2999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [TAC号段与TAI组的绑定关系（TAIGROUPBINDING）](configobject/UDG/20.15.2/TAIGROUPBINDING.md)

## 使用实例

假设运营商需要在一个本地已经配置的TAI组删除一个TAC号段：

```
RMV TAIGROUPBINDING: TAIGROUPNAME="beijing", TACSECNUM=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除TAC号段与TAI组的绑定关系（RMV-TAIGROUPBINDING）_25926887.md`
