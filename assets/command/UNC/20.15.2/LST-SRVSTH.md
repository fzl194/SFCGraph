---
id: UNC@20.15.2@MMLCommand@LST SRVSTH
type: MMLCommand
name: LST SRVSTH（查询业务功能开关状态）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SRVSTH
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 业务功能开关
status: active
---

# LST SRVSTH（查询业务功能开关状态）

## 功能

**适用NF：NCG**

该命令用于查询业务功能开关。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRVSTH]] · 业务功能开关状态（SRVSTH）

## 使用实例

查询业务功能开关：

```
LST SRVSTH:;
```

```
RETCODE = 0  操作成功

结果如下:
---------
                负载均衡开关  =  开启
       RU间负载不均的检测阈值  =  5
           检查无效链路的开关  =  开启
           GA无效链路老化时长  =  4320
     Ga口链路Cancel帧流控开关  =  关闭
     Ga口链路测试空帧流控开关  =  关闭
   Ga口链路可能重复帧流控开关  =  关闭
   Ga口正常数据帧重发异常检测  =  关闭
 GA链路可能重复帧缓存老化时长  =  1440
 GA链路可能重复帧剔重异常校验  =  关闭
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询业务功能开关状态（LST-SRVSTH）_41462209.md`
