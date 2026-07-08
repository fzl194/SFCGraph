---
id: UNC@20.15.2@MMLCommand@LST ANTIATTACK
type: MMLCommand
name: LST ANTIATTACK（查询防报文攻击上限）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ANTIATTACK
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- 防报文攻击配置
status: active
---

# LST ANTIATTACK（查询防报文攻击上限）

## 功能

**适用网元：SGSN、MME**

该命令用来查询防报文攻击个数的上限值。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/ANTIATTACK]] · 防报文攻击上限（ANTIATTACK）

## 使用实例

查询防报文攻击上限:

LST ANTIATTACK:;

```
%%LST ANTIATTACK:;%%
RETCODE = 0  操作成功。

查询结果如下
------------
 GTP信令流量控制开关  =  启用
每秒接收信令个数上限  =  300
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询防报文攻击上限(LST-ANTIATTACK)_72225583.md`
