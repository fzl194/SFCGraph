---
id: UDG@20.15.2@MMLCommand@LST VONRMOSFACTOR
type: MMLCommand
name: LST VONRMOSFACTOR（查询MOS计算值的补偿因子）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VONRMOSFACTOR
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- VoNR质量监控配置
- VoNR MOS 补充因子
status: active
---

# LST VONRMOSFACTOR（查询MOS计算值的补偿因子）

## 功能

**适用NF：UPF**

该命令用于查询MOS计算值的补偿因子。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [MOS补偿因子（VONRMOSFACTOR）](configobject/UDG/20.15.2/VONRMOSFACTOR.md)

## 使用实例

查询MOS计算值的补偿因子：

```
LST VONRMOSFACTOR:;
```

```

RETCODE = 0  操作成功

MOS补偿因子配置
---------------
语音编解码类型    MOS补偿因子1    MOS补偿因子2    MOS补偿因子3    MOS补偿因子4    MOS补偿因子5

AMR NB            0               0                 0               0               0           
AMR WB            0               0                 0               0               0           
G.711             0               0                 0               0               0           
G.722             0               0                 0               0               0           
G.729             0               0                 0               0               0           
EVS NB            0               0                 0               0               0           
EVS WB            0               0                 0               0               0           
EVS SWB           0               0                 0               0               0           
EVS FB            0               0                 0               0               0           
EVS AMR-WB IO     0               0                 0               0               0           
(结果个数 = 10)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询MOS计算值的补偿因子（LST-VONRMOSFACTOR）_91056084.md`
