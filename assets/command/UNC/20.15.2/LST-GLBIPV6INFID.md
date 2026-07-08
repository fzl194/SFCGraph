---
id: UNC@20.15.2@MMLCommand@LST GLBIPV6INFID
type: MMLCommand
name: LST GLBIPV6INFID（查询整机IPv6接口ID配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBIPV6INFID
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- IPv6接口标识管理
- 全局IPv6接口标识管理
status: active
---

# LST GLBIPV6INFID（查询整机IPv6接口ID配置）

## 功能

**适用NF：PGW-C、GGSN、SMF**

此命令用于查询IMSI作为用户的IPv6地址Interface ID功能开关配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [整机IPv6接口ID配置（GLBIPV6INFID）](configobject/UNC/20.15.2/GLBIPV6INFID.md)

## 使用实例

查询IMSI作为用户的IPv6地址Interface ID功能配置：

```
%%LST GLBIPV6INFID:;%%
RETCODE = 0  操作成功

结果如下
--------
配置IMSI作为IPv6 Interface ID  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询整机IPv6接口ID配置（LST-GLBIPV6INFID）_96242150.md`
