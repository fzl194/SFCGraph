---
id: UNC@20.15.2@MMLCommand@LST INTERMMEFC
type: MMLCommand
name: LST INTERMMEFC（查询Inter-MME流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: INTERMMEFC
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- Inter-MME接入流控管理
status: active
---

# LST INTERMMEFC（查询Inter-MME流控参数）

## 功能

**适用网元：MME**

该命令用于查询Inter-MME接入流控功能的相关参数。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/INTERMMEFC]] · Inter-MME流控参数（INTERMMEFC）

## 使用实例

查询Inter-MME流控参数：

LST INTERMMEFC:;

```
%%LST INTERMMEFC:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
Inter-MME接入流控功能开关  =  开启
           流控速率最小值  =  10
           流控速率最大值  =  200
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Inter-MME流控参数(LST-INTERMMEFC)_26146164.md`
