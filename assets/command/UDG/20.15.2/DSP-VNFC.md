---
id: UDG@20.15.2@MMLCommand@DSP VNFC
type: MMLCommand
name: DSP VNFC（显示VNFC）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: VNFC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 操作维护
- 配置管理
- VNFC信息
status: active
---

# DSP VNFC（显示VNFC）

## 功能

该命令用于查看VNFC信息，比如VNFC的ID、名称、类型、状态，以及启动时间等信息，通过这些信息可以了解启动的VNFC是否正确，及当故障发生时，依据查询到的信息进行故障诊断。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNFCNAME | VNFC名称 | 可选必选说明：可选参数<br>参数含义：VNFC名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VNFC]] · 重启系统（VNFC）

## 使用实例

显示VNFC：

```
DSP VNFC:;
```

```
 
RETCODE = 0  操作成功

结果如下:
-------------------------
VNFC ID   VNFC名称    VNFC类型名称     VNFC状态    VNFC创建时间           资源类型    VM1的名称    VM2的名称    基础版本           补丁版本          初始启动配置文件名称     内联管理口IP

0         VNFP        VNFP             运行中      2016-05-05 10:18:59    无          NULL         NULL         V100R018C00B110    NULL              NULL                     192.168.1.1
2         ipnls       VNRS_VNFC        运行中      2016-05-06 17:44:07    无          NULL         NULL         V100R018C00B110    NULL              NULL                     192.168.1.2
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-VNFC.md`
