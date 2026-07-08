---
id: UNC@20.15.2@MMLCommand@RMV EPSQOS4DEFBER
type: MMLCommand
name: RMV EPSQOS4DEFBER（删除Qos Profile缺省承载QoS属性）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: EPSQOS4DEFBER
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- EPS QoS配置
- 缺省承载的EPS QoS
status: active
---

# RMV EPSQOS4DEFBER（删除Qos Profile缺省承载QoS属性）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用来删除Qos Profile缺省承载QoS属性。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | Qos Profile名 | 可选必选说明：必选参数<br>参数含义：该参数用来指定Qos Profile名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD QOSPROFILE命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EPSQOS4DEFBER]] · Qos Profile缺省承载QoS属性（EPSQOS4DEFBER）

## 使用实例

删除QosProfileName为“test”的缺省承载Qos属性：

```
RMV EPSQOS4DEFBER:QOSPROFILENAME="test";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Qos-Profile缺省承载QoS属性（RMV-EPSQOS4DEFBER）_71516449.md`
