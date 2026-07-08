---
id: UNC@20.15.2@MMLCommand@LST NBFC
type: MMLCommand
name: LST NBFC（查看NB流控数据）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NBFC
command_category: 查询类
applicable_nf:
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
- NB-IoT业务流控管理
status: active
---

# LST NBFC（查看NB流控数据）

## 功能

**适用网元：MME**

该命令用于查询NB流控数据。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NBFC]] · 查看NB流控数据（NBFC）

## 使用实例

查询NB流控数据：

LST NBFC:;

```
%%LST NBFC:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
            NB_IoT流控开关  =  关闭
        CPU过载控制门限(%)  =  65
   流控速率最小值（个/秒）  =  10
   流控速率最大值（个/秒）  =  300
Back off timer最小值（秒）  =  900
Back off timer最大值（秒）  =  1800
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NBFC.md`
