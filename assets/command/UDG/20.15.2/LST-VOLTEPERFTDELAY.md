---
id: UDG@20.15.2@MMLCommand@LST VOLTEPERFTDELAY
type: MMLCommand
name: LST VOLTEPERFTDELAY（查询理想报文的最小时延偏差、固定传输时延）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VOLTEPERFTDELAY
command_category: 查询类
applicable_nf:
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- VoLTE 理想到达报文
status: active
---

# LST VOLTEPERFTDELAY（查询理想报文的最小时延偏差、固定传输时延）

## 功能

**适用NF：PGW-U**

该命令用于查询理想报文的最小时延偏差、固定传输时延。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/VOLTEPERFTDELAY]] · 理想到达报文的最小时延偏差、固定传输时延（VOLTEPERFTDELAY）

## 使用实例

查询理想报文的最小时延偏差、固定传输：

```
LST VOLTEPERFTDELAY:;
```

```

RETCODE = 0  操作成功

理想报文的最小时延偏差、固定传输时延
------------------------------------
理想到达报文的最小时延偏差  =  10
理想时延报文的固定传输时延  =  180
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-VOLTEPERFTDELAY.md`
