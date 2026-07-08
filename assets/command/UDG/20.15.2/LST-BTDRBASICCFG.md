---
id: UDG@20.15.2@MMLCommand@LST BTDRBASICCFG
type: MMLCommand
name: LST BTDRBASICCFG（查询BTDR单据上报参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: BTDRBASICCFG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 智能板管理
- 实时流北向配置管理
- 基本信息配置
status: active
---

# LST BTDRBASICCFG（查询BTDR单据上报参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询BTDR单据上报参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [BTDR单据上报参数（BTDRBASICCFG）](configobject/UDG/20.15.2/BTDRBASICCFG.md)

## 使用实例

查询BTDR单据上报参数：

```
%%LST BTDRBASICCFG:;
```

```
%%
RETCODE = 0  Operation succeeded

Parameters for reporting BTDRs
------------------------------
                         Reporting Switch  =  ENABLE
                     Reporting Period (s)  =  50
UDP Packet Payload Maximum Length (bytes)  =  520
       Cache Duration of Sent Packets (s)  =  30
                  Pseudonymization Switch  =  ENABLE
                    Pseudonymization Mode  =  PRE_DEFINED
               Pseudonymization Algorithm  =  HMACSHA256
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询BTDR单据上报参数（LST-BTDRBASICCFG）_19881190.md`
