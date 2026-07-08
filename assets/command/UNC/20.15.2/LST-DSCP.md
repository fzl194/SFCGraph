---
id: UNC@20.15.2@MMLCommand@LST DSCP
type: MMLCommand
name: LST DSCP（显示接口DSCP配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DSCP
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 接口DSCP管理
status: active
---

# LST DSCP（显示接口DSCP配置）

## 功能

**适用NF：NCG**

该命令用来查看NCG对外网元接口发送IP包时携带的DSCP值。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACE | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于选择信令报文修改DSCP值的接口类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- Ga：Ga。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DSCP]] · 接口DSCP配置（DSCP）

## 使用实例

查询NCG对外网元接口发送IP包时携带的DSCP配置：

```
LST DSCP：;
```

```
RETCODE = 0  操作成功。

结果如下:
--------
      接口类型  =  Ga
差分服务代码点  =  56
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示接口DSCP配置（LST-DSCP）_51174295.md`
