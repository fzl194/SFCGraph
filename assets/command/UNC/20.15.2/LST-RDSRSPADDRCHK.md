---
id: UNC@20.15.2@MMLCommand@LST RDSRSPADDRCHK
type: MMLCommand
name: LST RDSRSPADDRCHK（查询全局RADIUS响应消息源端口检查配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RDSRSPADDRCHK
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- RADIUS响应消息地址检查
status: active
---

# LST RDSRSPADDRCHK（查询全局RADIUS响应消息源端口检查配置）

## 功能

**适用NF：PGW-C、SMF**

该命令用来显示全局RADIUS响应消息源IP/端口检查配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RDSRSPADDRCHK]] · 全局RADIUS响应消息源端口检查配置（RDSRSPADDRCHK）

## 使用实例

显示全局RADIUS响应消息源IP/端口检查配置信息：

```
LST RDSRSPADDRCHK:;
```

```

RETCODE = 0  操作成功

全局RADIUS响应消息源端口检查配置
--------------------------------
RADIUS鉴权响应消息源IP/端口检查开关  =  允许
RADIUS计费响应消息源IP/端口检查开关  =  允许
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RDSRSPADDRCHK.md`
