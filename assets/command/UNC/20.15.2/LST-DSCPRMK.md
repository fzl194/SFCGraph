---
id: UNC@20.15.2@MMLCommand@LST DSCPRMK
type: MMLCommand
name: LST DSCPRMK（查询重映射对应表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DSCPRMK
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- DSCP
- DSCP重映射管理
status: active
---

# LST DSCPRMK（查询重映射对应表）

## 功能

**适用网元：SGSN**

该命令用于查询重映射对应表。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DSCPRMK]] · 重映射对应表（DSCPRMK）

## 使用实例

查询DSCP重标记关系：

LST DSCPRMK:;

```
%%LST DSCPRMK:;%%
RETCODE = 0  执行成功。

输出结果如下
------------
   违反规则报文行为  =  重标记
 EF类重标志后的DSCP  =  4类确保转发
  AF4重标志后的DSCP  =  尽力转发
  AF3重标志后的DSCP  =  尽力转发
  AF2重标志后的DSCP  =  尽力转发
  AF1重标志后的DSCP  =  尽力转发
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DSCPRMK.md`
