---
id: UDG@20.15.2@MMLCommand@LST LOOPUDP
type: MMLCommand
name: LST LOOPUDP（查询UDP环回配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LOOPUDP
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- 逻辑接口管理
- 逻辑接口配置
- UDP环回
status: active
---

# LST LOOPUDP（查询UDP环回配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询UDP环回功能的配置情况。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/LOOPUDP]] · UDP环回配置（LOOPUDP）

## 使用实例

查询UDP环回配置：

```
LST LOOPUDP:;
```

```

RETCODE = 0  操作成功

UDP环回配置
-----------
        S1-U接口UDP环回开关  =  不使能
        Tx-U接口UDP环回开关  =  不使能
  S1-U接口UDP环回源IPv4地址  =  0.0.0.0
      S1-U接口UDP环回源端口  =  0
S1-U接口UDP环回目的IPv4地址  =  0.0.0.0
    S1-U接口UDP环回目的端口  =  0
        S1-U接口VPN实例名称  =  NULL
  Tx-U接口UDP环回源IPv4地址  =  0.0.0.0
      Tx-U接口UDP环回源端口  =  0
Tx-U接口UDP环回目的IPv4地址  =  0.0.0.0
    Tx-U接口UDP环回目的端口  =  0
        Tx-U接口VPN实例名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询UDP环回配置（LST-LOOPUDP）_70043012.md`
