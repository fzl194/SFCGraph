---
id: UNC@20.15.2@MMLCommand@ADD PORTGROUP
type: MMLCommand
name: ADD PORTGROUP（增加端口组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PORTGROUP
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

# ADD PORTGROUP（增加端口组）

## 功能

通常，设备的接口数比较多，并且很多接口具有相同的配置。如果对这些接口进行逐个配置，不但操作繁琐，而且容易输入错误。为解决此问题，可以通过该命创建一个端口组，然后将需要执行相同配置命令的接口加入到该端口组，在端口组视图下配置命令时，系统会自动到端口组绑定的所有成员接口下执行这些命令行，完成接口批量配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PORTGROUPNAME | 端口组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示端口组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32；字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PORTGROUP]] · 端口组（PORTGROUP）

## 使用实例

增加端口组ifm：

```
ADD PORTGROUP:PORTGROUPNAME="ifm";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PORTGROUP.md`
