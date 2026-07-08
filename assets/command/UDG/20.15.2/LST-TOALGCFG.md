---
id: UDG@20.15.2@MMLCommand@LST TOALGCFG
type: MMLCommand
name: LST TOALGCFG（查询TCP算法配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOALGCFG
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP算法配置
status: active
---

# LST TOALGCFG（查询TCP算法配置）

## 功能

**适用NF：UPF**

该命令用于查询TCP算法配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [TCP算法配置（TOALGCFG）](configobject/UDG/20.15.2/TOALGCFG.md)

## 使用实例

查询TCP算法配置：

```
LST TOALGCFG:;
```

```

RETCODE = 0  操作成功

TCP算法配置
-----------
TCP拥塞控制算法  =  CCALG_CUBIC
慢启动阶段的门限值计算因子  =  717
启动hybrid slow start算法  =  ENABLE
初始拥塞窗口  =  64
TCP初始接收窗口  =  64
启动hybrid slow start算法的最小拥塞窗口门限值  =  512
Forward Acknowledgement算法  =  ENABLE
每个套接字TCP队列的大小  =  131072
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询TCP算法配置（LST-TOALGCFG）_44249106.md`
