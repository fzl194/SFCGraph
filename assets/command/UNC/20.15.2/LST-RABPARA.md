---
id: UNC@20.15.2@MMLCommand@LST RABPARA
type: MMLCommand
name: LST RABPARA（查询RAB参数协商配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RABPARA
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- Pre-R8 QoS
- QoS协商控制
- Iu模式RAB参数协商
status: active
---

# LST RABPARA（查询RAB参数协商配置）

## 功能

**适用网元：SGSN**

此命令用于查询RAB参数协商配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/RABPARA]] · RAB参数协商配置（RABPARA）

## 使用实例

查询RAB参数协商配置

LST RABPARA:;

```
%%LST RABPARA:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                            可协商RAB参数  =  最大和保证速率
可选RAB的带宽与初始RAB的带宽的百分比（%）  =  50
                     上行最大速率协商列表  =  NULL
                     下行最大速率协商列表  =  NULL
                     上行保证速率协商列表  =  NULL
                     下行保证速率协商列表  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RAB参数协商配置(LST-RABPARA)_26146228.md`
