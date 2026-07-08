---
id: UNC@20.15.2@MMLCommand@LST QOSCTRL
type: MMLCommand
name: LST QOSCTRL（查询QoS控制配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSCTRL
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 全局QoS功能配置
- 全局QoS控制功能
status: active
---

# LST QOSCTRL（查询QoS控制配置）

## 功能

**适用NF：SMF、SGW-C、PGW-C**

该命令用于查询配置了带宽控制全局开关的用户信息，包括用户无线接入类型和漫游属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSCTRL]] · QoS控制配置（QOSCTRL）

## 使用实例

查询配置了带宽控制全局开关的用户信息：

```
%%LST QOSCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
用户漫游类型  RAT类型                                                     

漫游用户      UNKOWN  
拜访用户      GETRAN  
本地用户      UNKOWN  
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询QoS控制配置（LST-QOSCTRL）_09652687.md`
