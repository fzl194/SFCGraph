---
id: UDG@20.15.2@MMLCommand@ADD PORTGROUPMEMBER
type: MMLCommand
name: ADD PORTGROUPMEMBER（增加端口组成员）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: PORTGROUPMEMBER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 端口组
status: active
---

# ADD PORTGROUPMEMBER（增加端口组成员）

## 功能

该命令用于增加端口组成员，通过命令ADD PORTGROUP创建端口组后，端口组中并不包含任何成员接口，此时，可以通过该命令向端口组中添加接口，这样在进行端口组的配置时，系统才会自动到端口组绑定的所有成员接口下，完成接口批量配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 增加端口组成员时，必须先配置所在的端口组。
- 批量添加时，成员接口类型要一致。
- 批量添加时，结束接口的名称排序需要在起始接口后。
- 该命令只支持添加Loopback口。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PORTGROUPNAME | 端口组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示端口组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32；字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |
| MEMBERIFNAME | 端口组成员名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示端口组成员的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| ENDIFNAME | 批量添加时，结束的端口组成员名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示批量添加时结束的端口组成员的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [端口组成员（PORTGROUPMEMBER）](configobject/UDG/20.15.2/PORTGROUPMEMBER.md)

## 使用实例

批量增加端口组ifm的成员：

```
ADD PORTGROUPMEMBER:PORTGROUPNAME="ifm",MEMBERIFNAME="Loopback1",ENDIFNAME="Loopback4";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加端口组成员（ADD-PORTGROUPMEMBER）_00866713.md`
