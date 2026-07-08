---
id: UNC@20.15.2@MMLCommand@MOD PSAUPFBINDATSSS
type: MMLCommand
name: MOD PSAUPFBINDATSSS（修改PSA UPF和ATSSS UPF绑定关系中的ATSSS-UPF）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PSAUPFBINDATSSS
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- PSA绑定ATSSS
status: active
---

# MOD PSAUPFBINDATSSS（修改PSA UPF和ATSSS UPF绑定关系中的ATSSS-UPF）

## 功能

**适用NF：SMF**

该命令用于修改PSA UPF和ATSSS UPF绑定关系中的ATSSS UPF。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PSAUPFINSTNAME | PSA UPF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PSA UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要在ADD UPNODE中事先配置，可执行LST UPNODE进行查看。注意查询结果是“UPF功能”为None的“UPF实例名称”。 |
| ATSSSINSTNAME | ATSSS UPF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ATSSS UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要在ADD UPNODE中事先配置，可执行LST UPNODE进行查看。注意查询结果是“UPF功能”取值为ATSSS的“UPF实例名称”。 |

## 操作的配置对象

- [PSA UPF和ATSSS UPF绑定关系中的ATSSS-UPF（PSAUPFBINDATSSS）](configobject/UNC/20.15.2/PSAUPFBINDATSSS.md)

## 使用实例

假设执行此命令前已经使用ADD PSAUPFBINDATSSS添加了一条记录：PSA UPF实例名称为upf_none，ATSSS UPF实例名称为upf_atsss。现修改绑定关系中的ATSSS UPF实例名称为upf_atsss_1：

```
MOD PSAUPFBINDATSSS: PSAUPFINSTNAME="upf_none", ATSSSINSTNAME="upf_atsss_1";
%%MOD PSAUPFBINDATSSS: PSAUPFINSTNAME="upf_none", ATSSSINSTNAME="upf_atsss_1";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改PSA-UPF和ATSSS-UPF绑定关系中的ATSSS-UPF（MOD-PSAUPFBINDATSSS）_96242670.md`
