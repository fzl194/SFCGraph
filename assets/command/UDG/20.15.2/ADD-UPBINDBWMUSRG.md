---
id: UDG@20.15.2@MMLCommand@ADD UPBINDBWMUSRG
type: MMLCommand
name: ADD UPBINDBWMUSRG（增加带宽管理用户组User Profile绑定）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPBINDBWMUSRG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 31984
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 带宽管理用户组用户模板绑定
status: active
---

# ADD UPBINDBWMUSRG（增加带宽管理用户组User Profile绑定）

## 功能

**适用NF：PGW-U、UPF**

该命令用于将绑定某个UserProfile的用户加入一个带宽管理用户组。当运营商希望对特定UserProfile下的用户进行带宽控制时，需要将该UserProfile绑定到包含带宽控制策略的用户组下，该命令就是完成绑定的功能。

## 注意事项

- 该命令最大记录数为31984。当配置记录数大于规格的90%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格90%时，恢复“ALM-135602215 配置数量超阈值”告警。阈值可以通过MOD CFGTHRESHOLD命令修改。
- 一个用户组下包含的APN、UserProfile和切片的数量总和最大值为16。
- 绑定一个UserProfile到某带宽管理用户组，用户更新可以触发该配置对该用户组已在线的用户生效，否则对该用户组已在线用户不生效。
- 绑定UserProfile的带宽管理用户组不能是默认、或者全局用户组。
- 绑定到用户组下的UserProfile必须已经配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERGROUPNAME | 用户组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要被用户模板绑定的带宽管理用户组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD BWMUSERGROUP命令配置生成。 |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要绑定的用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPBINDBWMUSRG]] · 带宽管理用户组User Profile绑定（UPBINDBWMUSRG）

## 使用实例

假如运营商希望在名为“testbwmusergroup”的用户组中，包含绑定“testuserprofile”的用户：

```
ADD UPBINDBWMUSRG:USERGROUPNAME="testbwmusergroup",USERPROFILENAME="testuserprofile";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加带宽管理用户组User-Profile绑定（ADD-UPBINDBWMUSRG）_82837491.md`
