---
id: UDG@20.15.2@MMLCommand@MOD USRRELATEIDEN
type: MMLCommand
name: MOD USRRELATEIDEN（修改用户关联识别）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: USRRELATEIDEN
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 用户关联识别
status: active
---

# MOD USRRELATEIDEN（修改用户关联识别）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改指定的protocol的用户关联配置，对某些配置过用户关联功能的protocol，运营商的需求发生变化，不需要提升识别准确率时配置该命令。

## 注意事项

该命令执行后60s生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLNAME | 协议名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置对应的协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：当需要修改用户关联识别配置时配置该参数，该参数用于输入指定修改的协议名称。 |
| USRRLTIDENSW | 用户关联识别开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否开启用户关联识别功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：关闭用户关联识别功能。<br>- ENABLE：开启用户关联识别功能。<br>默认值：无<br>配置原则：<br>- DISABLE：关闭对应协议的用户关联识别功能。<br>- ENABLE：开启对应协议用户关联识别功能。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/USRRELATEIDEN]] · 用户关联识别（USRRELATEIDEN）

## 使用实例

假设运营商的某个应用有变更，不需要对https协议提升识别准确率时，需要修改指定protocol的用户关联识别功能：

```
MOD USRRELATEIDEN: PROTOCOLNAME="https",USRRLTIDENSW=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-USRRELATEIDEN.md`
