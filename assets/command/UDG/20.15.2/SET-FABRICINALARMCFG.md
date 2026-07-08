---
id: UDG@20.15.2@MMLCommand@SET FABRICINALARMCFG
type: MMLCommand
name: SET FABRICINALARMCFG（设置PAE告警配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FABRICINALARMCFG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# SET FABRICINALARMCFG（设置PAE告警配置）

## 功能

该命令用来设置PAE的Fabric-In平面“ALM-100338 Fabric平面状态为Down”告警的屏蔽配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令开启屏蔽告警后，需要手动清除已产生的告警。

- 该命令存在系统初始记录，参数的初始设置值如下表：
  | ENABLE |
  | --- |
  | TRUE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组;

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENABLE | 屏蔽告警标记 | 可选必选说明：必选参数<br>参数含义：该参数用于开启和关闭告警屏蔽功能。<br>数据来源：本端规划<br>取值范围：布尔类型。<br>- TRUE：标识告警屏蔽。<br>- FALSE：标识告警不屏蔽。<br>默认值：TRUE<br>配置原则：无。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FABRICINALARMCFG]] · PAE告警配置（FABRICINALARMCFG）

## 使用实例

开启PAE的Fabric-In平面“ALM-100338 Fabric平面状态为Down”告警屏蔽功能，Fabric-In平面“ALM-100338 Fabric平面状态为Down”告警不再上报：

```
%%SET FABRICINALARMCFG: ENABLE=TRUE;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-FABRICINALARMCFG.md`
