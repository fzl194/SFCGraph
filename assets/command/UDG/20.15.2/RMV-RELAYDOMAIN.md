---
id: UDG@20.15.2@MMLCommand@RMV RELAYDOMAIN
type: MMLCommand
name: RMV RELAYDOMAIN（删除媒体中继域名配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RELAYDOMAIN
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继域名配置
status: active
---

# RMV RELAYDOMAIN（删除媒体中继域名配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除媒体中继域名配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYDOMAINNAME | 媒体中继域名配置名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置媒体中继域名配置名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：RELAYDOMAINNAME参数不允许与RELAYTPLNAME相同。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYDOMAIN]] · 媒体中继域名配置（RELAYDOMAIN）

## 使用实例

假如需要删除一组媒体中继域名配置，则命令如下：

```
RMV RELAYDOMAIN: RELAYDOMAINNAME="test001";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-RELAYDOMAIN.md`
