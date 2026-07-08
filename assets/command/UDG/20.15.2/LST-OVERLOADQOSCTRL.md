---
id: UDG@20.15.2@MMLCommand@LST OVERLOADQOSCTRL
type: MMLCommand
name: LST OVERLOADQOSCTRL（查询过载限速参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OVERLOADQOSCTRL
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 过载限速
- 过载限速参数
status: active
---

# LST OVERLOADQOSCTRL（查询过载限速参数）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询过载限速参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/OVERLOADQOSCTRL]] · 过载限速参数（OVERLOADQOSCTRL）

## 使用实例

查询过载限速功能配置，执行如下命令：

```
LST OVERLOADQOSCTRL:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------
           过载限速开关  =  使能
            CPU过载阈值  =  80
            CPU恢复阈值  =  75
上行最大带宽(千比特/秒)  =  1000
下行最大带宽(千比特/秒)  =  1000
           用户抽样方式  =  自动抽样
     过载限速判定周期数  =  12
 过载限速恢复判定周期数  =  36
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-OVERLOADQOSCTRL.md`
