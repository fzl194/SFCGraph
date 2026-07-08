---
id: UNC@20.15.2@MMLCommand@RMV GLBPCRFGROUP
type: MMLCommand
name: RMV GLBPCRFGROUP（删除全局PCRF组绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GLBPCRFGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- 全局PCRF组
status: active
---

# RMV GLBPCRFGROUP（删除全局PCRF组绑定关系）

## 功能

**适用NF：PGW-C、GGSN**

此命令用来删除PCRF分组和指定的号段绑定，以及绑定优先级。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令支持批量删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置绑定的IMSIMSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBPCRFGROUP]] · 全局PCRF组绑定关系（GLBPCRFGROUP）

## 使用实例

删除GLBPCRFGROUP：IMSIMSISDNSEG为“ims”：

```
RMV GLBPCRFGROUP:IMSIMSISDNSEG="ims";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GLBPCRFGROUP.md`
