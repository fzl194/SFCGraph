---
id: UDG@20.15.2@MMLCommand@RMV SNSSAIBWMUSRG
type: MMLCommand
name: RMV SNSSAIBWMUSRG（删除带宽管理用户组切片绑定）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SNSSAIBWMUSRG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 带宽管理用户切片绑定
status: active
---

# RMV SNSSAIBWMUSRG（删除带宽管理用户组切片绑定）

## 功能

**适用NF：PGW-U、UPF**

该命令用于将某个切片用户从一个带宽管理用户组中删除。当运营商希望不对特定切片下的用户进行带宽控制时，需要删除该切片与带宽管理用户组的绑定关系。

## 注意事项

删除一个切片和某带宽管理用户组的绑定，用户更新可以触发该删除的配置对该用户组已在线的用户生效，否则对该用户组已在线用户不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERGROUPNAME | 用户组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要被切片绑定的带宽管理用户组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SST | 切片/服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用来设置切片/服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无<br>配置原则：无 |
| SD | 切片区分码 | 可选必选说明：可选参数<br>参数含义：该参数用来指定切片区分码。<br>数据来源：全网规划<br>取值范围：字符串类型，每个字符必须为0~9的数字或a~f/A-F的字母。<br>默认值：无<br>配置原则：该参数必须是长度为6的字符串。如S-NSSAI无SD，SD需配置为全F。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SNSSAIBWMUSRG]] · 带宽管理用户组切片绑定（SNSSAIBWMUSRG）

## 使用实例

假如运营商希望删除名为“test”的用户组和切片名称为123456切片的绑定：

```
RMV SNSSAIBWMUSRG: USERGROUPNAME="test", SST=1, SD="123456";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除带宽管理用户组切片绑定（RMV-SNSSAIBWMUSRG）_04649171.md`
