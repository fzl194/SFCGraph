---
id: UNC@20.15.2@MMLCommand@ADD MPACBINDGBL
type: MMLCommand
name: ADD MPACBINDGBL（增加MPAC全局策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MPACBINDGBL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 2
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- MPAC
- 全局策略配置
status: active
---

# ADD MPACBINDGBL（增加MPAC全局策略）

## 功能

该命令用于配置全局MPAC策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为2。
- MPAC策略全局绑定仅支持绑定IPv4、IPv6策略各一条。
- 不支持修改命令，必须先删除原来绑定的策略，然后重新增加。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：无 |
| POLICYNAMEV4 | IPv4策略名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于指定IPv4策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。大小写敏感，英文字母开头，不支持空格。<br>默认值：无 |
| POLICYNAMEV6 | IPv6策略名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于指定IPv6策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。大小写敏感，英文字母开头，不支持空格。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MPACBINDGBL]] · MPAC全局策略（MPACBINDGBL）

## 使用实例

配置MPAC全局策略：

```
ADD MPACBINDGBL:IPVERSION=IPv4,POLICYNAMEV4="policyV4";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加MPAC全局策略（ADD-MPACBINDGBL）_49961826.md`
