---
id: UNC@20.15.2@MMLCommand@MOD TSTPCFSEL
type: MMLCommand
name: MOD TSTPCFSEL（修改拨测用户与PCF服务区的绑定关系）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD TSTPCFSEL（修改拨测用户与PCF服务区的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于修改用户与PCF服务区的绑定关系。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 用户的IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是14~15。每个字符只能是十进制数字。<br>默认值：无<br>配置原则：<br>该参数表示用户完整的IMSI信息，不支持前缀匹配。 |
| SERVINGSCOPE | PCF服务区名称 | 可选必选说明：必选参数<br>参数含义：该参数用于描述目标PCF的服务区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。 区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TSTPCFSEL]] · 拨测用户与PCF服务区的绑定关系（TSTPCFSEL）

## 使用实例

修改IMSI是"123456789012345"的用户激活到PCF业务服务区是“testservingscope”的PCF。

```
MOD TSTPCFSEL:IMSI="123456789012345",SERVINGSCOPE="testservingscope";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-TSTPCFSEL.md`
