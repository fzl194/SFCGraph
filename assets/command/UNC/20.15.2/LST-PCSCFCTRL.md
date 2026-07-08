---
id: UNC@20.15.2@MMLCommand@LST PCSCFCTRL
type: MMLCommand
name: LST PCSCFCTRL（查询P-CSCF控制配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCSCFCTRL
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- IMS管理
- P-CSCF管理
- P-CSCF故障恢复控制
status: active
---

# LST PCSCFCTRL（查询P-CSCF控制配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询P-CSCF控制属性配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCSCFCTRL]] · P-CSCF控制配置（PCSCFCTRL）

## 使用实例

显示P-CSCF故障后是否主动向用户侧发送UpdateBearerRequest消息配置信息：

```
%%LST PCSCFCTRL:;%%
RETCODE = 0 操作成功

结果如下
------------
故障恢复 = 使能
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PCSCFCTRL.md`
