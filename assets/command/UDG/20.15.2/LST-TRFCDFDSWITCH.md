---
id: UDG@20.15.2@MMLCommand@LST TRFCDFDSWITCH
type: MMLCommand
name: LST TRFCDFDSWITCH（查询大流量攻击防护配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TRFCDFDSWITCH
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- DDoS防护
- 大流量攻击防护开关
status: active
---

# LST TRFCDFDSWITCH（查询大流量攻击防护配置）

## 功能

**适用NF：UPF**

该命令用来查询整机粒度是否开启大流量攻击检测功能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TRFCDFDSWITCH]] · 大流量攻击防护配置（TRFCDFDSWITCH）

## 使用实例

查询整机粒度大流量攻击检测功能开关状态：

```
LST TRFCDFDSWITCH:;
```

```

RETCODE = 0 操作成功。

大流量攻击防护配置信息
----------------------
上行大流量攻击检测开关  =  使能
下行大流量攻击检测开关  =  使能
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TRFCDFDSWITCH.md`
