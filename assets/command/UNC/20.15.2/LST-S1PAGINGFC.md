---
id: UNC@20.15.2@MMLCommand@LST S1PAGINGFC
type: MMLCommand
name: LST S1PAGINGFC（查询S1寻呼流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1PAGINGFC
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
- S1寻呼流控管理
status: active
---

# LST S1PAGINGFC（查询S1寻呼流控参数）

## 功能

**适用网元：MME**

该命令用于查询S1模式寻呼流控功能的相关参数。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [S1寻呼流控参数（S1PAGINGFC）](configobject/UNC/20.15.2/S1PAGINGFC.md)

## 使用实例

查询S1寻呼流控参数：

LST S1PAGINGFC:;

```
%%LST S1PAGINGFC:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
         S1寻呼流控功能开关  =  开启
            SGs寻呼流控开关  =  开启
           S102寻呼流控开关  =  开启
           寻呼重发控制开关  =  开启
       寻呼突发预防功能开关  =  开启
  寻呼流控速率门限（次/秒）  =  150
寻呼流控速率最小值（次/秒）  =  10
             寻呼预留处理量  =  15
         语音寻呼预留处理量  =  5
        PAE反压流控功能开关  =  开启
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1寻呼流控参数(LST-S1PAGINGFC)_72225835.md`
