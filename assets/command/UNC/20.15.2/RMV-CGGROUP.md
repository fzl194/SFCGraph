---
id: UNC@20.15.2@MMLCommand@RMV CGGROUP
type: MMLCommand
name: RMV CGGROUP（删除CG组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CGGROUP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG组管理
- CG组
status: active
---

# RMV CGGROUP（删除CG组）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来删除指定的CG组。

## 注意事项

- 该命令执行后立即生效。
- 删除指定CG组，删除时必须要指定CG组的ID。
- 删除CG组，输入一个不存在的CG组的名字时，会提示删除失败。
- 如果CG组绑在离线计费模板下或被设置为全局CG组时，删除时则提示删除失败。
- 禁止在有用户在线时执行该命令，删除后会导致使用该CG组的用户在全局范围内选择CG发送话单。
- 禁止在该CG组下存在缓存话单时执行该命令，删除后会导致该CG组下的缓存话单无法发送。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CGGRPID | CG组ID | 可选必选说明：必选参数<br>参数含义：CG组的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CGGROUP]] · CG组（CGGROUP）

## 使用实例

删除CG组ID为1的CG组：

```
RMV CGGROUP: CGGRPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CGGROUP.md`
