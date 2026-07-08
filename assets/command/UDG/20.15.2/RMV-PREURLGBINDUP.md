---
id: UDG@20.15.2@MMLCommand@RMV PREURLGBINDUP
type: MMLCommand
name: RMV PREURLGBINDUP（删除用户模板的前缀URL组绑定关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PREURLGBINDUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- Prefixed URL组绑定
status: active
---

# RMV PREURLGBINDUP（删除用户模板的前缀URL组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

![](删除用户模板的前缀URL组绑定关系（RMV PREURLGBINDUP）_82837412.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，可能会影响业务。

该命令用于删除用户模板与前缀URL组的绑定关系。

## 注意事项

- 本命令修改后对所有用户生效，大概五分钟之后生效。
- 如果不输入前缀URL组，则代表删除该UserProfile对应的所有前缀URL组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PREURLGRPNAME | 前缀URL组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定前缀URL组名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PREURLGBINDUP]] · 用户模板的前缀URL组绑定关系（PREURLGBINDUP）

## 使用实例

删除前缀URL组与UserProfile的绑定关系，USERPROFILENAME为“testprofile1”，PREURLGRPNAME为“testurlgroup”：

```
RMV PREURLGBINDUP:USERPROFILENAME="testprofile",PREURLGRPNAME="testurlgroup";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-PREURLGBINDUP.md`
