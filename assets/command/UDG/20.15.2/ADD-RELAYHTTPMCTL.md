---
id: UDG@20.15.2@MMLCommand@ADD RELAYHTTPMCTL
type: MMLCommand
name: ADD RELAYHTTPMCTL（增加媒体中继Http消息控制）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: RELAYHTTPMCTL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 20
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继HTTP消息控制
status: active
---

# ADD RELAYHTTPMCTL（增加媒体中继Http消息控制）

## 功能

**适用NF：PGW-U、UPF**

该命令用于添加媒体中继Http消息控制。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为20。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HTTPMSGCTRLNAME | 媒体中继Http消息控制名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定媒体中继Http消息控制名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYHTTPMCTL]] · 媒体中继Http消息控制（RELAYHTTPMCTL）

## 使用实例

假如需要创建一组媒体中继Http消息控制，则命令如下：

```
ADD RELAYHTTPMCTL:HTTPMSGCTRLNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加媒体中继Http消息控制（ADD-RELAYHTTPMCTL）_94871979.md`
