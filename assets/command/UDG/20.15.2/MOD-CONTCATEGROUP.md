---
id: UDG@20.15.2@MMLCommand@MOD CONTCATEGROUP
type: MMLCommand
name: MOD CONTCATEGROUP（修改内容分类组）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: CONTCATEGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容分类组配置
status: active
---

# MOD CONTCATEGROUP（修改内容分类组）

## 功能

**适用NF：PGW-U、UPF**

该命令用来修改内容分类组记录。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONTCATEGNAME | 内容分类组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容分类组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于设置优先级。数值越小优先级越高。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CONTCATEGROUP]] · 内容分类组（CONTCATEGROUP）

## 使用实例

修改内容分类组优先级为1：

```
MOD CONTCATEGROUP: CONTCATEGNAME="cf_contcategrprange1", PRIORITY=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-CONTCATEGROUP.md`
