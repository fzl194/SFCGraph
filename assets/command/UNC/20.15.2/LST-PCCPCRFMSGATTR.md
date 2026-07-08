---
id: UNC@20.15.2@MMLCommand@LST PCCPCRFMSGATTR
type: MMLCommand
name: LST PCCPCRFMSGATTR（查询PCRF返回消息属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCCPCRFMSGATTR
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
- 信令控制
- 服务器端信元控制
status: active
---

# LST PCCPCRFMSGATTR（查询PCRF返回消息属性）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询PCRF返回消息属性的配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCPCRFMSGATTR]] · PCRF返回消息属性（PCCPCRFMSGATTR）

## 使用实例

查询PCRF返回消息属性的配置：

```
LST PCCPCRFMSGATTR:;
```

```

RETCODE = 0  操作成功

PCRF消息属性信息
----------------
基于CCA-U Origin-Host AVP触发PCRF重选  =  禁止
  基于RAR Origin-Host AVP触发PCRF重选  =  禁止
基于CCA-I Origin-Host AVP触发PCRF重选  =  禁止
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PCCPCRFMSGATTR.md`
