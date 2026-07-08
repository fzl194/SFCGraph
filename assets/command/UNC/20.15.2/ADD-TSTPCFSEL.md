---
id: UNC@20.15.2@MMLCommand@ADD TSTPCFSEL
type: MMLCommand
name: ADD TSTPCFSEL（增加拨测用户与PCF服务区的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TSTPCFSEL
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCF发现和选择管理
- PCF服务区拨测管理
status: active
---

# ADD TSTPCFSEL（增加拨测用户与PCF服务区的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于配置用户和PCF服务区的绑定关系。一般用于拨测场景，将指定IMSI的用户激活到指定的PCF服务区上，测试PCF的基本功能。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 该命令用于拨测PCF，拨测完成后建议立即删除该配置。
- 一个IMSI只能配置一个PCF服务区域。
- 拨测PCF的命令有两条，该命令和ADD TSTPCFBINDING。ADD TSTPCFBINDING的优先级高于该命令。

- 最多可输入100条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 用户的IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是14~15。每个字符只能是十进制数字。<br>默认值：无<br>配置原则：<br>该参数表示用户完整的IMSI信息，不支持前缀匹配。 |
| SERVINGSCOPE | PCF服务区名称 | 可选必选说明：必选参数<br>参数含义：该参数用于描述目标PCF的服务区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。 区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TSTPCFSEL]] · 拨测用户与PCF服务区的绑定关系（TSTPCFSEL）

## 使用实例

配置IMSI是"123456789012345"的用户激活到PCF业务服务区是“testservingscope”的PCF。

```
ADD TSTPCFSEL:IMSI="123456789012345",SERVINGSCOPE="testservingscope";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TSTPCFSEL.md`
