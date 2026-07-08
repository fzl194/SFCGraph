---
id: UNC@20.15.2@MMLCommand@LST NBIOTRATVALUE
type: MMLCommand
name: LST NBIOTRATVALUE（查询NB-IoT终端配置的RAT值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NBIOTRATVALUE
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- NB-IoT用户RAT值
status: active
---

# LST NBIOTRATVALUE（查询NB-IoT终端配置的RAT值）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询NB-IoT终端接入时UNC给周边网元发送消息时RAT信元中填写的值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [NB-IoT终端配置的RAT值（NBIOTRATVALUE）](configobject/UNC/20.15.2/NBIOTRATVALUE.md)

## 使用实例

显示NB-IoT终端接入时UNC给周边网元发送消息时RAT值：

```
LST NBIOTRATVALUE:;
```

```

RETCODE = 0  操作成功

NB-IoT用户的RAT值
-----------------
          和OCS交互使用的RAT值  =  EUTRAN-NB-IoT
           和CG交互使用的RAT值  =  EUTRAN-NB-IoT
和AAA计费服务器交互使用的RAT值  =  EUTRAN-NB-IoT
和AAA鉴权服务器交互使用的RAT值  =  EUTRAN-NB-IoT
         和PCRF交互使用的RAT值  =  EUTRAN-NB-IoT
       SGW发送给PGW使用的RAT值  =  EUTRAN-NB-IoT
          和CHF交互使用的RAT值  =  EUTRAN-NB-IoT
          和PCF交互使用的RAT值  =  EUTRAN-NB-IoT
            和UPF交互使的RAT值  =  EUTRAN-NB-IoT
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NB-IoT终端配置的RAT值（LST-NBIOTRATVALUE）_09896821.md`
