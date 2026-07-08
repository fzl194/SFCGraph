---
id: UNC@20.15.2@MMLCommand@LST UNIHTR
type: MMLCommand
name: LST UNIHTR（查询统一HTR功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UNIHTR
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- HTR流控局向管理
- 统一HTR流控局向管理
- 统一HTR流控功能管理
status: active
---

# LST UNIHTR（查询统一HTR功能）

## 功能

**适用网元：SGSN、MME**

该命令用于查询统一HTR（Hard to Reach）流控功能的相关参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UNIHTR]] · 统一HTR功能（UNIHTR）

## 使用实例

查询固定速率流控信息： LST UNIHTR:;

```
%%LST UNIHTR:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
    局向流控开关  =  开启
启控速率配置策略  =  系统缺省值
 流控恢复阈值(%)  =  85
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UNIHTR.md`
