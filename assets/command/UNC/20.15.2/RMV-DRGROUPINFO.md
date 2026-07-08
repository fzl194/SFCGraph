---
id: UNC@20.15.2@MMLCommand@RMV DRGROUPINFO
type: MMLCommand
name: RMV DRGROUPINFO（删除容灾组信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DRGROUPINFO
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# RMV DRGROUPINFO（删除容灾组信息）

## 功能

该命令用于删除一条指定的容灾组信息。

## 注意事项

- 该命令执行后立即生效。

- 该命令只用于在UEG-L/UEN网元采用主备（冷备）容灾模式下执行。
- 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。
- 该命令将删除主备容灾实例的关联，必须按照去激活主备容灾指导书中的步骤执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRGROUPID | 容灾组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于标识一条容灾组信息，不同容灾组信息的该标识不能相同。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DRGROUPINFO]] · 容灾组信息（DRGROUPINFO）

## 使用实例

删除一条指定的容灾组信息：

```
%%RMV DRGROUPINFO: DRGROUPID=1;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DRGROUPINFO.md`
