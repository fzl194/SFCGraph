---
id: UDG@20.15.2@MMLCommand@ADD SNSSAIBWMUSRG
type: MMLCommand
name: ADD SNSSAIBWMUSRG（增加带宽管理用户组切片绑定）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SNSSAIBWMUSRG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
max_records: 31984
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 带宽管理用户切片绑定
status: active
---

# ADD SNSSAIBWMUSRG（增加带宽管理用户组切片绑定）

## 功能

**适用NF：PGW-U、UPF**

该命令用于将某个切片的用户加入一个带宽管理用户组。当运营商希望对特定切片下的用户进行带宽控制时，需要将该切片绑定到包含带宽控制策略的用户组下。

## 注意事项

- 该命令最大记录数为31984。
- 一个用户组下包含的APN、UserProfile和切片的数量总和最大值为16。
- 绑定一个切片到某带宽管理用户组，用户更新可以触发该配置对该用户组已在线的用户生效，否则对该用户组已在线用户不生效。
- 绑定切片的带宽管理用户组不能是默认、或者全局用户组。
- 绑定到用户组下的切片必须已经通过ADD SNSSAI命令配置。
- 如果切片绑定到多个BwmUserGroup，只有用户组优先级最高的会生效。
- 本命令属于高危命令，操作不当会导致性能下降明显，执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERGROUPNAME | 用户组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要被切片绑定的带宽管理用户组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD BWMUSERGROUP命令配置生成。 |
| SST | 切片/服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用来设置切片/服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无<br>配置原则：该参数使用ADD SNSSAI命令配置生成。 |
| SD | 切片区分码 | 可选必选说明：可选参数<br>参数含义：该参数用来指定切片区分码。<br>数据来源：全网规划<br>取值范围：字符串类型，每个字符必须为0~9的数字或a~f/A-F的字母。<br>默认值：无<br>配置原则：该参数必须是长度为6的字符串。如S-NSSAI无SD，SD需配置为全F。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SNSSAIBWMUSRG]] · 带宽管理用户组切片绑定（SNSSAIBWMUSRG）

## 使用实例

假如运营商希望在名为“test”的用户组中，包含切片名称为123456的用户：

```
ADD SNSSAIBWMUSRG: USERGROUPNAME="test", SST=1, SD="123456";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加带宽管理用户组切片绑定（ADD-SNSSAIBWMUSRG）_16930642.md`
