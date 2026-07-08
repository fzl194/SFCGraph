---
id: UDG@20.15.2@MMLCommand@DSP TSNINFO
type: MMLCommand
name: DSP TSNINFO（显示TSN信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TSNINFO
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- TM路径管理
- TSN节点信息
status: active
---

# DSP TSNINFO（显示TSN信息）

## 功能

**适用NF：SGW-U、PGW-U**

用来查看TSN信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TSNINFO]] · TSN信息（TSNINFO）

## 使用实例

运行该命令，显示当前TSN信息：

```
DSP TSNINFO:;
```

```

RETCODE = 0 操作成功

TSN 信息:
---------------
TSN info  =  
Master TSN      
          NE ID Code Len = 1
              NE ID Code = 16
              NE ID Name = TSN1
               NE Status = Activity
              IP Address = 10.0.0.0
                Recovery = 1
             Create Time = 17:45:58 07/15/2022(MM/DD/YYYY)
             Active Time = 17:45:58 07/15/2022(MM/DD/YYYY)
        Last Update Time = 17:45:58 07/15/2022(MM/DD/YYYY)
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-TSNINFO.md`
