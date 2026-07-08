---
id: UDG@20.15.2@MMLCommand@LST IPSQMADJUST
type: MMLCommand
name: LST IPSQMADJUST（查询IPSQM调整参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPSQMADJUST
command_category: 查询类
applicable_nf:
- SGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- IPSQM控制
- IPSQM参数调整配置
status: active
---

# LST IPSQMADJUST（查询IPSQM调整参数）

## 功能

**适用NF：SGW-U、UPF**

该命令用于查询业务处理节点（POD）的最低保护带宽及突发尺寸。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPSQMADJUST]] · IPSQM调整参数（IPSQMADJUST）

## 使用实例

业务处理节点（POD）的最低保护带宽及突发尺寸：

```
LST IPSQMADJUST:;
```

```

RETCODE = 0  操作成功

IPSQM调整参数
-------------
                阈值（兆比特/秒）  =  30
低带宽域的最低保护值（千比特/秒）  =  300
       低带宽域的突发尺寸（字节）  =  2000
高带宽域的最低保护值（千比特/秒）  =  1000
       高带宽域的突发尺寸（字节）  =  10000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IPSQMADJUST.md`
