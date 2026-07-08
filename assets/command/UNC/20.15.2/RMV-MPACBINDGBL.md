---
id: UNC@20.15.2@MMLCommand@RMV MPACBINDGBL
type: MMLCommand
name: RMV MPACBINDGBL（删除MPAC全局策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MPACBINDGBL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- MPAC
- 全局策略配置
status: active
---

# RMV MPACBINDGBL（删除MPAC全局策略）

## 功能

该命令用于删除全局MPAC策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MPACBINDGBL]] · MPAC全局策略（MPACBINDGBL）

## 使用实例

删除MPAC全局策略：

```
RMV MPACBINDGBL:IPVERSION=IPv4;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MPAC全局策略（RMV-MPACBINDGBL）_49802258.md`
