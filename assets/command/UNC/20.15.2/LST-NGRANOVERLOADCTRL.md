---
id: UNC@20.15.2@MMLCommand@LST NGRANOVERLOADCTRL
type: MMLCommand
name: LST NGRANOVERLOADCTRL（查询5G基站过载监控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGRANOVERLOADCTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGRAN接入管理控制
status: active
---

# LST NGRANOVERLOADCTRL（查询5G基站过载监控参数）

## 功能

**适用NF：AMF**

该命令用于查询5G基站过载监控相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [5G基站过载监控参数（NGRANOVERLOADCTRL）](configobject/UNC/20.15.2/NGRANOVERLOADCTRL.md)

## 使用实例

查询TALIST下基站过载监控相关参数，执行如下命令：

```
%%LST NGRANOVERLOADCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
TALIST下基站过载检测开关  =  OFF
            过载阈值(个)  =  400
            恢复阈值(个)  =  300
          核查周期(分钟)  =  60
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G基站过载监控参数（LST-NGRANOVERLOADCTRL）_09227301.md`
