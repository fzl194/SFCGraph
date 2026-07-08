---
id: UDG@20.15.2@MMLCommand@RMV CONTCATEGBIND
type: MMLCommand
name: RMV CONTCATEGBIND（删除内容分类组绑定关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CONTCATEGBIND
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容分类组绑定配置
status: active
---

# RMV CONTCATEGBIND（删除内容分类组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

![](删除内容分类组绑定关系（RMV CONTCATEGBIND）_43076793.assets/notice_3.0-zh-cn.png)

本命令属于高危命令,执行本命令后将删除指定内容过滤策略与指定内容分类组或所有内容分类组间的绑定关系，可能影响url过滤动作执行结果，请谨慎使用。

该命令用于删除内容分类组绑定关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFPROFILENAME | 内容过滤策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CFPROFILE命令配置生成。 |
| CONTCATEGNAME | 内容分类组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内容分类组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CONTCATEGROUP命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CONTCATEGBIND]] · 内容分类组绑定关系（CONTCATEGBIND）

## 使用实例

删除指定内容分类组绑定关系配置：

```
RMV CONTCATEGBIND: CFPROFILENAME="cf_profile1", CONTCATEGNAME="cf_contcategrprange1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-CONTCATEGBIND.md`
