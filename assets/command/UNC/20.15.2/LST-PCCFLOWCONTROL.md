---
id: UNC@20.15.2@MMLCommand@LST PCCFLOWCONTROL
type: MMLCommand
name: LST PCCFLOWCONTROL（查询PCC流控配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCCFLOWCONTROL
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- PCC公共参数
status: active
---

# LST PCCFLOWCONTROL（查询PCC流控配置）

## 功能

**适用NF：PGW-C、SMF**

此命令用于查询UNC重授权请求的消息发送速率和SMF接收PCF的Npcf_SMPolicyControl_UpdateNotify消息的速率。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [PCC流控配置（PCCFLOWCONTROL）](configobject/UNC/20.15.2/PCCFLOWCONTROL.md)

## 使用实例

查询PCC流控配置：

```
LST PCCFLOWCONTROL:;
```

```

RETCODE = 0  操作成功

PCC流控配置参数
---------------
Revalidation发送速率  =  25
UpdateNotify消息接收速率 = 2000
TerminateNotify消息接收速率 = 2000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PCC流控配置（LST-PCCFLOWCONTROL）_34160974.md`
