---
id: UNC@20.15.2@MMLCommand@RMV 5GCSUBQOS
type: MMLCommand
name: RMV 5GCSUBQOS（删除5GC签约QoS配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: 5GCSUBQOS
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 本地5GC QoS
status: active
---

# RMV 5GCSUBQOS（删除5GC签约QoS配置）

## 功能

**适用NF：SMF**

该命令用来删除5G用户的签约QoS属性的相关配置。

## 注意事项

- 命令执行后只对新接入用户生效。

- 若5G用户的签约QoS属性被ADD QOSPROFILE或SET QOSGLOBAL引用时，不能直接删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBQOSINDEX | 用户QoS索引 | 可选必选说明：必选参数<br>参数含义：该参数表示用户QoS索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5GC签约QoS配置（5GCSUBQOS）](configobject/UNC/20.15.2/5GCSUBQOS.md)

## 使用实例

删除“QoS索引”为“1”的5GC签约QoS配置：

```
RMV 5GCSUBQOS:SUBQOSINDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5GC签约QoS配置（RMV-5GCSUBQOS）_09652552.md`
