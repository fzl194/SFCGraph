---
id: UDG@20.15.2@MMLCommand@LST SIPSIGMIRRORPARA
type: MMLCommand
name: LST SIPSIGMIRRORPARA（查询镜像SIP信令功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SIPSIGMIRRORPARA
command_category: 查询类
applicable_nf:
- SGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- VOLTE管理
- SIP信令功能
status: active
---

# LST SIPSIGMIRRORPARA（查询镜像SIP信令功能）

## 功能

**适用NF：SGW-U、UPF**

该命令用于查询SIP镜像功能是否使能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SIPSIGMIRRORPARA]] · 镜像SIP信令功能（SIPSIGMIRRORPARA）

## 使用实例

该命令用于查询SIP镜像功能是否使能：

```
LST SIPSIGMIRRORPARA:;
```

```

RETCODE = 0  操作成功

结果如下
--------
       镜像功能开关  =  不使能
内层IPv6报文分片MTU  =  0
          重定向VPN  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询镜像SIP信令功能（LST-SIPSIGMIRRORPARA）_30165424.md`
