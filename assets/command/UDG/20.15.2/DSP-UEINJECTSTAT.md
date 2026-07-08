---
id: UDG@20.15.2@MMLCommand@DSP UEINJECTSTAT
type: MMLCommand
name: DSP UEINJECTSTAT（查询UE灌包状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: UEINJECTSTAT
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- UE侧连通性检测
- UE灌包信息
status: active
---

# DSP UEINJECTSTAT（查询UE灌包状态）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询当前灌包UE的灌包状态。

## 注意事项

该命令显示的信息在执行命令ACT UEINJECTSEND失败时不会被重置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UEINJECTSTAT]] · UE灌包状态（UEINJECTSTAT）

## 使用实例

查询UE下行灌包状态：

```
DSP UEINJECTSTAT:;
```

```

RETCODE = 0 操作成功。

UE灌包状态信息
--------------------------
UE灌包状态 =
            SENDER  =  0
          ForceEnd  =  0
      TotalSendNum  =  0
      TotalSendFLow =  0
          CurrRate  =  0
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-UEINJECTSTAT.md`
