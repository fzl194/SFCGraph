---
id: UNC@20.15.2@MMLCommand@RMV EPSSUBQOS
type: MMLCommand
name: RMV EPSSUBQOS（删除EPS签约QoS配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: EPSSUBQOS
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
- 本地EPS QoS
status: active
---

# RMV EPSSUBQOS（删除EPS签约QoS配置）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用来删除用户的签约QoS属性的相关配置。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBQOSINDEX | 用户QoS索引 | 可选必选说明：必选参数<br>参数含义：该参数表示用户QoS索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@EPSSUBQOS]] · EPS签约QoS配置（EPSSUBQOS）

## 使用实例

删除“SUBQOSINDEX”为“123”的记录：

```
RMV EPSSUBQOS: SUBQOSINDEX=123;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-EPSSUBQOS.md`
